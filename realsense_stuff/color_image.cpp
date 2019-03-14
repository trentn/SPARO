// include the librealsense C++ header file
#include <librealsense2/rs.hpp>

// include OpenCV header file
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;


const int max_value_H = 360/2;
const int max_value = 255;
const String window_capture_name = "Video Capture";
const String window_detection_name = "Object Detection";
int low_H = 0, low_S = 0, low_V = 0;
int high_H = max_value_H, high_S = max_value, high_V = max_value;
static void on_low_H_thresh_trackbar(int, void *)
{
    low_H = min(high_H-1, low_H);
    setTrackbarPos("Low H", window_detection_name, low_H);
}
static void on_high_H_thresh_trackbar(int, void *)
{
    high_H = max(high_H, low_H+1);
    setTrackbarPos("High H", window_detection_name, high_H);
}
static void on_low_S_thresh_trackbar(int, void *)
{
    low_S = min(high_S-1, low_S);
    setTrackbarPos("Low S", window_detection_name, low_S);
}
static void on_high_S_thresh_trackbar(int, void *)
{
    high_S = max(high_S, low_S+1);
    setTrackbarPos("High S", window_detection_name, high_S);
}
static void on_low_V_thresh_trackbar(int, void *)
{
    low_V = min(high_V-1, low_V);
    setTrackbarPos("Low V", window_detection_name, low_V);
}
static void on_high_V_thresh_trackbar(int, void *)
{
    high_V = max(high_V, low_V+1);
    setTrackbarPos("High V", window_detection_name, high_V);
}




int main()
{   
    namedWindow(window_capture_name, WINDOW_AUTOSIZE);
    namedWindow(window_detection_name, WINDOW_AUTOSIZE);

    createTrackbar("Low H", window_detection_name, &low_H, max_value_H, on_low_H_thresh_trackbar);
    createTrackbar("High H", window_detection_name, &high_H, max_value_H, on_high_H_thresh_trackbar);
    createTrackbar("Low S", window_detection_name, &low_S, max_value, on_low_S_thresh_trackbar);
    createTrackbar("High S", window_detection_name, &high_S, max_value, on_high_S_thresh_trackbar);
    createTrackbar("Low V", window_detection_name, &low_V, max_value, on_low_V_thresh_trackbar);
    createTrackbar("High V", window_detection_name, &high_V, max_value, on_high_V_thresh_trackbar);

    rs2::pipeline pipe;
    rs2::config cfg;
    
    cfg.enable_stream(RS2_STREAM_COLOR, 640, 480, RS2_FORMAT_BGR8, 30);
    
    pipe.start(cfg);

    // Camera warmup - dropping several first frames to let auto-exposure stabilize
    rs2::frameset frames;
    for(int i = 0; i < 30; i++)
    {
        frames = pipe.wait_for_frames();
    }
    

    rs2::frame color_frame;
    Mat color_HSV, color_filtered;
    while(true) {
        frames = pipe.wait_for_frames();
        color_frame = frames.get_color_frame();
        Mat color(Size(640, 480), CV_8UC3, (void*)color_frame.get_data(), Mat::AUTO_STEP);
        
        cvtColor(color, color_HSV, COLOR_BGR2HSV);
        inRange(color_HSV, Scalar(low_H, low_S, low_V), Scalar(high_H, high_S, high_V), color_filtered);

        imshow(window_capture_name, color);
        imshow(window_detection_name, color_filtered);

        char key = (char) waitKey(30);
        if (key == 'q' || key == 27)
        {
            break;
        }
    }
    return 0;
}
