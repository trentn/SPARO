// include the librealsense C++ header file
#include <librealsense2/rs.hpp>
#include <librealsense2/rsutil.h>

// include OpenCV header file
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

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

    //color_frame = frames.get_color_frame();
    //depth_frame = frames.get_depth_frame();


    /*
    //generate point cloud & get vertices
    rs2::pointcloud pc;
    rs2::points points = pc.calculate(depth_frame);
    pc.map_to(color_frame);
    auto vertices = points.get_vertices();
    */

    
    //filter on color
    Mat color(Size(640, 480), CV_8UC3, (void*)color_frame.get_data(), Mat::AUTO_STEP);
    Mat depth(Size(640, 480), CV_8UC3, (void*)depth_frame.get_data(), Mat::AUTO_STEP);

    cvtColor(color, color_HSV, COLOR_BGR2HSV);
    inRange(color_HSV,
            Scalar(target_color->low_H, target_color->low_S, target_color->low_V),
            Scalar(target_color->high_H, target_color->high_S, target_color->high_V), color_filtered);

    //Mat depth_filtered;
    //bitwise_and(depth, depth.clone(), depth_filtered, color_filtered);


    //get center of "blob"
    Moments m = moments(color_filtered, true);
    Point p(m.m10/m.m00, m.m01/m.m00);

    circle(color, p, 5, Scalar(128,0,0), -1);

    //extract x,y,z
    /*
    auto centroid = vertices[p.x*p.y];
    cout << "X:" << centroid.x
         << " Y:" << centroid.y
         << " Z:" << centroid.z
         << endl;
    */

    
    cout << depth.at<float>((int)p.x, (int)p.y) << endl;
    
    cout << depth_frame.as<rs2::depth_frame>().get_distance((int)p.x,  (int)p.y) << endl;

    float threeD_point[3] = {0};
    float pixel[2] = {p.x, p.y};
    //default depth scale is 1mm
    rs2_deproject_pixel_to_point(threeD_point, &c_intrinsics, pixel, depth_frame.as<rs2::depth_frame>().get_distance((int)p.x,  (int)p.y));

    
    cout << "X: " << threeD_point[0]
         << " Y: " << threeD_point[1]
         << " Z: " << threeD_point[2]
         << endl;

    imshow("Color Image", color);
    imshow("Color Mask", color_filtered);
    //imshow("Depth Map", depth);
    //imshow("Filtered Depth", depth_filtered);
    
    waitKey(0);

    return 0;
}
