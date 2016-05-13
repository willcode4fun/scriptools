#!/usr/local/bin/python2.7
import sys
import os
import bpy
import math
import mathutils
from pprint import pprint
from math import radians
from math import degrees
from mathutils import Vector

def rotate_camera(p_rotation):
	p_camera = bpy.data.objects['Camera']
	#camera position
	loc = Vector((0,3.0,6.0)) * mathutils.Matrix.Rotation(radians(p_rotation), 4, 'Z')
	p_camera.location = loc.to_tuple()
	
	rx = 35.264 #isometric angle
	mat_rot = mathutils.Matrix.Rotation(radians(180-p_rotation), 4, 'Z')
	mat_rot *= mathutils.Matrix.Rotation(radians(rx), 4, 'X')
	#print(mat_rot)
	#print(mat_rot.to_euler())
	p_camera.rotation_euler = mat_rot.to_euler()
	
	fov = 50.0
	# Set camera fov in degrees
	p_camera.data.angle = radians(fov)
	
def rotate_camera_front():
	p_camera = bpy.data.objects['Camera']
	#camera position
	p_camera.location = Vector((0,7.0,2.0)).to_tuple()
	rx = 90.0
	mat_rot = mathutils.Matrix.Rotation(radians(180), 4, 'Z')
	mat_rot *= mathutils.Matrix.Rotation(radians(rx), 4, 'X')
	p_camera.rotation_euler = mat_rot.to_euler()
	fov = 50.0
	# Set camera fov in degrees
	p_camera.data.angle = radians(fov)