import datetime
import os
import shutil
import sys
import getopt
# from PIL import Image


__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.path.dirname(os.path.abspath(__file__))

FAILURES = 0
MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}


### Class


class Sorter:

    source_dir = ""
    dest_dir = ""
    dest_structure = {}
    dir_contents = []

    def __init__(self,source,destination):
        self.source_dir = source
        self.dest_dir = destination
        self.dest_structure = {}
        self.dir_contents = self.get_list()
    
    def get_list(self):
        buffer = []
        output = []
        buffer = os.listdir(self.source_dir)
        for x in buffer:
            if os.path.isfile(os.path.join(self.source_dir,x)):
                output.append(x)
        return output
    
    def sort(self):
        years = []
        im = "" 

        for x in self.dir_contents: 

            try:
                im = Image.open(os.path.join(self.source_dir,x))
                exif = im.getexif()
                t = exif[306]               

                try:
                    im = Image.open(os.path.join(self.source_dir,x))
                    exif = im.getexif()
                    t = exif[306]  
                    success = True      
                except:
                    success = False
                if success:
                    try:
                        buffer = datetime.datetime.strptime(t,'%Y:%m:%d %H:%M:%S')            
                        t = datetime.datetime.timestamp(buffer)                
                    except:
                        t = t 
                        FAILURES += 1        
            except:
                t = os.stat(os.path.join(self.source_dir,x)).st_mtime
            im.close()

            month = datetime.datetime.fromtimestamp(t).strftime("%m")
            year = datetime.datetime.fromtimestamp(t).strftime("%y")
            name = "20" + year    
            dest = os.path.join(self.dest_dir,name)
            if os.path.exists(dest):
                final_dest = os.path.join(dest,MONTHS[month])
                if os.path.exists(final_dest):
                    shutil.move(os.path.join(self.source_dir,x),final_dest)
                    pass
                else:
                    os.makedirs(os.path.join(dest,MONTHS[month]))
                    shutil.move(os.path.join(self.source_dir,x),final_dest)
            else:
                os.makedirs(os.path.join(dest,MONTHS[month]))
                shutil.move(os.path.join(self.source_dir,x),os.path.join(dest,MONTHS[month]))

    def unsort(self):
        file_count = 0
        buffer = os.listdir(self.source_dir)
       
        for x in buffer:   
            path_0 = os.path.join(self.source_dir,x)          
            if os.path.isdir(path_0) and "20" in x:
                buffer = os.listdir(path_0)   

                for x in buffer: 
                    path_1 = os.path.join(path_0,x) 
                    if os.path.isdir(path_1) and x in MONTHS.values():
                        buffer = os.listdir(path_1) 

                        for x in buffer:
                            path_2 = os.path.join(path_1,x)
                            if os.path.isfile(path_2):
                                file_count += 1
                                shutil.move(path_2,self.source_dir)
                                
                            else:
                                print("NONFILE FOUND")
                # print(path_0)
                shutil.rmtree(path_0)

            
                








