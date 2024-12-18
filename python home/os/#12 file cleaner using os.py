import os 
os.chdir("d:\DCIM\Download\extra")
# os.mkdir("other file")
a=os.listdir("d:\DCIM\Download\extra")
image_ext = ['.jpg','.jpeg','.png']
video_ext = ['.mp4','.flv']
docc_ext = ['.text','.pdf','.docs']
for file in a:
    if (os.path.splitext(file)[1].lower in image_ext):
        os.replace(file,f"d:\\DCIM\\Download\\extra\\image\\{file}")
    elif (os.path.splitext(file)[1].lower in video_ext):
        os.replace(file,f"d:\\DCIM\\Download\\extra\\video\\{file}")
    elif (os.path.splitext(file)[1].lower in docc_ext):
        os.replace(file,f"d:\\DCIM\\Download\\extra\\pdf\\{file}")
    elif (os.path.splitext(file)[1].lower not in image_ext and os.path.splitext(file)[1].lower not in video_ext and os.path.splitext(file)[1].lower not in docc_ext and os.path.isfile(file)):
        os.replace(file,f"d:\\DCIM\\Download\\extra\\image\\{file}")