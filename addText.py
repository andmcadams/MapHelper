#!/usr/bin/python
from gimpfu import *
import letterprinter

landmarkDict = {
	"arr": letterprinter.LETTER_ARR_LANDMARK,
	"height": 13
}

cityDict = {
	"arr": letterprinter.LETTER_ARR_CITY,
	"height": 18
}

kingdomDict = {
	"arr": letterprinter.LETTER_ARR_KINGDOM,
	"height": 24
}

textTypeDict = [landmarkDict, cityDict, kingdomDict]

# Given two bytearrays, bitwise or each part, then return.
# This has to be done since j and f overlap with other characters in the kingdom label.
def bit_or(arr1, arr2):
	result = ''
	if len(arr1) != len(arr2):
		exit(1)
	for i in range(len(arr1)):
		result += chr(arr1[i] | arr2[i])
	return result


def python_add_text(img, layer, text, textType):

	textLayerGroup = None
	for l in img.layers:
		if l.name == "Text Group":
			textLayerGroup = l
			break

	if textLayerGroup == None:
		#throw some error
		exit(0)

	l = pdb.gimp_layer_new(img, img.width, img.height, 1, '{} Text Layer'.format(text), 100, 0)
	l.visible = False
	img.insert_layer(l, textLayerGroup, 0)

	region = l.get_pixel_rgn(0, 0, l.width, l.height, True)
	totalOffset = 0

	d = textTypeDict[textType]

	for c in text:
		(offset, data) = d['arr'][c]()
		if data != None:

			# Note that all text js goes below the char in front. They are treated as a special case here.
			if c == 'j':
				totalOffset -= 1

			region[totalOffset:totalOffset+offset,:d['height']] = bit_or(bytearray(region[totalOffset:totalOffset+offset,:d['height']]), bytearray(data))

			# Note that city and kingdom text fs goes above the char after it. They are treated as a special case here.
			if c == 'f' and (textType == 1 or textType == 2):
				offset -= 1

		totalOffset += offset

	l.visible = True

	# Add drop shadow
	#color black
	#blend mode normal
	#op 100
	#angle 135
	#distance 1.0
	#spread 100
	#size 0
	#contour linear
	#noise 0
	#Layer knocks out drop shadow (True)
	#Merge layers (False) The layerfx lib does not seem to handle layergroups very well, so I will manually merge the layers.
	pdb.python_layerfx_drop_shadow(img, l, (0, 0, 0), 100, 0, 0, 0, 100, 0, 135, 1, True, False)

	# Merge the shadow layer with the text layer
	shadowLayerCopy = pdb.gimp_layer_copy(img.layers[0], True)
	pdb.gimp_image_remove_layer(img, img.layers[0])
	img.insert_layer(shadowLayerCopy, textLayerGroup, 0)
	img.merge_down(shadowLayerCopy, 1)



register(
        "python_add_text",
        "Add a label to the map",
        "Add a label to the map",
        "Andrew McAdams",
        "Andrew McAdams",
        "2020",
        "<Image>/Filters/Map/Add text",
        "",
        [
            (PF_STRING, "text", "Label text", None),
            (PF_RADIO, "squareSize", "Label type", 0, (("Landmark", 0), ("City", 1), ("Kingdom", 2))),
        ],
        [],
        python_add_text)

main()
