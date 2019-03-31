// include the librealsense C++ header file
#include <librealsense2/rs.hpp>
#include <librealsense2/rsutil.h>

// include OpenCV header file
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

void detect_target();

struct HSV {
    int low_H;
    int high_H;
    int low_S;
    int high_S;
    int low_V;
    int high_V;
};


struct HSV blue     = {100, 110, 150, 255, 50, 255};
struct HSV orange   = {0, 15, 150, 255, 100, 255};
struct HSV teal     = {70, 130, 150, 255, 80, 255};

struct HSV* target_color = &blue;

int main(int argc, char** argv) {
    if(argc > 1) {
        switch(argv[1][0]) {
            case 'b':   target_color = &blue;
                        break;
            case 'o':   target_color = &orange;
                        break;
            case 't':   target_color = &teal;
                        break; 
        }
    }

    detect_target();

    return 0;
}


void detect_target(){
        rs2::colorizer color_map;
    rs2::pipeline pipe;
    rs2::config cfg;

    cfg.enable_stream(RS2_STREAM_DEPTH, 640, 480);
    cfg.enable_stream(RS2_STREAM_COLOR, 640, 480, RS2_FORMAT_BGR8, 30);
    
    pipe.start(cfg);

    auto const c_intrinsics = pipe.get_active_profile().get_stream(RS2_STREAM_COLOR).as<rs2::video_stream_profile>().get_intrinsics();


    // Camera warmup - dropping several first frames to let auto-exposure stabilize
    rs2::frameset frames;
    for(int i = 0; i < 60; i++)
    {
        frames = pipe.wait_for_frames();
    }
    rs2::align align = rs2::align(RS2_STREAM_COLOR);
    auto aligned_frames = align.process(frames);

    rs2::frame color_frame, depth_frame;
    Mat color_HSV, color_filtered;

    color_frame = aligned_frames.get_color_frame();
    depth_frame = aligned_frames.get_depth_frame();
    
    //filter on color
    Mat color(Size(640, 480), CV_8UC3, (void*)color_frame.get_data(), Mat::AUTO_STEP);
    Mat depth(Size(640, 480), CV_8UC3, (void*)depth_frame.get_data(), Mat::AUTO_STEP);

    cvtColor(color, color_HSV, COLOR_BGR2HSV);
    inRange(color_HSV,
            Scalar(target_color->low_H, target_color->low_S, target_color->low_V),
            Scalar(target_color->high_H, target_color->high_S, target_color->high_V), color_filtered);

    //mask edges
    Mat mask = Mat::zeros(Size(640,480), CV_8U);
    mask(Rect(210,50,210,380)) = 255;
    Mat color_masked;
    bitwise_and(color_filtered, color_filtered.clone(), color_masked, mask);

    //Mat depth_filtered;
    //bitwise_and(depth, depth.clone(), depth_filtered, color_filtered);


    //get center of "blob"
    Moments m = moments(color_masked, true);
    Point p(m.m10/m.m00, m.m01/m.m00);

    circle(color, p, 5, Scalar(128,0,0), -1);

    //extract x,y,z
    //cout << depth.at<float>((int)p.x, (int)p.y) << endl;    
    //cout << depth_frame.as<rs2::depth_frame>().get_distance((int)p.x,  (int)p.y) << endl;

    float threeD_point[3] = {0};
    float pixel[2] = {p.x, p.y};
    //default depth scale is 1mm
    rs2_deproject_pixel_to_point(threeD_point, &c_intrinsics, pixel, depth_frame.as<rs2::depth_frame>().get_distance((int)p.x,  (int)p.y));

    
    
    //bounding boxes
    int thresh = 1;
    RNG rng(12345);
    Mat canny_output;
    Canny(color_masked, canny_output, thresh, thresh);

    vector<vector<Point>> contours;
    findContours(canny_output, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

    vector<vector<Point>> contours_poly(contours.size());
    vector<RotatedRect> rBoundingRect(contours.size());

    for(int i = 0; i < contours.size(); i++) {
        approxPolyDP(contours[i], contours_poly[i], 1, true);
        rBoundingRect[i] = minAreaRect(contours_poly[i]);
    }
    
    for(int i = 0; i < contours_poly.size(); i++){
        Scalar bcolor = Scalar(rng.uniform(0,256), rng.uniform(0,256), rng.uniform(0,256));
        drawContours(color, contours_poly, (int)i, bcolor);
        Point2f vertices[4];
        rBoundingRect[i].points(vertices);
        for(int j = 0; j < 4; j++){
            line(color, vertices[j], vertices[(j+1)%4], bcolor, 2);
        }
    }
    cout << contours.size() << endl;
    cout << contours_poly.size() << endl;
    
    
    cout << "X: " << threeD_point[0]
         << " Y: " << threeD_point[1]
         << " Z: " << threeD_point[2]
         << endl;

    imshow("Color Image", color);
    imshow("Color Mask", color_masked);
    imshow("Mask", mask);
    //imshow("Depth Map", depth);
    //imshow("Filtered Depth", depth_filtered);
    
    waitKey(0);
}