# Picohash
# A python program that converts images into ASCII graphics

import os
from PIL import Image

imageList = [i for i in os.listdir('.') if i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg')]
imageList.sort()

#mapping
pixelMap = { 'E1':' ', 'C5':'.', 'A9':',', '8C':"-", '70':"'", '56':':', '3B':';', '22':'+', '00':'#'}


def modification(imagefile):
	text = open(imagefile.split('.')[0]+'.html', 'w')
	text.write('<!DOCTYPE html><html><head><title>'+imagefile+'</title><style>body {font-size: 3px;}</style></head><body><pre>')
	
	image = Image.open(imagefile).convert('L').rotate(90, expand=True)
	print 'processing ' + imagefile
	rgbim = image.convert('RGB')
	w, h = rgbim.size

	for i in xrange(w):
		imageString = ""
		for j in xrange(h):
			px = rgbim.getpixel((i, j))
			for sym in ['E1', 'C5', 'A9', '8C', '70', '56', '3B', '22', '00']:
				symVal = int(sym, 16)
				if(px >= (symVal, symVal, symVal)):
					imageString += pixelMap[sym]
					break
		text.write(imageString[::-1] + '\n')
			
	text.write('</pre></body></html>')
	print 'Saved ' + imagefile + '.html'
			
	text.close()
	image.close()
	rgbim.close()

for imagefile in imageList:
	print 'Do you want to process ' + imagefile + '? [y/n]'
	inp = raw_input()
	if inp=='y' or inp=='Y':
		modification(imagefile)
	else:
		continue
