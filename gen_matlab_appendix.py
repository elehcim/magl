#!/bin/python
# Genera la appendice con i file Matlab
import string
import os
import fnmatch

#f=open('~/Dropbox/MachineDesign/Design of an air turbine starter for an aircraft engine','r')

matlab_path='/home/michele/Dropbox/MachineDesign/MatlabFiles'

subfolder_list=[]
def recursive(initial_path):
	global subfolder_list
	for f in next(os.walk(initial_path))[1]:
		if f==[]:continue
		#print subfolder_list
		newpath=os.path.join(initial_path, f)
		recursive(newpath)
		subfolder_list.append(newpath)
	return subfolder_list

def crop_dirnames(arg, sep):
	b=[]
	for j in arg: b.append(string.split(j,sep)[1])
	return b

def list_m_files(path):
	for 

def write_section(f):
	header=
	
a=recursive(matlab_path)
cropped_a=crop_dirnames(a,'MatlabFiles/')
#for j in a: b.append(string.split(j,'MatlabFiles/')[1])
for i in cropped_a: print i


out_filename='pippo1.txt'
with open(out_filename, 'w') as file_out:
	file_out.write(write_section())

# for filename in fnmatch.filter(files, pattern):
#         print( os.path.join(root, filename))


# for f in next(os.walk(matlab_path))[1]: 
# 	print f
# 	subdir=os.walk(f[1])
# 	print subdir[2]
# 	print f
# #print files



#---------------
# files=os.listdir(matlab_path)
# print files
# def sezione(arg):
# 	print '\section{arg}'

# #os.path.join('/foo/bar', f)

# for f in files: os.path.isdir(os.path.join(matlab_path, f))


#root, dirs, files = next(os.walk(matlab_path))

# print 'directories:', dirs
# print 'files:', files
