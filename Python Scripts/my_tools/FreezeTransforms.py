import maya.cmds as cmds

sels = cmds.ls(sl=True)

for i in sels:

    cmds.makeIdentity(i, a=True, t=True, r=True, s=True, n=False)