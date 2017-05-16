import sys
import argparse
import glob
import cv2
import struct
import traceback

width, height = 24, 24

def exception_response(e):
	exc_type, exc_value, exc_traceback = sys.exc_info()
	lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
	for line in lines:
		print(line)

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', dest='input_dir')
	parser.add_argument('-o', dest='output_filename')
	parser.add_argument('--show', action='store_true', dest='show', default=False)
	args = parser.parse_args()
	return (args.input_dir, args.output_filename, args.show)
	
def writeVecHeader(outputfile, count):
    header = struct.pack('<iihh', count, width * height, 0, 0) # little endian: int, int, short, short
    outputfile.write(header)

def writeVecSample(outputfile, vec):
    header = struct.pack('<B', 0) # little endian: unsigned char
    outputfile.write(header)
    
    for col in vec:
        for i in col:
            header = struct.pack('<h', i) # short
            outputfile.write(header)
    

def createsamples(input_dir, output_vec_file, show):
    if input_dir.endswith('/'):
        input_dir = input_dir[:-1]
        
    files = glob.glob('{0}/*.*'.format(input_dir))
    count = len(files)
    
    try:
        with open(output_vec_file, 'wb') as outputfile:
            writeVecHeader(outputfile, count)
            
            for file in files:
                print file
                img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
                # h, w = img.shape[:2]
                vec = cv2.resize(img, (width, height), interpolation = cv2.INTER_CUBIC)
                writeVecSample(outputfile, vec)

                if show:
                    cv2.imshow("img", vec)
                    code = cv2.waitKey(0)
                    if (code == 27):
                        break #Esc
                    cv2.destroyAllWindows()
    except Exception as e:
        exception_response(e)


if __name__ == '__main__':
    input_dir, output_filename, show = get_args()
    if not input_dir:
        sys.exit('requires a directory of input files. (-v input_dir)')
    if not output_filename:
        sys.exit('requires an output filename. (-o output_filename)')
    
    print("{0} -> {1}".format(input_dir, output_filename))
    createsamples(input_dir, output_filename, show);


