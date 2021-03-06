# Installation

This is a GIMP plugin. You will need GIMP in order to use it.

https://docs.gimp.org/en/gimp-scripting.html#gimp-plugins-install

The files that need to be moved into the plug-ins folder are:
* addText.py
* layerfx.py
* letterprinter.py
* pixelateMap.py
* setupMap.py

You may need to chmod +x the .py files in order for it to show up in GIMP. If the plug-in still doesn't show up, it's possible that the GIMP build you installed is missing gimp-python. If you are on Linux, you can get this from your package manager.

If you are using GNU Linux or macOS Catalina, you can probably use the install.sh script. The install script assumes you are using GIMP 2.10 installed in the default location.

# Usage

To create the layers and layer groups for a map, use `File > Create > Patterns > Map...`.

Based on GentleTractor's suggested setup:
https://www.reddit.com/r/GentleTractor/comments/4ziq7v/howto_guide_resources_for_making_fake_old_school/

In order to make the clipping mask, draw in the "Landmass" layer. Once you have a suitable landmass, use the color selector tool (Shift+o) and click on your landmass. If your landmass is more than one color, you will need to Shift+left click each color until they are all selected. Then right click the layer group `"Terrain Group" > Add Layer Mask > Selection > Add`.

Whenever you have a blended terrain that you are satisfied with, use the tool found at `Filter > Map > Pixelate map...` and enter in the block size you want to use. You should use whatever you selected when you created the map, but there's nothing stopping you from doing otherwise. This will create a new layer (Terrain Pixelated) in the Terrain Group. If you change the layer names generated, this will probably fail.

In order to add labels, use `Filter > Map > Add label...`. The labels support a-z, A-Z, spaces, hyphens, and apostrophes. Other characters will cause the plugin to crash. If other characters are needed, open an issue.

# Future Improvements

* <strike>Add a plug-in to pixelate an almost finished map</strike>
* <strike>Actually put something in install.sh. Need feedback on where to put it in different operating systems.</strike>
	* Add Windows install
* <strike>Create a layer with reference objects, icons, and colors</strike> Added GentleTractor's sprite page
	* Might want to condense and add new icons
* Add x,y to label creation?
