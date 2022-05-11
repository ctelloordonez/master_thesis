from os.path import join as pjoin
import numpy as np
import os

def read_file(path):
    import csv
    with open(path) as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
    return d


def ASCII_to_dict():
    root = 'data/ASCII_files/Participant1/Processed_Data'
    participant = {}
    for velocity in os.listdir(root):
        participant[velocity] = {}
        velocity_dir = pjoin(root, velocity)
        for leg in os.listdir(velocity_dir):
            participant[velocity][leg] = {}
            leg_dir = pjoin(velocity_dir, leg)
            for feature in os.listdir(leg_dir):
                if feature == 'Properties':
                    break
                participant[velocity][leg][feature] = {}
                feature_dir = pjoin(leg_dir, feature)
                for file in os.listdir(feature_dir):
                    trial = file.replace('.txt', '')
                    participant[velocity][leg][feature][trial] = {}
                    data = read_file(pjoin(feature_dir, file))
                    data = np.array(data)
                    data = data.transpose()
                    for i in data:
                        x = i[1:]
                        x = x.astype(float)
                        participant[velocity][leg][feature][trial][i[0]] = x

    return participant

