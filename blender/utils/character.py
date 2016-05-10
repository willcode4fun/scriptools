#!/usr/local/bin/python2.7
import bpy
import math
from math import radians
from math import degrees
import materials


zero = (0,0,0)

def addv(v1, v2):
  return (v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2])

def setMaterial(ob, mat):
  me = ob.data
  me.materials.append(mat)

def drawSphere(translateto, radius,material):
  bpy.ops.mesh.primitive_uv_sphere_add(location=zero)
  bpy.ops.transform.translate(value=translateto)
  bpy.ops.transform.resize(value=(radius,radius,radius))
  setMaterial(bpy.context.object, material)
  return bpy.context.object

def drawCube(translateto, size,material):
  bpy.ops.mesh.primitive_cube_add(location=zero)
  bpy.ops.transform.translate(value=translateto)
  bpy.ops.transform.resize(value=(size,size,0.1))
  setMaterial(bpy.context.object, materials.blue)
  
def drawCylinder(translateto, radius, length, material):
  bpy.ops.mesh.primitive_cylinder_add(location=zero)
  bpy.ops.transform.translate(value=translateto)
  bpy.ops.transform.resize(value=(radius,radius,length))
  setMaterial(bpy.context.object, material)
  return bpy.context.object

def drawBone(translateto, radius, length, material):
  point = addv(translateto,(0,0,radius))
  s1 = drawSphere(translateto,radius,material)
  point2 = addv(translateto,(0,0,length+radius))
  s2 = drawSphere(point2,radius,material)
  c1 = drawCylinder(point,radius,length,material)
  return (s1,s2,c1)
  
def rotateG(objs, rot, paxis):
  for obj in objs:  
    obj.select = True  
  bpy.ops.transform.rotate(value=radians(rot),axis=paxis)
def createCharacter():  
  #drawSphere((1.5,0,1.3),0.5)
  #drawSphere((-1.5,0,1.3),0.5)
  #drawSphere((0,0,2.3),1.5)

  #drawSphere((0,1.5,2.3),0.4)
  #drawSphere((0,0,0),1)
  #drawCube((0,0,0),2)
  head = drawSphere((0,0,3.5),1.2,materials.red)
  
  body = drawBone((0,0,1),1.2,0.2,materials.white)
  
  arm1 = drawBone((1,0,3),0.4,0.5,materials.blue)
  rotateG(arm1,135,(0,1,0))
  bpy.ops.transform.translate(value=(0.6,0,-1.5))
  
  arm2 = drawBone((-1,0,3),0.4,0.5,materials.blue)
  rotateG(arm2,-135,(0,1,0))
  bpy.ops.transform.translate(value=(-0.6,0,-1.5))
  

  