import numpy as np
import csv

features_file_loc =  "dataset/features.csv"
labels_file_loc = "dataset/labels.csv"
def load_file(file_loc, np_arr):
	with open(file_loc) as file_csv:
		csv_reader = csv.reader(file_csv)
		for row in csv_reader:
			row = np.array(row)
			np_arr = np.vstack((np_arr, row))
	np_arr = np_arr.astype(np.int)
	return np_arr

def insert_into_file(file_loc, arr):
	with open(file_loc, 'a', newline="\n") as file_csv:
		csv_writer = csv.writer(file_csv)
		csv_writer.writerow(arr)


features = load_file(features_file_loc, np.array([0,0,0, 0,0,0, 0,0,0]))
labels = load_file(labels_file_loc, np.array([0,0]))

def load():
	return features, labels

def insert_into_dataset(new_feature, new_label):
	global features_file_loc, labels_file_loc
	
	insert_into_file(features_file_loc, new_feature)
	insert_into_file(labels_file_loc, new_label)