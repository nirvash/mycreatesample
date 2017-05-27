import sys
import glob
import struct
import argparse
import traceback
import random

def exception_response(e):
	exc_type, exc_value, exc_traceback = sys.exc_info()
	lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
	for line in lines:
		print(line)

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', dest='input_filename')
	parser.add_argument('-o', dest='output_filename')
	args = parser.parse_args()
	return (args.input_filename, args.output_filename)

def readVecSample(data, i, image_size):
    body = data[i * (image_size * 2 + 1) + 1 :]
    vec = body[:image_size * 2]
    return vec
    

def writeVecSample(outputfile, vec):
    header = struct.pack('<B', 0) # little endian: unsigned char
    outputfile.write(header)
    for i in range(0,len(vec),2):
        val = struct.unpack('<h', vec[i:i+2])
        outval = struct.pack('<h', val[0]) # short
        outputfile.write(outval)
    # outputfile.write(vec)

def shuffle_vec_file(input_vec_file, output_vec_file):
	# Get the total number of images
	total_num_images = 0
	try:
		with open(input_vec_file, 'rb') as vecfile:	
			content = ''.join(str(line) for line in vecfile.readlines())
			val = struct.unpack('<iihh', content[:12])
			total_num_images = val[0]
			image_size = val[1]
	except IOError as e:
		print('An IO error occured while processing the file: {0}'.format(f))
		exception_response(e)

	print('Shuffle {0} -> {1}, num {2}'.format(input_vec_file, output_vec_file, total_num_images))

	header = struct.pack('<iihh', total_num_images, image_size, 0, 0)
	try:
		with open(output_vec_file, 'wb') as outputfile:
			outputfile.write(header)
			data = content[12:]
			list = range(0, total_num_images)
			random.shuffle(list)
			for i in list:
			    vec = readVecSample(data, i, image_size)
			    writeVecSample(outputfile, vec)
			
	except Exception as e:
		exception_response(e)


if __name__ == '__main__':
	input_filename, output_filename = get_args()
	if not input_filename:
		sys.exit('requires an input filename.')
	if not output_filename:
		sys.exit('requires an output filename.')

	shuffle_vec_file(input_filename, output_filename)

