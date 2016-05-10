#!/usr/local/bin/python2.7
import bpy
import math
from math import radians
from math import degrees
import materials


zero = (0,0,0)

def setMaterial(ob, mat):
	me = ob.data
	me.materials.append(mat)

def drawSphere(translateto, radius):
	bpy.ops.mesh.primitive_uv_sphere_add(location=zero)
	bpy.ops.transform.translate(value=translateto)
	bpy.ops.transform.resize(value=(radius,radius,radius))
	#setMaterial(bpy.context.object, red)

def drawCube(translateto, size):
	bpy.ops.mesh.primitive_cube_add(location=zero)
	bpy.ops.transform.translate(value=translateto)
	bpy.ops.transform.resize(value=(size,size,0.1))
	#setMaterial(bpy.context.object, blue)
def createCharacter():	
	drawSphere((1.5,0,1.3),0.5)
	drawSphere((-1.5,0,1.3),0.5)
	drawSphere((0,0,2.3),1.5)

	drawSphere((0,1.5,2.3),0.4)
	drawSphere((0,0,0),1)
	drawCube((0,0,0),2)
	bpy.ops.mesh.primitive_cylinder_add(location=zero)
	bpy.ops.transform.resize(value=(1.5,1.5,1.5))
	setMaterial(bpy.context.object, materials.white)
	bpy.ops.mesh.primitive_cylinder_add(location=(0,0,3.6))
	bpy.ops.transform.resize(value=(1.2,1.2,0.1))
	bpy.ops.transform.rotate(value=radians(15),axis=(1,0,0))
	setMaterial(bpy.context.object, materials.blue)
	bpy.ops.mesh.primitive_cylinder_add(location=(0,0,3.6))
	bpy.ops.transform.resize(value=(0.9,0.9,0.6))
	bpy.ops.transform.rotate(value=radians(15),axis=(1,0,0))
	setMaterial(bpy.context.object, materials.blue)