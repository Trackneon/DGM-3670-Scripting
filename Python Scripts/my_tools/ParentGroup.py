import maya.cmds as cmds

sels = cmds.ls(sl=True)

for i in sels:
    new_group = cmds.group(em=True, name=i + "_grp")
    cmds.matchTransform(new_group, i)
    cmds.parent(i, new_group)
    cmds.makeIdentity(i, a=True, t=True, r=True, s=True, n=False)

