#!/usr/local/bin/python2.7
# to run : D:/TOOLS/Blender/blender --background minion.blend -P testgen3D.py &
# C:/TOOLS/Blender/blender --background -P testgen3D.py &
# C:/OUTILS/blender-2.77a-windows64/blender --background -P testgen3D.py -- conf.yaml &
import sys
import os
import bpy
import bmesh
from pprint import pprint
import math
from math import radians
sys.path.append('utils')
import character
import configuration
import scene
import camera



scene.clear()
scene.prepare()
#character.createCharacter()


full_path_to_file = os.getcwd()+"/TRTL_GRN.OBJ"
bpy.ops.import_scene.obj(filepath=full_path_to_file)
scene.select_all_meshes()
bpy.ops.transform.resize(value=(2,2,2))

#character.draw_table()

#render front
camera.rotate_camera_front()
scene.render_in_file('image_front.png')

# render iso directions
camera.rotate_camera(0)
scene.select_all_meshes()
for rotation in range(0, 360, int(360/8)):
	print("Rotation %01d" % rotation)
	#camera.rotate_camera( rotation)
	# better rotate scene than camera
	scene.render_in_file('image_%d.png' % rotation)
	bpy.ops.transform.rotate(value=radians(360/8), constraint_axis=(False,False,True))

conf = configuration.read_conf(sys.argv[-1])
pprint(conf)

dims = scene.compute_dimentions()
pprint(dims)


bpy.ops.wm.quit_blender()
#sys.exit(0)