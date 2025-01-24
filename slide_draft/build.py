from os import listdir, system
from pathlib import Path

scenes = ["Inheritance"]

system("export PYTHONPATH=$(pwd)")

for scene in scenes:
    system(f"manim-slides render ./scene/{scene}.py {scene}")
    
system(f"manim-slides convert {' '.join(scenes)} ./out/index.html")