# toPitch.py

# convert a PitchTier file into a Pitch file in the format:
# time	f0
import os

path = "D:/广州话语调研究/广州话标注/语气词标注/S/all"
files = os.listdir(path)
os.mkdir(path + '/pitch')
for filename in files:
	if filename.endswith("PitchTier"):
		with open(path + '/' + filename, 'r') as file:
			text = file.readlines()

		newName = filename[:-4]
		data = []

		index = []

		for line in text:
			if line.startswith("points ["):
				index.append(text.index(line))

		for i in index:
			time = text[i + 1][13:].strip()
			f0 = text[i + 2][12:].strip()
			data.append([time, f0])

		with open(path + '/pitch/' + newName, 'w') as file:
			file.write('\n'.join(['\t'.join(datapoint) for datapoint in data]))
