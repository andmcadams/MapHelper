# Installation

This is a GIMP plugin. You will need GIMP in order to use it.

https://docs.gimp.org/en/gimp-scripting.html#gimp-plugins-install

You may need to chmod +x the setupMap.py and pixelateMap.py files in order for it to show up in GIMP.

On Linux, I simply ran
`$ cp setupMap.py ~/.config/GIMP/2.10/plug-ins/`
and
`$ cp pixelateMap.py ~/.config/GIMP/2.10/plug-ins/`

to install.

# Usage

To create the layers and layer groups for a map, use `File > Create > Patterns > Map...`.

Based on GentleTractor's suggested setup:
https://www.reddit.com/r/GentleTractor/comments/4ziq7v/howto_guide_resources_for_making_fake_old_school/

In order to make the clipping mask, draw in the "Landmass" layer. Once you have a suitable landmass, use the color selector tool (Shift+o) and click on your landmass. If your landmass is more than one color, you will need to Shift+left click each color until they are all selected. Then right click the layer group "Terrain Group" > Add Layer Mask > Selection > Add.

Whenever you have a blended terrain that you are satisfied with, use the pixelateMap tool found at `Filter > Map > Pixelate map...` and enter in the block size you want to use. You should probably use whatever you selected when you created the map, but there's nothing stopping you from doing otherwise. This will create a new layer (Terrain Pixelated) in the Terrain Group. If you change the layer names generated, this will probably fail.

# Future Improvements

* <strike>Add a plug-in to pixelate an almost finished map</strike>
* Actually put something in install.sh. Need feedback on where to put it in different operating systems.
* Create a layer with reference objects, icons, and colors?
