import maya.cmds as cmds
import random

def createRandomObjects(obj_file, num_objects, distance_range):
    for i in range(num_objects):
        x_pos = random.uniform(-distance_range, distance_range)
        z_pos = random.uniform(-distance_range, distance_range)
        y_rot = random.uniform(0, 360) #rotate around y axis

        #import file
        cmds.file(obj_file, i=True, usingNamespaces=False)
        imported_obj = cmds.ls(type='transform', long=True)[0]
        new_name = 'randomObject_' + str(cmds.ls('randomObject_*', long=True).__len__() + 1) #unique names
        cmds.rename(imported_obj, new_name)
        
        #move and rotate object
        cmds.move(x_pos, 0, z_pos, new_name)
        cmds.rotate(0, y_rot, 0, new_name)

#create window
def createRandomizerUI():
    if cmds.window("randomizerWindow", exists=True):
        cmds.deleteUI("randomizerWindow", window=True)
    window = cmds.window("randomizerWindow", title="Randomizer", widthHeight=(500, 500))
    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="Upload OBJ File:")
    obj_file_field = cmds.textField("objFilePath", editable=False)
    cmds.button(label="Browse", command=lambda x: openFileDialog(obj_file_field))

    cmds.separator(height=10)

    cmds.text(label="Enter Number of Objects:")
    num_objects_field = cmds.intField("numObjectsField", minValue=1, value=1)

    cmds.separator(height=10)

    cmds.text(label="Enter Distance Range:")
    distance_range_field = cmds.floatField("distanceRangeField", minValue=0.1, value=10.0)

    cmds.separator(height=10)

    cmds.button(label="Create Random Objects", command=lambda x: createRandomObjects(
        cmds.textField("objFilePath", query=True, text=True),
        cmds.intField(num_objects_field, query=True, value=True),
        cmds.floatField(distance_range_field, query=True, value=True)
    ))

    cmds.showWindow(window)

#select file dialog box
def openFileDialog(obj_file_field):
    result = cmds.fileDialog2(fileFilter='Wavefront OBJ (*.obj)', dialogStyle=2, fileMode=1)
    if result:
        cmds.textField(obj_file_field, edit=True, text=result[0])

createRandomizerUI()
