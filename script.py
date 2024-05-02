import os
import math

def pmtok_hud(ratio_value, HUD_pos, ui_folder):
    scale_factor = (16/9) / ratio_value
    for root, dirs, files in os.walk(ui_folder):
        for file in files:
            if file.endswith('.bfres'):
                pass
                # Do the scaling
                # looks for the Skeleton part of every bfres, and then scales x by the scale_factor, from 1 to 0.76 for example
    if HUD_pos == "corner":
        # Shift stuff
        pass
