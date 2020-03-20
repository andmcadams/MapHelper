#!/usr/bin/python
from gimpfu import *

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
	def getBlockAverage(x, y, squareSize, layer):
		colors = []
		for i in range(0,squareSize):
			for j in range(0, squareSize):
				if x+j < layer.width and y+i < layer.height:
					c = layer.get_pixel(x+j, y+i)
					# If the alpha channel is not 0, push it in to be counted
					if c[3] != 0:
						colors.append(c)

		if len(colors) == 0:
			return (0, 0, 0, 0)

		avgRed = 0
		avgBlue = 0
		avgGreen = 0
		for color in colors:
			avgRed += color[0]
			avgGreen += color[1]
			avgBlue += color[2]
		avgRed = int(avgRed/len(colors))
		avgGreen = int(avgGreen/len(colors))
		avgBlue = int(avgBlue/len(colors))

		# Always set alpha to max
		return (avgRed, avgGreen, avgBlue, 0xFF)



	for i in range(0, img.height, squareSize):
		for j in range(0, img.width, squareSize):
			blockColor = getBlockAverage(j, i, squareSize, pixelLayer)
			for w in range(0, squareSize):
				for z in range(0, squareSize):
					if j+z < layer.width and i+w < layer.height:
						pixelLayer.set_pixel(j+z, i+w, blockColor)

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




