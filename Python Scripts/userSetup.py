import maya.cmds as cmds
import sys

if not cmds.commandPort(':4434', query=True):
    cmds.commandPort(name=':4434')

if 'D:/UVU/Fall 2020/DGM 3670/Git Repo/DGM 3670 Scripting/Python Scripts' not in sys.path:
    sys.path.append('D:/UVU/Fall 2020/DGM 3670/Git Repo/DGM 3670 Scripting/Python Scripts')