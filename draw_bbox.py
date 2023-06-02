import cv2
import json

def get_text_data(filename):
    # Opening JSON file
    with open("static/" + filename, 'r') as openfile:
        json_object = json.load(openfile)
    segment_result_test = json_object['annotationResults'][0]['textAnnotations'][0]
    segment_result = json_object['annotationResults'][0]['textAnnotations']
    all_text_data = []
    for result in segment_result:
        label = result['text']
        time = result['segments'][0]['segment']
        confidence = result['segments'][0]['confidence']
        data = dict(time)
        data['labels'] = label
        data['confidence'] = confidence
        all_text_data.append(data)
    return all_text_data

def get_logo_json(filename):
    with open(filename, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    logo_result = json_object['annotationResults'][0]['logoRecognitionAnnotations']
    all_logos_data = []
    for result in logo_result:
        label = result['entity']['description']
        time = result['tracks'][0]['segment']
        confidence = result['tracks'][0]['confidence']
        time_stamps = result['tracks'][0]['timestampedObjects']
        data = dict(time)
        data['labels'] = label
        data['confidence'] = confidence
        data['timestampedObjects'] = time_stamps
        all_logos_data.append(data)
    return all_logos_data

def read_json(video, json_path):
    fps = float(video.get(cv2.CAP_PROP_FPS))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps_detail = [[] for _ in range(total_frames)]
    brands = get_logo_json(json_path)
    for brand in brands:
        brand_name = brand['labels']
        for time in brand['timestampedObjects']:
            frame_no = int(float(time['timeOffset'][:-1]) * fps)
            bbox = time['normalizedBoundingBox']
            info = {brand_name: bbox}
            fps_detail[frame_no].append(info)
    return fps_detail

if __name__ == "__main__":
    video_path = 'videos/video1.mp4'
    json_path = 'response.json'
    output_path = 'output_video.mp4'
    video = cv2.VideoCapture(video_path)
    frame_wise_info=read_json(video, 'response.json')
    # print(frame_wise_info)
    # Get video properties
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    # Create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, int(fps), (frame_width, frame_height))

    # print(frame_wise_info[0])


    for frame_number in range(total_frames):
        _, frame = video.read()
        # print(frame_wise_info[frame_number])
        for brand_bbox in frame_wise_info[frame_number]:
            if brand_bbox:
                key = list(brand_bbox.keys())[0]
                print(key)
                print(len(brand_bbox[key]))
                if (len(brand_bbox[key])) ==4:
                    left = int(brand_bbox[key]['left'] * frame_width)
                    top = int(brand_bbox[key]['top'] * frame_height)
                    right = int(brand_bbox[key]['right'] * frame_width)
                    bottom = int(brand_bbox[key]['bottom'] * frame_height)

                    print('Coordinates', left, top, right, bottom)
                    #
                    # Draw the bounding box on the frame
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.imshow('Result', frame)
                    # cv2.waitKey(0)

                # Write the modified frame to the output video
            output_video.write(frame)
# # Release the video and output video file
video.release()
output_video.release()

