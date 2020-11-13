import maya.cmds as cmds

object_name_string = ('Sphere_###_Jnt')

num_of_chars = object_name_string.count('#')
string_parts = object_name_string.partition('#' * num_of_chars)

zfill