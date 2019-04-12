# extractPitch.py

# extract the pitch of the last syllable
# according to the info in metadata.txt

import os

path = "D:/广州话语调研究/广州话标注/语气词标注/S/all"

os.mkdir(path + "/pitch/boundary")

with open(path + "/metadata.txt", 'r') as file:
	text = file.readlines()

text = [line.split('\t') for line in text]

for line in text[1:]:
	filename = line[0]
	start = float(line[4])
	end = float(line[5])
	with open(path + "/pitch/" + filename + ".Pitch", 'r') as file:
		data = file.readlines()
	data = [line.strip().split('\t') for line in data]
	data = [[float(point) for point in line] for line in data]
	newdata = []
	for i in range(len(data)):
		if data[i][0] >= start and data[i][0] <= end:
			newdata.append(data[i])
	newdata = [[str(point) for point in line] for line in newdata]
	with open(path + "/pitch/boundary/" + filename + ".pitch", 'w') as file:
		file.write('\n'.join(['\t'.join(line) for line in newdata]))

