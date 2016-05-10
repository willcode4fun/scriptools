#!/usr/local/bin/python2.7
import sys
import os
import bpy
def makeMaterial(name, diffuse, specular, alpha):
	mat = bpy.data.materials.new(name)
	mat.diffuse_color = diffuse
	mat.diffuse_shader = 'TOON'
	mat.diffuse_intensity = 1.0
	mat.specular_color = specular
	mat.specular_shader = 'TOON'
	mat.specular_intensity = 0.5
	mat.alpha = alpha
	mat.ambient = 10
	mat.emit=0.5
	return mat

red = makeMaterial('Red',(1,0,0),(1,0.5,.05),1)
blue = makeMaterial('Blue',(0,0,1),(1,1,1),1)
white = makeMaterial('White',(1,1,1),(1,1,1),1)

def createMaterial():    
    # Create image texture from image. Change here if the snippet 
    # folder is not located in you home directory.
    realpath = os.path.expanduser('D:/PROJETS/PERSO/blender/face.png')
    tex = bpy.data.textures.new('ColorTex', type = 'IMAGE')
    tex.image = bpy.data.images.load(realpath)
    tex.use_alpha = True
 
    # Create shadeless material and MTex
    mat = bpy.data.materials.new('TexMat')
    mat.use_shadeless = True
    mtex = mat.texture_slots.add()
    mtex.texture = tex
    mtex.texture_coords = 'UV'
    mtex.use_map_color_diffuse = True 
    return mat