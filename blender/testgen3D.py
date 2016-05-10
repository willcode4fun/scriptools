#!/usr/local/bin/python2.7
# to run : D:/TOOLS/Blender/blender --background minion.blend -P testgen3D.py &
# C:/TOOLS/Blender/blender --background -P testgen3D.py &
import sys
import os
import bpy
import bmesh
import math
import mathutils
from math import radians
from math import degrees
from mathutils import Vector
sys.path.append('utils')
import character

def clear_scene():
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.ops.object.select_by_type(type='MESH')
	bpy.ops.object.delete(use_global=False)
	for item in bpy.data.meshes:
		bpy.data.meshes.remove(item)


	
def rotate_camera(p_camera, p_rotation):
	#camera position
	loc = Vector((0,3.0,6.0)) * mathutils.Matrix.Rotation(radians(p_rotation), 4, 'Z')
	p_camera.location = loc.to_tuple()
	
	rx = 35.264 #isometric angle
	mat_rot = mathutils.Matrix.Rotation(radians(180-p_rotation), 4, 'Z')
	mat_rot *= mathutils.Matrix.Rotation(radians(rx), 4, 'X')
	print(mat_rot)
	print(mat_rot.to_euler())
	p_camera.rotation_euler = mat_rot.to_euler()
	
	fov = 50.0
	# Set camera fov in degrees
	p_camera.data.angle = radians(fov)
	
def rotate_camera_front(p_camera):
	#camera position
	loc = Vector((0,6.0,3.0))
	p_camera.location = loc.to_tuple()
	
	rx = 90.0
	mat_rot = mathutils.Matrix.Rotation(radians(180), 4, 'Z')
	mat_rot *= mathutils.Matrix.Rotation(radians(rx), 4, 'X')
	print(mat_rot)
	print(mat_rot.to_euler())
	p_camera.rotation_euler = mat_rot.to_euler()
	
	fov = 50.0
	# Set camera fov in degrees
	p_camera.data.angle = radians(fov)




def printrot(vect):
	print("rotation %f %f %f" % (degrees(vect[0]), degrees(vect[1]), degrees(vect[2])))
clear_scene()	

def createBall():
	bpy.ops.mesh.primitive_uv_sphere_add(segments= 8, ring_count=8, location=(0,0,2))
	bpy.ops.transform.resize(value=(2,2,2))
	bpy.ops.object.mode_set(mode = 'EDIT')
	bpy.ops.mesh.select_all(action = 'SELECT')
	bpy.ops.mesh.mark_seam()
	bpy.ops.uv.sphere_project(direction ='VIEW_ON_EQUATOR')
	#setMaterial(bpy.context.object, mat)

def maxVect(vect1, vect2):
	return Vector((max(vect1.x,vect2.x),max(vect1.y,vect2.y),max(vect1.z,vect2.z)))

def minVect(vect1, vect2):
	return Vector((min(vect1.x,vect2.x),min(vect1.y,vect2.y),min(vect1.z,vect2.z)))
	
def groupAll():
	if not 'myGroup' in bpy.data.groups:  
		bpy.ops.group.create(name="myGroup")   
	# if you want to select all mesh objects.  
	objects_to_add = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']  	  
	scn = bpy.context.scene  
	max = Vector((0,0,0))
	min = Vector((0,0,0))
	for name in objects_to_add:
		min = minVect(min, scn.objects[name].location)
		max = maxVect(max, scn.objects[name].location + scn.objects[name].dimensions)
		scn.objects.active = scn.objects[name]  
		bpy.ops.object.group_link(group="myGroup") 
	print("min")
	print(min)
	print("max")
	print(max)
scene = bpy.data.scenes['Scene']

#mat = createMaterial() 

# Create new cube and give it UVs
#bpy.ops.mesh.primitive_cube_add(location=(0,0,2))
bpy.ops.mesh.primitive_uv_sphere_add(segments= 8, ring_count=8, location=(0,0,2))
#bpy.ops.mesh.primitive_uv_sphere_add( location=(0,0,2))
#bpy.ops.transform.resize(value=(2,2,2))
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.mark_seam()
#bpy.ops.uv.smart_project()
bpy.ops.uv.sphere_project(correct_aspect = False)
bpy.ops.uv.stitch()
# Add material to current object
#setMaterial(bpy.context.object, mat)


cam = bpy.data.objects['Camera']
# Set render resolution
scene.render.resolution_x = 500
scene.render.resolution_y = 500
scene.world.ambient_color = (0.1,0.1,0.1)
num_steps = 8
stepsize = 360/num_steps
scene.render.image_settings.file_format="PNG";
scene.render.alpha_mode = 'TRANSPARENT' 
scene.render.use_edge_enhance = True
scene.render.edge_threshold = 1
scene.render.use_antialiasing = True

bpy.ops.object.mode_set(mode='OBJECT')
bpy.data.objects['Sphere'].select = True
bpy.ops.object.delete()

character.createCharacter()

groupAll()
#bpy.ops.transform.resize(value=(0.5, 0.5, 0.5))
#render front
rotate_camera_front(cam)
scene.render.filepath = os.getcwd()+'/image_front.png'
bpy.ops.render.render( write_still=True) 

def isometric8directions() :
	for step in range(0, num_steps):
		rotation = stepsize*step
		print("Rotation %01d" % rotation)
		rotate_camera(cam, rotation)
		scene.render.filepath = os.getcwd()+'/image_%d.png' % rotation
		bpy.ops.render.render( write_still=True) 
		print(cam.location)
isometric8directions()
	
#for ob in bpy.data.objects:
#    print (ob.name)
	
test = Vector((4,0,0)) * mathutils.Matrix.Rotation(radians(90), 4, 'Z')
print(test)
bpy.ops.wm.quit_blender()
#sys.exit(0)