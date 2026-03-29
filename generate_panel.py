import bpy
import os
import math

model_path = r"C:\ironhack\labs\breaker-synthetic-datagen\BlenderDownloads\ycb7-63n-miniature-circuit-breaker\source\extracted\2_pole.obj"
breaker_width = 0.036
breaker_depth = 0.0753
breaker_height = 0.0844

#clear the scene
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
bpy.ops.object.delete()

# create 1x10 grid of breakers
for i in range(10): 
    x_pos = i * breaker_width
    #import the model
    bpy.ops.wm.obj_import(filepath=model_path)
    #Grab the active object
    mcb = bpy.context.selected_objects[0]
    #give it a unique name
    mcb.name = f'MCB_{i:02d}'
    mcb.rotation_euler = (math.radians(90), 0, math.radians(0))
    #set position and scale
    mcb.scale = (0.0101, 0.0101, 0.0101)
    bpy.context.view_layer.update()
 
    #rotate
    mcb.location = (x_pos, 0, 0.035)

    print(f'Placed {mcb.name} at X: {x_pos:.3f}m | Real Size: X={mcb.dimensions.x:.3f}, Y={mcb.dimensions.y:.3f}, Z={mcb.dimensions.z:.3f}')
print('\nPanel Generation Complete!')