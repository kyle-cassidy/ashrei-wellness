# import os
# import subprocess

# source_dir = "/Users/kielay/Developer/Projects/ashrei/ashrei-wellness/home/assets/icons/stack/webp"
# target_dir = (
#     "/Users/kielay/Developer/Projects/ashrei/ashrei-wellness/home/assets/icons/stack"
# )

# for filename in os.listdir(source_dir):
#     if filename.endswith(".webp"):
#         input_path = os.path.join(source_dir, filename)
#         output_path = os.path.join(target_dir, filename.replace(".webp", ".svg"))

#         subprocess.run(["inkscape", input_path, f"--export-plain-svg={output_path}"])

# print("Conversion complete.")
######################################333

import os
import subprocess
from PIL import Image

source_dir = "/Users/kielay/Developer/Projects/ashrei/ashrei-wellness/home/assets/icons/stack/webp"
target_dir = (
    "/Users/kielay/Developer/Projects/ashrei/ashrei-wellness/home/assets/icons/stack"
)

for filename in os.listdir(source_dir):
    if filename.endswith(".webp"):
        input_path = os.path.join(source_dir, filename)
        png_path = os.path.join(target_dir, filename.replace(".webp", ".png"))
        svg_path = os.path.join(target_dir, filename.replace(".webp", ".svg"))

        # Convert WebP to PNG
        with Image.open(input_path) as img:
            img.save(png_path, "PNG")

        # Convert PNG to SVG using Inkscape
        subprocess.run(["inkscape", png_path, f"--export-filename={svg_path}"])

        # Remove the temporary PNG file
        os.remove(png_path)

print("Conversion complete.")
