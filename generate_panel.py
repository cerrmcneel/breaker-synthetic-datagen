import bpy
import os
import math
import random

# --- 1. SETUP ---
model_path = r"C:\ironhack\labs\breaker-synthetic-datagen\BlenderDownloads\ycb7-63n-miniature-circuit-breaker\source\extracted\2_pole_multi.obj"
breaker_width = 0.036

# Cleanup before we start
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# --- 2. THE POWER LOOP ---
for i in range(10): 
    x_pos = i * breaker_width
    
    # Import the model
    bpy.ops.wm.obj_import(filepath=model_path)
    
    # Grab the specific parts we just imported
    imported_parts = bpy.context.selected_objects
    body = None
    switch = None

    # Identify which is which
    for obj in imported_parts:
        if 'switch' in obj.name.lower():
            switch = obj
        else:
            body = obj

    # Move and orient both parts to the same spot
    for obj in imported_parts:
        obj.rotation_euler = (math.radians(90), 0, 0)
        obj.scale = (0.0101, 0.0101, 0.0101)
        obj.location = (x_pos, 0, 0.035)

    # --- 3. THE RANDOMIZER ---
    should_flip = random.choice([True, False])

    if switch:
        if should_flip:
            # Tilt the switch "down" to show it is OFF
            switch.rotation_euler[0] -= math.radians(25)

    # Print the status using double quotes for the outside
    status = "OFF" if should_flip else "ON"
    print(f"Placed {body.name if body else 'Unknown'} with Switch {status}")

print('\nRandomized Panel Complete! 🎲⚡')
