#!/bin/bash
echo $BLENDER_HOME
$BLENDER_HOME/blender --background -P testgen3D.py -- conf.yaml &