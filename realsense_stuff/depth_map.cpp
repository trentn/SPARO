// include the librealsense C++ header file
#include <librealsense2/rs.hpp>

// include OpenCV header file
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {   
    rs2::colorizer color_map;
    rs2::pipeline pipe;
    rs2::config cfg;
    
    cfg.enable_stream(RS2_STREAM_DEPTH, 640, 480);
    cfg.enable_stream(RS2_STREAM_COLOR, 640, 480, RS2_FORMAT_BGR8, 30);
    
    pipe.start(cfg);

    // Camera warmup - dropping several first frames to let auto-exposure stabilize
    rs2::frameset frames;
    for(int i = 0; i < 30; i++)
    {
        frames = pipe.wait_for_frames();
    }
    rs2::align align = rs2::align(RS2_STREAM_COLOR);
    auto aligned_frames = align.process(frames);

    rs2::frame color_frame, depth_frame;
    Mat color_HSV, color_filtered;

    color_frame = aligned_frames.get_color_frame();
    depth_frame = aligned_frames.get_depth_frame().apply_filter(color_map);
    
    Mat color(Size(640, 480), CV_8UC3, (void*)color_frame.get_data(), Mat::AUTO_STEP);
    Mat depth(Size(640, 480), CV_8UC3, (void*)depth_frame.get_data(), Mat::AUTO_STEP);

    cvtColor(color, color_HSV, COLOR_BGR2HSV);
    inRange(color_HSV, Scalar(70, 150, 77), Scalar(130, 255, 255), color_filtered);

    Mat depth_filtered;
    bitwise_and(depth, depth.clone(), depth_filtered, color_filtered);

    imshow("Color Image", color);
    imshow("Color Mask", color_filtered);
    imshow("Depth Map", depth);
    imshow("Filtered Depth", depth_filtered);
    
    waitKey(0);

    return 0;
}
