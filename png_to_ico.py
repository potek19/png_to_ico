from PIL import Image
import os

input_folder = 'Input'
output_folder = 'Output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.ico')
        
        if not os.path.exists(output_path):
            img = Image.open(input_path)
            img.save(output_path)