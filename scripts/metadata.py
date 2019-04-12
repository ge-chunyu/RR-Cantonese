# metadata.py

# get the metadata of the files
# filename, speaker, gender, tone, 
# start(start time of the last rhyme), end(end time of the last rhyme)

import os

path = "D:/广州话语调研究/广州话标注/语气词标注/S/all"

files = os.listdir(path)

metadata = []
metadata.append('\t'.join(['filename', 'speaker', 'gender', 'tone', 'start', 'end', 'rhyme']))
for filename in files:
	if filename.endswith("TextGrid"):
		with open(path + '/' + filename, 'r') as file:
			text = file.readlines()

		speaker = filename[:2]
		gender = filename[:1]
		tone = filename[6]
		start = text[-7][19:].strip()
		end = text[-6][19:].strip()
		rhyme = text[-5][19:].strip().strip('"')
		metadata.append('\t'.join([filename[:-9], speaker, gender, tone, start, end, rhyme]))

with open(path + '/' + 'metadata.txt', 'w') as file:
	file.write('\n'.join(metadata))