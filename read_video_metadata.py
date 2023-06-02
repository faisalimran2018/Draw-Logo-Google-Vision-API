import json

def get_labeled_json(filename):
	with open("static/"+filename, 'r') as openfile:
		# Reading from json file
		json_object = json.load(openfile)

	segment_result =  json_object['annotationResults'][0]['segmentLabelAnnotations']
	segment_result_shot =  json_object['annotationResults'][0]['shotLabelAnnotations']

	all_labels_data = []

	for result in segment_result:
		label = result['entity']['description']
		time = result['segments'][0]['segment']
		confidence = result['segments'][0]['confidence']
		data = dict(time)
		data['labels'] = label
		data['confidence'] = confidence
		all_labels_data.append(data)

	for result in segment_result_shot:
		label = result['entity']['description']
		time = result['segments'][0]['segment']
		confidence = result['segments'][0]['confidence']

		data = dict(time)
		data['labels'] = label
		data['confidence'] = confidence
		all_labels_data.append(data)

	return all_labels_data

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
		data = dict(time)
		data['labels'] = label
		data['confidence'] = confidence
		# print(data)
		all_logos_data.append(data)
	return all_logos_data

def get_text_data(filename):
	# Opening JSON file
	with open("static/"+filename, 'r') as openfile:
		json_object = json.load(openfile)
	segment_result_test = json_object['annotationResults'][0]['textAnnotations'][0]
	segment_result = json_object['annotationResults'][0]['textAnnotations']
	all_text_data = []
	for result in segment_result:
		# print(result)
		label = result['text']
		time = result['segments'][0]['segment']
		confidence = result['segments'][0]['confidence']
		data = dict(time)
		data['labels'] = label
		data['confidence'] = confidence
		# print(data)
		all_text_data.append(data)
	return all_text_data

#
# print(all_labels_data)
# print(len(all_labels_data))
#
# data = all_labels_data
# print("Total Data with Time: ",len(all_labels_data))
# fps = 25
#
# # Calculate the frame numbers corresponding to the annotations
# annotations = []
# for annotation in data:
#     start_time = annotation['startTimeOffset'].rstrip('s')
#     end_time = annotation['endTimeOffset'].rstrip('s')
#     start_frame = int(float(start_time) * fps)
#     end_frame = int(float(end_time) * fps)
#     annotations.append({
#         'label': annotation['labels'],
#         'confidence': annotation['confidence'],
#         'start_frame': start_frame,
#         'end_frame': end_frame
#     })
#
#
# frames = []
# for i in range(end_frame + 1):
#     frame_annotations = [a for a in annotations if a['start_frame'] <= i <= a['end_frame']]
#     frames.append({
#         'frame_number': i,
#         'annotations': frame_annotations
#     })
# print(len(frames))
#
#
# for frame in frames:
# 	print(frame)
# 	print(len(frame['annotations']))
