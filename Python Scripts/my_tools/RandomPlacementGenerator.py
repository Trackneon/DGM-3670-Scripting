import maya.cmds as cmds
import random

duplicates = 3

# random.randrange(-20,20)

objects = cmds.ls(sl=True)

# copies.extend(objectCopies)

for o in objects:

    for i in range(0, duplicates):
        objectCopy = cmds.duplicate(o)

        print i

        cmds.move(random.randrange(-20, 20), random.randrange(-20, 20), random.randrange(-20, 20),
                  objectCopy,
                  relative=1,
                  objectSpace=1,
                  worldSpaceDistance=1)
