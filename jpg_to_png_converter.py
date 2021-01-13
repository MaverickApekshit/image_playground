import sys
import os
from PIL import Image

#get first and second argument
original_file_location = sys.argv[1]
new_file_location = sys.argv[2]

#check if new folder esits, if not create it
if not os.path.exists(new_file_location):
	os.makedirs(new_file_location)

#get all the original files
original_files = os.listdir(original_file_location)

#convert each file to png and save
for original_file in original_files:
	img  = Image.open(f'{original_file_location}{original_file}')
	clean_name = os.path.splitext(original_file)[0]
	img.save(f'{new_file_location}{clean_name}.png', 'PNG')
