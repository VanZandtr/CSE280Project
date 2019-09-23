import sys
import struct
from PIL import Image

MAP_INVALID  = 255
MAP_PATHWAY  = 0

def Map2Array(filename):
	f = open(filename, 'r')
	
	if f.readline() != 'P5\n':
		sys.stderr.write('Invalid file format')
		return
	
	data = f.readline()
	while data.startswith('#'):
		data = f.readline()
	
	# Get width and height
	size  = data.strip().split(' ')
	map_width  = int(size[0])
	map_height = int(size[1])
	
	# Read max color
	f.read(4)
	
	map_data = f.read()
	map_d = map_data[500]
	
	map_array = []
	while map_data:
		map_array.append(list(map_data[:map_width]))
		map_data = map_data[map_width:]
	
	empty_byte = ord(map_array[0][0])
	for i in range(len(map_array)):
		for j in range(len(map_array[i])):
			byte = ord(map_array[i][j])
			if byte == empty_byte:
				byte = MAP_INVALID
			else:
				byte = MAP_PATHWAY
			map_array[i][j] = byte
	return map_array

def Array2Map(converted_map, filename=None):
	f = None
	if filename:
		f = open(filename, 'w')
	else:
		f = sys.stdout
	
	f.write('P5\n')
	f.write('{} {}\n'.format(len(converted_map[0]), len(converted_map)))
	f.write('255\n')
	for row in converted_map:
		for b in row:
			f.write('{}'.format(chr(b)))

def PGM2PNG(filename):
	img = Image.open(filename)
	img = img.convert("RGBA")
	datas = img.getdata()

	newData = []
	for item in datas:
	    if item[0] == 255 and item[1] == 255 and item[2] == 255:
		newData.append((255, 255, 255, 0))
	    else:
		newData.append(item)

	img.putdata(newData)
	img.save(filename.replace('pgm', 'png'), "PNG")

def main():
	if len(sys.argv) < 2:
		sys.stdout.write('usage: {} [map] [out-file]\n'.format(sys.argv[0]))
		return
	
	converted_map = Map2Array(sys.argv[1])
	Array2Map(converted_map, sys.argv[2])

if __name__ == '__main__':
	main()
