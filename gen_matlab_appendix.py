#!/bin/python
# Genera la appendice con i file Matlab
import string
import os
import fnmatch
import glob

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

def list_m_files(matlab_path):
	pattern="*.m"
	list_m_files={}
	a=recursive(matlab_path)
	for k in a:
		#print k
		files=os.listdir(k)
		m_files = fnmatch.filter(files, pattern)
		dir_name=string.split(k,'MatlabFiles/')[1]
		list_m_files[dir_name]=m_files
	return list_m_files

def write_header(tex_file):
	out=open(tex_file,'w')
	header=(
'''\chapter{Matlab Code}
\label{chptr:Matlab}
\lstset{language=matlab,
basicstyle=\\fontfamily{pcr}\\footnotesize,
numberstyle=\\tiny,
commentstyle=\color{blue}\itshape,
stringstyle=\color{red},
showstringspaces=false,
tabsize=3,
numbers=left}\n\n'''
)
	out.write(header)
	out.close()

def write_section(m_file,tex_file):
	input_file=open(m_file,'r')
	output_file=open(tex_file,'a')
	#nome_m_file=string.split(m_file,'/')[-1]
	nome_m_file=string.split(os.path.splitext(m_file)[0],'/')[-1]
	header=('\section{%s}\n\label{sec:%s}\n' % (nome_m_file,nome_m_file))
	body=input_file.read()
	output_file.write(header)
	output_file.write(body)
	input_file.close()
	output_file.close()

a=recursive(matlab_path)
#print a

print list_m_files(matlab_path)

#cropped_a=crop_dirnames(a,'MatlabFiles/')
#print cropped_a
#for j in a: b.append(string.split(j,'MatlabFiles/')[1])

out_filename='pippo1.txt'
write_header(out_filename)
write_section('/home/michele/Dropbox/MachineDesign/MatlabFiles/M-Dynamics/riprove per trovare angoli/alpha1.m',out_filename)
# with open(out_filename, 'w') as file_out:
# 	file_out.write(write_section())

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
