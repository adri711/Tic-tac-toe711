import numpy as np
import csv

features = np.array([0,0,0, 0,0,0, 0,0,0])
labels = np.array([0,0])
with open("dataset/features.csv") as features_file:
	csv_reader = csv.reader(features_file)
	for row in csv_reader:
		row = np.array(row)
		features  = np.vstack((features, row))
with open("dataset/labels.csv") as labels_file:
	csv_reader = csv.reader(labels_file)
	for row in csv_reader:
		row = np.array(row)
		labels  = np.vstack((labels, row))
features = features.astype(np.int)
labels = labels.astype(np.int)

def load():
	return features, labels
