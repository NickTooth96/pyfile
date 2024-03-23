import os
import datetime

from PIL import Image

__PATH__ = os.getcwd()


def get_list(src=os.getcwd()):
    """returns list of all files in directory

    Args:
        src (_type_): _description_

    Returns:
        list: list of all files in current directory (dest)
    """
    buffer = []
    output = []
    print(">>>",src)
    buffer = os.listdir(src)
    for x in buffer:
        if os.path.isfile(os.path.join(src,x)):
            output.append(x)
    return output

def remove_non_image(dir_list,source_dir):
    output = []
    for file in dir_list:
        try:
            Image.open(os.path.join(source_dir,file))
            output.append(file)
        except:
            pass
    return output

def display_image(list,source_dir):
    length = len(str(len(list))) + 1
    for file in list:
        im = Image.open(os.path.join(source_dir,file))
        exif = im.getexif()
        try:
            t = exif[306]
        except:
            t = os.stat(os.path.join(source_dir,file)).st_mtime 
        idex = str(int(list.index(file))).rjust(length,"0")
        try: 
            date = datetime.datetime.fromtimestamp(t)
        except:
            date = t + " <- NOT USEFUL"

        print(idex,shorten(file,25),date)
        
def display(list,source_dir):
    length = len(str(len(list))) + 1
    for file in list:
        idex = str(int(list.index(file))).rjust(length,"0")
        print(idex,shorten(file,25))

def shorten(str_in,length):
    out = ""    
    if len(str_in) <= length:
        out = str_in.ljust(length - 1, " ")
    else:
        length = int(length/2)
        first_half = str_in[0:length - 3]
        last_half = str_in[len(str_in) - length:len(str_in)]
        out = first_half + "..." + last_half 
    return out