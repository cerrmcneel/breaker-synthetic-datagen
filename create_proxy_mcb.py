import bpy 
import os

#tell the system where the actual 3D model is located
model_dir= r"c:\ironhack\labs\breaker-synthetic-datagen\BlenderDownloads\ycb7-63n-miniature-circuit-breaker\source\extracted"
model_file = "YCB7-63n.obj"
full_path = os.path.join(model_dir, model_file)

#clear the scene
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH': 
        obj.select_set(True)
bpy.ops.object.delete()
#import the model
if os.path.exists(full_path):
    bpy.ops.wm.obj_import(filepath=full_path)
    #grab te newly imported object
    mcb = bpy.context.selected_objects[0]
    mcb.name = "Real_MCB"

    #correct the scale. Standar MCBs are ~18mm wide
    mcb.dimensions = (0.018, 0.080, 0.070)
    #place the object on the floor
    mcb.location = (0, 0, 0.035)
 
    print(f'Success! Imported {mcb.name} at real-world scale')
else:
    print(f'Error: Could not find the model at {full_path}')