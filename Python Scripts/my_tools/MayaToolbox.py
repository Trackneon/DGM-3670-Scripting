import maya.cmds as cmds


class MayaToolboxUI():
    def __init__(self):
        self.tool_window = 'cl_MayaToolboxWindow'

    def create(self):
        self.delete()

        self.tool_window = cmds.window(self.tool_window,
                                       title='Maya Toolbox Window',
                                       widthHeight=(200, 200))

        self.col_layout = cmds.columnLayout(parent=self.tool_window,
                                            adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='Delete History', c=lambda *x: self.call_delete_history())
        cmds.button(parent=self.col_layout, label='Freeze Transformations', c=lambda *x: self.call_freeze_transforms())
        cmds.button(parent=self.col_layout, label='Parent Group', c=lambda *x: self.call_parent_group())
        cmds.button(parent=self.col_layout, label='Parent/Scale Constraint', c=lambda *x: self.call_ps_constraint())
        cmds.button(parent=self.col_layout, label='Local Axis', c=lambda *x: self.call_local_axis())
        cmds.button(parent=self.col_layout, label='Rename/Random Gen', c=lambda *x: self.call_renamer_toolbox())

        cmds.showWindow(self.tool_window)

    def delete(self):
        if cmds.window(self.tool_window, exists=True):
            cmds.deleteUI(self.tool_window)

    def call_delete_history(self):
        import DeleteHistory
        reload(DeleteHistory)
        pass

    def call_freeze_transforms(self):
        import FreezeTransforms
        reload(FreezeTransforms)
        pass

    def call_parent_group(self):
        import ParentGroup
        reload(ParentGroup)
        pass

    def call_ps_constraint(self):
        import ParentScaleConstraint
        reload(ParentScaleConstraint)

    def call_local_axis(self):
        import DisplayLocalAxis
        reload(DisplayLocalAxis)

    def call_renamer_toolbox(self):
        import RenamerToolbox
        reload(RenamerToolbox)
        # renamer_toolbox_instance = RenamerToolbox.RenamerToolboxUI()
        # renamer_toolbox_instance.create_tool_window()
        pass


tool_window = MayaToolboxUI()
tool_window.create()
