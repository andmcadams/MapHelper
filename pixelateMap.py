#!/usr/bin/python
from gimpfu import *
import struct

def python_pixelate_map(img, layer, squareSize):
	# get the correct image

	terrainLayerGroup = None
	for l in img.layers:
		if l.name == "Terrain GroupLayer":
			terrainLayerGroup = l
			break

	if terrainLayerGroup == None:
		#throw some error
		exit(0)

	terrainLayer = None
	for l in terrainLayerGroup.layers:
		if l.name == "Terrain Smooth":
			terrainLayer = l
			break

	if terrainLayer == None:
		#throw some error
		exit(0)

	# Copy the smooth terrain layer
	pixelLayer = pdb.gimp_layer_copy(terrainLayer, True)
	pixelLayer.name = "Terrain Pixelated"
	img.insert_layer(pixelLayer, terrainLayerGroup, 1)

	# Go through each 3x3 block or 4x4 block
	def setBlockAverage(x, y, squareSize, region, h, w):
		colors = ''
		# Get colors of the nxn square
		endX = False
		endY = False
		if x+squareSize < w and y+squareSize < h:
			colors = region[x:x+squareSize,y:y+squareSize]
		elif x+squareSize < w:
			colors = region[x:x+squareSize,y:]
			endY = True
		elif y+squareSize < h:
			colors = region[x:, y:y+squareSize]
			endX = True
		else:
			colors = region[x:,y:]
			endX = True
			endY = True


		avgRed = 0
		avgBlue = 0
		avgGreen = 0
		# colors is of the form "{0xRR0xGG0xBB0xAA}*"
		colorCount = 0
		for i in range(0, len(colors), 4):
			r = colors[i]
			g = colors[i+1]
			b = colors[i+2]
			a = colors[i+3]
			aVal = struct.unpack("<B", a)[0]
			if aVal == 0:
				continue
			else:
				avgRed += struct.unpack("<B", r)[0]
				avgGreen += struct.unpack("<B", g)[0]
				avgBlue += struct.unpack("<B", b)[0]
				colorCount += 1

		# This is Python2 so / should do int div if both are ints
		if colorCount != 0:
			avgRed /= colorCount
			avgGreen /= colorCount
			avgBlue /= colorCount

		# Always set alpha to max
		colorString = struct.pack("<B", avgRed) + struct.pack("<B", avgGreen) + struct.pack("<B", avgBlue) + struct.pack("<B", 255)
		colorString *= len(colors)/len(colorString)
		
		if not endX and not endY:
			region[x:x+squareSize,y:y+squareSize] = colorString
		elif not endX:
			region[x:x+squareSize,y:] = colorString
		elif not endY:
			region[x:,y:y+squareSize] = colorString
		else:
			region[x:,y:] = colorString


	# This is an undocumented function I found on some gimpchat forum
	region = pixelLayer.get_pixel_rgn(0, 0, pixelLayer.width, pixelLayer.height, True)
	height = pixelLayer.height
	width = pixelLayer.width
	for i in range(0, height, squareSize):
		for j in range(0, width, squareSize):
			blockColor = setBlockAverage(j, i, squareSize, region, height, width)

	gimp.displays_flush()

register(
        "python_pixelate_map",
        "Pixelate a smooth map",
        "Pixelate a smooth map",
        "Andrew McAdams",
        "Andrew McAdams",
        "2020",
        "<Image>/Filters/Map/Pixelate map...",
        "",
        [ 
                (PF_RADIO, "squareSize", "Pixels per tile", 3, (("3", 3), ("4", 4))),
        ],
        [],
        python_pixelate_map)

main()




