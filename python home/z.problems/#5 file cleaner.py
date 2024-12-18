import os 
import shutil

os.chdir("d:\\DCIM\\Download")
a=os.listdir("d:\\DCIM\\Download")

# os.mkdir("video")
# os.mkdir("image")
# os.mkdir("pdf")
# os.mkdir("extra")
for file in a :
    if file.endswith(".jpg"):
        shutil.move(file,"d:\\DCIM\\Download\\image")
    elif file.endswith(".pdf"):
        shutil.move(file,"d:\\DCIM\\Download\\pdf")
    elif file.endswith(".mp4"):
        shutil.move(file,"d:\\DCIM\\Download\\video")
    else:
        shutil.move(file,"d:\\DCIM\\Download\\extra") #galti hogyi , else se sari file + folder extra ke andar chale gye !