#!/usr/local/bin/python2.7
import bpy
import math
from math import radians
from math import degrees
import mathutils
from mathutils import Vector
from mathutils import Quaternion
import materials



zero = (0,0,0)


def dist(p1,p2):
  v = diffv(p2, p1)
  return (v[0]**2 + v[1]**2 + v[2]**2)**0.5
  
def addv(v1, v2):
  return (v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2])
  
def diffv(v1, v2):
  return (v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2])

def setMaterial(ob, mat):
  me = ob.data
  me.materials.append(mat)

def drawSphere(translateto, radius, material):
  return drawEllipsoid(translateto, (radius,radius,radius),material)

def drawEllipsoid(translateto, radiuses, material):
  bpy.ops.mesh.primitive_uv_sphere_add(location=zero)
  bpy.ops.transform.translate(value=translateto)
  bpy.ops.transform.resize(value=radiuses)
  setMaterial(bpy.context.object, material)
  return bpy.context.object
  
def drawCube(translateto, size,material):
  bpy.ops.mesh.primitive_cube_add(location=zero)
  bpy.ops.transform.translate(value=translateto)
  bpy.ops.transform.resize(value=(size,size,0.1))
  setMaterial(bpy.context.object, material)
  
def drawCylinder(translateto, radiuses, length, material):
  bpy.ops.mesh.primitive_cylinder_add(location=zero, depth=length)
  bpy.ops.transform.translate(value=translateto)
  bpy.ops.transform.resize(value=(radiuses[0],radiuses[1],1))
  #bpy.ops.transform.translate(value=(0,0,length/2))
  setMaterial(bpy.context.object, material)
  return bpy.context.object

def drawBone(translateto, radius, length, material):
  point = addv(translateto,(0,0,radius))
  s1 = drawSphere(translateto,radius,material)
  point2 = addv(translateto,(0,0,length))
  s2 = drawSphere(point2,radius,material)
  c1 = drawCylinder(translateto,radius,length,material)
  return (s1,s2,c1)

def drawBone2(p1, p2, radiuses, material):
  length = dist(p1,p2)
  print('length :',length)
  v = Vector(diffv(p1, p2))
  up = Vector((0,0,1))
  if v!=-up:
    rot = up.rotation_difference(v)
  else:
    rot = Quaternion((1,0,0),math.pi)
  s1 = drawEllipsoid((0,0,-0.5*length),radiuses,material)
  s2 = drawEllipsoid((0,0,0.5*length),radiuses,material)
  c1 = drawCylinder(zero,radiuses,length,materials.blue)
  s1.select = True
  s2.select = True
  c1.select = True
  #bpy.ops.transform.translate(value=(0,0,length/2))
  #bpy.ops.object.editmode_toggle()
  bpy.ops.transform.rotate(value=rot.angle, axis=rot.axis)
  #bpy.ops.object.editmode_toggle()
  #bpy.ops.transform.translate(value=Vector((0,0,-0.5*length))*rot.to_matrix())
  rot.normalize();
  bpy.ops.transform.translate(value=Vector((0,0,0.5*length))*rot.to_matrix())
  bpy.ops.transform.translate(value=p1)
  return (s1,s2,c1)
  #return c1
  
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
  drawCube((0,0,0),2,materials.red)
  #drawCube((0,-1,1),1,materials.red)
  drawCube((1,0,3),0.4,materials.red)
  drawCube((1,0,2),0.4,materials.red)
  drawCube((-1,0,3),0.4,materials.red)
  drawCube((-1,0,2),0.4,materials.red)
  #drawCube((0,-1,3),1,materials.red)
  #head = drawSphere((0,0,3.5),1.2,materials.red)
  
  #body = drawBone((0,0,2),1.2,0.2,materials.white)
  
  #body = drawBone2((0,0,2),(1,0,2),(1,1.5,0.6),materials.white)
  
  body52 = drawBone2((-1,0,3),(1,0,3),(0.5,0.5,0.5),materials.green)
  body1 = drawBone2((1,0,2),(1,0,3),(0.3,0.3,0.3),materials.blue)
  body3 = drawBone2((-1,0,2),(-1,0,3),(0.3,0.3,0.3),materials.blue)
  
  body5 = drawBone2((0,0,5),(1,0,3),(0.2,0.2,0.2),materials.blue)
  body4 = drawBone2((0,0,5),(-1,0,3),(0.2,0.2,0.2),materials.blue)
  #arm1 = drawBone((1,0,3),0.4,0.5,materials.blue)
  #rotateG(arm1,135,(0,1,0))
  #bpy.ops.transform.translate(value=(0.6,0,-1.5))
  
  #arm2 = drawBone((-1,0,3),0.4,0.5,materials.blue)
  #rotateG(arm2,-135,(0,1,0))
  #bpy.ops.transform.translate(value=(-0.6,0,-1.5))
  #bpy.ops.transform.translate(value=(-0.6,0,-1.5))
  

  