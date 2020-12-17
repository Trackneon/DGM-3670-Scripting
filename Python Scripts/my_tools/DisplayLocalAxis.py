import maya.cmds as cmds

sels = cmds.ls(sl=True)

for i in sels:
    cmds.toggle(i, la=True)

    cmds.setAttr(i+'.displayLocalAxis', k=True)
    cmds.setAttr(i + '.jointOrientX', k=True)
    cmds.setAttr(i + '.jointOrientY', k=True)
    cmds.setAttr(i + '.jointOrientZ', k=True)


