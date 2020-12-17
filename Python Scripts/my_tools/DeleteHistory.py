import maya.cmds as cmds

sels = cmds.ls(sl=True)

for i in sels:

    cmds.delete(i, ch=1)

