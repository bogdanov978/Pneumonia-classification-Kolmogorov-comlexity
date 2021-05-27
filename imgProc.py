import cv2
import os
import py7zr

def preprocess_img(directory, img_path, img_size, label, name):
    text_dir = directory + "/text files/" + label + "/" 
    arc_dir =  directory + "/archives/" + label + "/"
    #
    raw_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(raw_img, (img_size, img_size))
    # cv2.imwrite(directory + "/images/" + label + "/" + name + ".jpeg", image)
    # Получение содержимого текстового файла и запись на диск
    bin_repr = [0] * img_size * img_size
    for y in range(img_size):
        for x in range(img_size):
            bin_repr[y*img_size + x] = image[y, x]
    
    bin_repr = bytes(bin_repr)    
    text_file = open(text_dir + name + ".txt", "wb")
    text_file.write(bin_repr)
    text_file.close()
    # Создание архива из текстового файла:
    os.chdir(text_dir)
    with py7zr.SevenZipFile(arc_dir + name + ".7z", 'w') as archive:
        archive.write(name + ".txt")
    os.chdir(directory[:directory.rfind('/data')])
