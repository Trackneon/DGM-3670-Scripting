import maya.cmds as cmds

sels = cmds.ls(sl=True)

if len(sels) % 2 == 1:
    cmds.error('Too many items selected.')

sels_num = len(sels)
#ctrls = sels[0:len(sels)/2] #you don't need to put 0 in front of or after a colon in python
#joints = sels[len(sels)/2:]

#loop through ctrls and joints to parent each joint to ctrls

for i in range(0, sels_num, 2):
    print 'I want to constrain %s to %s' % (sels[i+1], sels[i])
    cmds.parentConstraint(sels[i+1], sels[i], maintainOffset=False)
    cmds.scaleConstraint(sels[i+1], sels[i], maintainOffset=False)