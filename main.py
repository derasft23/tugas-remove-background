import rembg
from PIL import Image
import numpy as np

def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

        
        output_data = rembg.remove(input_data)

       
        with open(output_path, "wb") as output_file:
            output_file.write(output_data)


input_image_path = "sample/Ukhti.jpg"
p = input_image_path.split("/")
name_img = p[1].split(".")
output_image_path = f"output/{name_img[0]}_ini_rm_bg.png"
remove_background(input_image_path, output_image_path)
