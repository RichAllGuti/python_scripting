#
from PIL import Image
import os

#image_folder = "/Users/johnall/Downloads/images/"
image_folder = "C:/Users/(user_name)/Downloads/images/"

if __name__ == "__main__":

    for image_in_folder in  os.listdir(image_folder):

        image_name, image_extension = os.path.splitext(image_folder + image_in_folder)
        
        if image_extension in [".png",".jpg",".jpeg"]:
            
            image_name = Image.open(image_folder + image_in_folder)
            image_name.save(image_folder + "Compressed_image_"+image_in_folder, optimize = True, quality = 70)

    