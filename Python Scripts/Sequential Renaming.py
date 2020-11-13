import maya.cmds as cmds

input_string = ('Obj_###_Jnt')
char_list = list(input_string)
sels = cmds.ls(sl=True)
num_of_chars = input_string.count('#')
string_parts = input_string.partition('#' * num_of_chars)
piece = input_string.find("#")
index_num = (piece + num_of_chars)

chars_list = []
last_char = index_num - 1

for i in range(piece, last_char, 1):
    character = char_list.pop(i)
    chars_list.extend(character)

new_input_string = ''.join(char_list)

replace_num_string = '1'
replace_num_int = 1
replace_index = (input_string[piece: index_num])
last_name_string = ""

if string_parts[1]:
    for s in sels:
        new_num = replace_num_string.zfill(num_of_chars)
        last_name_string = new_input_string.replace('#', new_num)
        replace_num_int += 1
        replace_num_string = str(replace_num_int)
        cmds.rename(last_name_string)

else:
    print ('Characters are not sequential. Input another string.')