# -*- coding: utf-8 -*-

'''
把外接扩展插件载入环境变量
'''

from os import path, symlink, sep, remove
from program_top.utilities.my_dir import browse_dir, get_relative_filename_from_absolute

def load_shared_objects():
	'''将所有扩展中的共享链接库软链接到程序文件夹'''
	current_filename=__file__
	extention_init_file=path.realpath(current_filename)
	extension_path=path.dirname(extention_init_file)
	project_path=path.dirname(extension_path)
	target_so_files=browse_dir(extension_path, '.so')
	
	for each_so in target_so_files:
		'''
		如果有什么扩展.so库，就把它创建符号链接到项目文件夹，供搜索
		'''
		relative_so_name=get_relative_filename_from_absolute(each_so)
		symlinked_lib_name=project_path+sep+relative_so_name
		
		try:#无论软链接是否存在，都先删除之
			remove(symlinked_lib_name)
		except:
			pass
		
		try:
			symlink(each_so, symlinked_lib_name)#这里使用绝对地址的目标做链接
		except:
			pass
		pass
	pass

load_shared_objects()