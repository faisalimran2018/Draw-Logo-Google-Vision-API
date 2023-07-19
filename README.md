## Drawing Logos and Text on video from response of Vision API

This repository contains a Python script for object detection and annotation in video using data extracted from a JSON file. The script can perform text and logo detection on a video and then generate a new video with annotations.

How to Use
To use this script, simply adjust the variables under the if __name__ == "__main__": block to match the paths of your files:

video_path: Path to the input video.
json_path: Path to the input JSON file.
output_path: Path where the output video will be saved.
type_of_detection: Specify the type of detection ('logo' or 'text').
Then run the script in your terminal:

sh
Copy code
python video_processing.py
Requirements
Before running the script, make sure you have the following Python libraries installed in your Python environment:

OpenCV
tqdm
numpy
json
You can install these using pip:

sh
Copy code
pip install opencv-python tqdm numpy
Code Description
The script mainly consists of three functions:

get_text_data(filename): Extracts text annotations from a JSON file.
get_logo_data(filename): Extracts logo annotations from a JSON file.
get_fps_detail(video, json_path, type): Extracts frame per second (FPS) detail from a JSON file.
And a main section that reads the video, processes the frames according to the logo or text data, draws the annotations on the frames and writes them into a new video.

Please ensure the compatibility of the input video format with your OpenCV version.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
Thanks to OpenCV and its contributors for providing such a powerful library.
Thanks to the open-source community for their continuous support.
Disclaimer
This script is intended to be used for learning purposes. The author is not responsible for its use in any illicit activities or for any damages it might cause.

 Drawing bounding boxes on video using Google Vision API, Remember, Google doesn't return result in form of a json file, you will have to save it in json format using code below.

    result = operation.result(timeout=90)

    MessageToDict(result._pb)

* Install requirements using "pip install -r requirement.txt".
* Give path of json and source video in the code, better to make seprate folders and palce files.
* At the moment the code only supports text and logo so select logo or text in the code.

![img.png](img.png)

* run the file draw_bbox.py using "python draw_bbox.py"

### Source Image
![img_1.png](img_1.png)

### Result Image Logo
![img_2.png](img_2.png)
