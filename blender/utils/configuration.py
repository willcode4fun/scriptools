#!/usr/local/bin/python2.7
import sys
import os
import json

def read_conf(file_name = 'conf.json'):
	with open(file_name) as data_file:    
		data = json.load(data_file)
	return data

