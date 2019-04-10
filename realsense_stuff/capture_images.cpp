// include the librealsense C++ header file
#include <librealsense2/rs.hpp>
#include <librealsense2/rsutil.h>

// include OpenCV header file
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

void detect_target();
int main(int argc, char** argv) {
    char* tag = argv[1];
    int count = atoi(argv[2]);
    
    char* window_name = "Capture";

    namedWindow(window_name, WINDOW_AUTOSIZE);


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
    int i = 0;
    while(true) {
        frames = pipe.wait_for_frames();
        rs2::align align = rs2::align(RS2_STREAM_COLOR);
        auto aligned_frames = align.process(frames);

        rs2::frame color_frame, depth_frame;
        Mat color_HSV, color_filtered;

        color_frame = aligned_frames.get_color_frame();
        
        

        //filter on color
        Mat color(Size(640, 480), CV_8UC3, (void*)color_frame.get_data(), Mat::AUTO_STEP);

        imshow(window_name, color);

        char imageName[100];
        sprintf(imageName, "./images/color%s%d.jpg", tag, i);
        imwrite(imageName, color);

        char key = (char) waitKey(30);
        if (key == 'q' || key == 27)
        {
            break;
        }

        i++;
    }

    return 0;
}