#!/usr/bin/env python

import os

file_path = 'wine.data'

if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')

file = open('wine.data')

corrected_file = []
for line in file.readlines():
    clean_line = line.replace('  ', ' ').replace('  ', ' ').strip()
    line_values = clean_line.split(',')
    corrected_line = []
    for value in line_values:
        try:
            corrected_line.append(int(value))
        except:
            corrected_line.append(float(value))
    corrected_file.append(corrected_line)

corrected_file=corrected_file[0:178]


transposed_list=[]
for column in corrected_file[0]:
    transposed_list.append([])

for line in corrected_file:
    for idx, column in enumerate(line):
        transposed_list[idx].append(column)

import numpy as np

arr = np.array(corrected_file)

print('mean of each feature: ',np.mean(arr,axis=0))
print('Standard deveation of each feature: ', np.std(arr,axis=0))

#print(transposed_list)
