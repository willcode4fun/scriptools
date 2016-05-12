#!/usr/local/bin/python2.7
# to run : D:/TOOLS/Blender/blender --background minion.blend -P testgen3D.py &
# C:/TOOLS/Blender/blender --background -P testgen3D.py &
# C:/OUTILS/blender-2.77a-windows64/blender --background -P testgen3D.py -- conf.yaml &
import sys
import os
import bpy
import bmesh
from pprint import pprint

sys.path.append('utils')
import character
import configuration
import scene
import camera

scene.clear()
scene.prepare()
character.createCharacter()

#render front
camera.rotate_camera_front()
scene.render_in_file('image_front.png')

# render iso directions
for rotation in range(0, 360, int(360/8)):
	print("Rotation %01d" % rotation)
	camera.rotate_camera( rotation)
	scene.render_in_file('image_%d.png' % rotation)


conf = configuration.read_conf(sys.argv[-1])
pprint(conf)
scene.groupAll()
bpy.ops.wm.quit_blender()
#sys.exit(0)