"""writer-:SurjeetLodhiRajput
   ContactInfo-Surjeetrajput433@gmail.com
   all right are reserved to the writers of this code
   /this code can be used wherever you want but the thing you need to give appreciation to the writer of this code
"""
import PIL
from PIL import Image
import os
mywidth=2000
source_dir="C:\\Users\\HP\\Pictures\\database"
destination_dir="C:\\Users\\HP\\Pictures\\newdb"
def resize_pic(old_pic,new_pic,mywidth):
    img=Image.open(old_pic)
    wpercent=(mywidth/float(img.size[0]))
    hsize=int((float(img.size[1])*float(wpercent)))
    img=img.resize((mywidth,hsize),PIL.Image.ANTIALIAS)
    img.save(new_pic)
    print('done image successfully')

def entire_directory(source_dir,destination_dir,width):
    files=os.listdir(source_dir)
    i=0
    try:
        os.makedirs(destination_dir)
    except:
        pass
    for file in files:
        i+=1
        old_pic=source_dir+'/'+file
        new_pic=destination_dir+'/'+file
        resize_pic(old_pic,new_pic,width)
        print(i,"pictures done!")