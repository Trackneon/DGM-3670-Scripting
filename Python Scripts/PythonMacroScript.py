import maya.cmds as cmds

cmds.polySphere(name='Sphere_Geo',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(0,2,0, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(2,2,2, relative=1)

cmds.polySphere(name='Sphere_Geo1',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(0,4,0, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(1.5,1.5,1.5, relative=1)

cmds.polySphere(name='Sphere_Geo2',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(0,6,0, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(1.2,1.2,1.2, relative=1)

cmds.polySphere(name='Eye_Geo',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(.5,6.2,1.07, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(.3,.3,.1, relative=1)
cmds.rotate(0,26.6,0)

cmds.polySphere(name='Eye_Geo1',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(-.5,6.2,1.07, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(.3,.3,.1, relative=1)
cmds.rotate(0,-26.6,0)

cmds.polySphere(name='Button_Geo',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(0,2,1.95, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(.5,.5,.1, relative=1)
cmds.rotate(0,0,0)

cmds.polySphere(name='Button_Geo1',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(0,4,1.43, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(.4,.4,.1, relative=1)
cmds.rotate(0,0,0)

cmds.polyCone(name='Nose_Geo',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0])
cmds.move(0,6,1.43, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(.3,1,.3, relative=1)
cmds.rotate(90,0,0)

cmds.polyCylinder(name='Hat_Geo',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=3,
                subdivisionsCaps=2,
                axis=[0,1,0])
cmds.move(0,7.7,0, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(1,.7,1, relative=1)

cmds.polyCylinder(name='Hat_Geo1',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=1,
                subdivisionsCaps=1,
                axis=[0,1,0])
cmds.move(0,7,0, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(1.3,.3,1.3, relative=1)

cmds.polyCylinder(name='LArm_Geo',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=3,
                subdivisionsCaps=2,
                axis=[0,1,0])
cmds.move(2,4.6,0, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(.2,2.5,.2, relative=1)
cmds.rotate(0,0,-74)

cmds.polyCylinder(name='RArm_Geo',
                radius=1,
                subdivisionsX=20,
                subdivisionsY=3,
                subdivisionsCaps=2,
                axis=[0,1,0])
cmds.move(-2,4.6,0, relative=1, objectSpace=1, worldSpaceDistance=1)
cmds.scale(.2,2.5,.2, relative=1)
cmds.rotate(0,0,60)