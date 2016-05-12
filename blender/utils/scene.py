#!/usr/local/bin/python2.7
import sys
import os
import bpy
import mathutils
from mathutils import Vector

def prepare():
	scene = bpy.data.scenes['Scene']
	scene.render.resolution_x = 500
	scene.render.resolution_y = 500
	scene.world.ambient_color = (0.1,0.1,0.1)
	scene.render.image_settings.file_format="PNG";
	scene.render.alpha_mode = 'TRANSPARENT' 
	scene.render.use_edge_enhance = True
	scene.render.edge_threshold = 1
	scene.render.use_antialiasing = True
def clear():
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.ops.object.select_by_type(type='MESH')
	bpy.ops.object.delete(use_global=False)
	for item in bpy.data.meshes:
		bpy.data.meshes.remove(item)
def render_in_file(filename):
	bpy.context.scene.render.filepath = os.getcwd()+"/"+filename
	bpy.ops.render.render( write_still=True)	

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