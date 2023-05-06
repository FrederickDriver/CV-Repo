import os
from PIL import Image

directory = '/content/CV-Repo/new_data/data/labels/test/'
image_directory = '/content/CV-Repo/new_data/data/images/test/'
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename)) as f:
            file_text = f.read()
            words = file_text.split()
            pure_name = filename[:-4]
            image_path = image_directory + pure_name + ".png"
            im = Image.open(image_path)
            w, h = im.size
            words[1] =  str(float(words[1])/w)
            copy = words[3]
            words[3] =  str(float(words[4])/w)
            words[2] =  str(float(words[2])/h)
            words[4] =  str(float(copy)/h)
            words[1] =  str(float(words[1]) + float(words[3])/2)
            words[2] =  str(float(words[2]) + float(words[4])/2)
            to_write = words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4]
            f.close()
        f_write = open(directory + filename, "w")
        f_write .write(to_write)
        f_write.close()
