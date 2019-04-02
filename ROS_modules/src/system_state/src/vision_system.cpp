// include ros related header
#include "ros/ros.h"
#include "system_state/DetectTarget.h"

// include the librealsense C++ header file
#include <librealsense2/rs.hpp>
#include <librealsense2/rsutil.h>

// include OpenCV header file
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

bool detect_target(system_state::DetectTarget::Request &req,
                   system_state::DetectTarget::Response &res);

enum TargetType {VALVE1, VALVE2, VALVE3, BREAKER};

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

struct HSV* target_color = &teal;

int main(int argc, char** argv) {
    ros::init(argc, argv, "vision_system");
    ros::NodeHandle n;

    ros::ServiceServer service = n.advertiseService("detect_target", detect_target);
    ROS_INFO("Vision System ready");
    ros::spin();

    return 0;
}


bool detect_target(system_state::DetectTarget::Request &req,
                   system_state::DetectTarget::Response &res){
    
    switch(req.target){
        case VALVE1:  target_color = &blue;
                             break;

        case VALVE2:  target_color = &orange;
                             break;

        case VALVE3:  target_color = &blue;
                             break;

        case BREAKER: target_color = &orange;
                             break;

        default: break;
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
    // align frames and extract data
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

    //mask off outside edges
    Mat mask = Mat::zeros(Size(640,480), CV_8U);
    mask(Rect(210,50,210,380)) = 255;
    Mat color_masked;
    bitwise_and(color_filtered, color_filtered.clone(), color_masked, mask);

    //get center of "blob"
    Moments m = moments(color_masked, true);
    Point p(m.m10/m.m00, m.m01/m.m00);

    circle(color, p, 5, Scalar(128,0,0), -1);

    //extract x,y,z
    float threeD_point[3] = {0};
    float pixel[2] = {p.x, p.y};
    rs2_deproject_pixel_to_point(threeD_point, &c_intrinsics, pixel, depth_frame.as<rs2::depth_frame>().get_distance((int)p.x,  (int)p.y));

    //bounding boxes
    /*int thresh = 1;
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
    }*/
    
    res.X = threeD_point[0];
    res.Y = threeD_point[1];
    res.Z = threeD_point[2];

    ROS_INFO("X: %f; Y: %f; Z: %f", res.X, res.Y, res.Z);
    ROS_INFO("X: %f; Y: %f; Z: %f", threeD_point[0], threeD_point[1], threeD_point[2]);
    

    return true;
}