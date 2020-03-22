#!/usr/bin/python
from gimpfu import *

def python_make_map(width, height, squareSize, background):
	# Create a new image
	img = gimp.Image(width, height, 0)
	gimp.Display(img)

	# Create layers

	# This should be 64*{3,4} depending on which size you are doing. I assume 3 for now
	BLOCKSIZE = 64*squareSize
	OPAQUE = 100
	TRANSLUCENT = 50
	# add_layer(layer, 0) adds the layer to the top of the layer stack

	l = pdb.gimp_layer_new(img, width, height, 0, "Background", OPAQUE, 0)
	img.add_layer(l, 0)


	# Background colors
	# Ocean blue: 0x6277A6
	# Missing map/Cave black: 0x000000

	# Color in the background
	pdb.gimp_selection_all(img)
	if background == 0:
		pdb.gimp_context_set_foreground((0x62, 0x77, 0xA6, 0xFF))
	else:
		pdb.gimp_context_set_foreground((0x00, 0x00, 0x00, 0xFF))

	pdb.gimp_edit_bucket_fill(img.layers[-1], 0, 0, 100, 0.0, 0, 0.0, 0.0)


	l = pdb.gimp_layer_new(img, width, height, 1, "Landmass", OPAQUE, 0)
	l.visible = False
	img.add_layer(l, 0)

	lg = gimp.GroupLayer(img, "Terrain GroupLayer")
	pdb.gimp_image_insert_layer(img, lg, None, 0)

	l = pdb.gimp_layer_new(img, width, height, 1, "Terrain Smooth", OPAQUE, 0)
	l.visible = False
	img.insert_layer(l, lg, 0)

	l = pdb.gimp_layer_new(img, width, height, 1, "Block Coloring", OPAQUE, 0)
	l.visible = False
	img.insert_layer(l, lg, 0)

	l = pdb.gimp_layer_new(img, width, height, 1, "Paths", OPAQUE, 0)
	l.visible = False
	img.add_layer(l, 0)

	l = pdb.gimp_layer_new(img, width, height, 1, "Buildings", OPAQUE, 0)
	l.visible = False
	img.add_layer(l, 0)

	lg = gimp.GroupLayer(img, "Objects Group")
	pdb.gimp_image_insert_layer(img, lg, None, 0)

	l = pdb.gimp_layer_new(img, width, height, 1, "Objects", OPAQUE, 0)
	l.visible = False
	img.insert_layer(l, lg, 0)

	l = pdb.gimp_layer_new(img, width, height, 1, "Icons", OPAQUE, 0)
	l.visible = False
	img.add_layer(l, 0)

	lg = gimp.GroupLayer(img, "Text Group")
	pdb.gimp_image_insert_layer(img, lg, None, 0)

	# pdb.plug_in_grid doesn't actually seem to create gridlines sadly. Maybe I'm just calling it wrong?
	# pdb.plug_in_grid(img, img.layers[-1], 0, 10, 0, (0x00, 0x00, 0x00, 0xFF), 255, 0, 10, 0, (0xFF, 0x00, 0x00, 0xFF), 255, 0, 0, 0, (0xFF, 0x00, 0x00, 0xFF), 255)

	l = pdb.gimp_layer_new(img, width, height, 1, "Gridlines", TRANSLUCENT, 0)
	img.add_layer(l, 0)
	# Draw the gridlines
	l = img.layers[0]
	for i in range(10, height, BLOCKSIZE):
		for j in range(width):
			pdb.gimp_drawable_set_pixel(l, i, j, 4, [0xFF, 0xFF, 0xFF, 0xFF])

	for i in range(10, width, BLOCKSIZE):
		for j in range(height):
			pdb.gimp_drawable_set_pixel(l, j, i, 4, [0xFF, 0xFF, 0xFF, 0xFF])

register(
        "python_setup_map",
        "Set up the layers for making a map",
        "Set up the layers for making a map",
        "Andrew McAdams",
        "Andrew McAdams",
        "2020",
        "<Toolbox>/File/Create/Patterns/Map...",
        "",
        [
                (PF_INT, "width", "Width of the map", None),
                (PF_INT, "height", "Height of the map", None),
                (PF_RADIO, "squareSize", "Pixels per tile", 3, (("3", 3), ("4", 4))),
                (PF_RADIO, "background", "Background", 0, (("Ocean", 0), ("Cave", 1)))
        ],
        [],
        python_make_map)

main()