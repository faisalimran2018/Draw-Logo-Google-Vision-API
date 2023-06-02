import cv2
import json


def draw_bounding_boxes(video_path, json_path, output_path):
    # Read the video
    video = cv2.VideoCapture(video_path)

    # Get video properties
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Load the JSON response from the Google Cloud Vision API
    with open(json_path) as json_file:
        data = json.load(json_file)

    # Iterate over each frame
    for frame_number in range(total_frames):
        _, frame = video.read()

        # Get the frame's timestamp in seconds
        timestamp = frame_number / fps

        # Check if the timestamp exists in the JSON response
        if 'annotationResults' in data:
            print('annotationResults')
            annotation_results = data['annotationResults']
            # print('annotation results',annotation_results)

            for annotation in annotation_results:
                if 'segment' in annotation:
                    print('segments')
                    segments = annotation['segment']
                    print(segments)
                    # for segment in segments:
                    start_time = float(segments['startTimeOffset'][:-1])  # Remove 's' from the timestamp
                    end_time = float(segments['endTimeOffset'][:-1])  # Remove 's' from the timestamp

                    # Check if the frame's timestamp falls within the segment's time range
                    if start_time <= timestamp <= end_time:
                        print('frames timestamp falls within the segments time range')
                        if 'logoRecognitionAnnotations' in annotation:
                            print('logoRecognitionAnnotations')
                            logo_annotations = annotation['logoRecognitionAnnotations']

                            for logo_annotation in logo_annotations:
                                entity = logo_annotation['entity']
                                description = entity['description']
                                tracks = logo_annotation['tracks']

                                for track in tracks:
                                    if 'timestampedObjects' in track:
                                        print('timestampedObjects')
                                        timestamped_objects = track['timestampedObjects']

                                        for timestamped_object in timestamped_objects:
                                            time_offset = float(
                                                timestamped_object['timeOffset'][:-1])  # Remove 's' from the timestamp

                                            # Check if the frame's timestamp is within the bounding box's time range
                                            if start_time <= time_offset <= end_time:
                                                normalized_bounding_box = timestamped_object['normalizedBoundingBox']
                                                left = int(normalized_bounding_box['left'] * frame_width)
                                                top = int(normalized_bounding_box['top'] * frame_height)
                                                right = int(normalized_bounding_box['right'] * frame_width)
                                                bottom = int(normalized_bounding_box['bottom'] * frame_height)

                                            print('Coordinates', left, top, right, bottom)

                                            # Draw the bounding box on the frame
                                            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                                            cv2.imshow('Result',frame)
                                            cv2.waitKey(0)

    # Write the modified frame to the output video
    output_video.write(frame)

    # Release the video and output video file
    video.release()
    output_video.release()

    print("Bounding boxes drawn successfully. Output video saved at:", output_path)

    # Example usage
video_path = 'videos/video1.mp4'
json_path = 'response.json'
output_path = 'output_video.mp4'


draw_bounding_boxes(video_path, json_path, output_path)
