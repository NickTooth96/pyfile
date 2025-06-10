import datetime
import os
import shutil
from statistics import mean
import sys
import getopt
# from PIL import Image


__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.path.dirname(os.path.abspath(__file__))

BLACKLIST = ['97TH', 'REGIMENTAL', 'STRING', 'BAND', '-', '', '(Civil', 'War', 'Music)']
GRAYLIST = ['THE', 'A', 'AN','OF','ON','AND','TO', 'AND']


### Class


class Pseudoname():
    
    source_dir = ""
    dest_dir = ""
    dest_structure = {}
    dir_contents = []

    def __init__(self,source,destination):
        self.source_dir = source
        self.dest_dir = destination
        self.dest_structure = {}
        self.dir_contents = self.get_list()
    
    def rename(self):
        for x in self.dir_contents:
            title = ""
            print("\n",x)
            parsed_x = x.split()
            for i in range(len(parsed_x)):
                if parsed_x[i].upper() not in BLACKLIST and parsed_x[i].find("-") != -1:
                    split = parsed_x[i].split("-") # may change to try to split by each element of blacklist to make config file easier
                    parsed_x.remove(parsed_x[i])
                    # print(parsed_x)
                    for x in split:
                        parsed_x.insert(i,x)
                if parsed_x[i].upper() not in GRAYLIST:
                    parsed_x[i] = parsed_x[i].capitalize()
            parsed_x = self.remove(parsed_x)
            for e in parsed_x:
                title += e + " "
            print("|___",title)
    
    def remove(self,list):
        blacklist = BLACKLIST.copy()
        for i in range(len(list)-1):
            i = 0
            for y in blacklist:
                if list[i].upper() == y:
                    blacklist.remove(y)
                    del list[i]
                    break
                else:
                    mp = self.reasonable_match(list[i],y)
                    if mp >= 98 and mp <= 101:
                        blacklist.remove(y)
                        del list[i]
                    i += 1
        return list

    def reasonable_match(self,key,remove):
        i = 0
        match_percent =  0
        total_percent = 0
        key = key.upper()
        percent_list = []

        if len(key) == 0 or len(remove) == 0:
            return 0
        
        length_percent = len(key) / len(remove)
        shortest = len(key)
        longest = len(remove)

        for x in remove:
            all_not_alpha = 0
            if x.isalpha():
                all_not_alpha += 1
        if all_not_alpha == 0:
            return 0.0
        if len(remove) < shortest:
            shortest = len(remove)
            longest = len(key)
        else:
            # print(longest,len(key))
            key = key.ljust(longest,'*')
            # for i in range(len(key),longest):
            #     remove += '*'
            # print(key,remove)
            for i in range(longest):
                if key[i] == remove[i]:
                    match_percent += 1
                    # print(match_percent)
        match_percent = match_percent / longest
        percent_list.append(match_percent)
        percent_list.append(length_percent)
        total_percent = round(mean(percent_list)*100,2)
        return total_percent

def get_list(source: str) -> list:
    output = []
    buffer = os.listdir(os.path.expanduser(source))
    file_count = 0
    for x in buffer:
        if os.path.isfile(os.path.join(source,x)):
            output.append(x)
            file_count += 1
    print("Source Directory contains ",file_count,"files.")
    return output
    
def _name_list_from_file(filepath):
    out = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
    for line in lines:
        out.append(str(line))
    return out

def _process_file_list(titles: list) -> list:
    out = []
    for title in titles:
        buffer = {}
        title = title.strip()
        filename, ext = os.path.splitext(title)
        filename = _remove_blacklist(filename)
        rename = f"{_make_title(filename)}{ext}"
        # print(title,filename,ext,rename)
        buffer["from"] = title
        buffer["to"] = rename
        buffer["filename"] = filename
        buffer["extention"] = ext
        out.append(buffer)
    return out

def _remove_blacklist(filename: str) -> str:
    out = filename
    tmp = filename.split(" ")
    for x in tmp:
        if x.upper() in BLACKLIST:
            out = out.replace(str(x),"")
    out = out.strip()
    if '-' in out:
        out = out.replace('-', ' ').strip()
        out =  _remove_blacklist(out)
    return out.strip()

def _make_title(filename: str) -> str:
    out = ""
    tmp = filename.split()
    for word in tmp:
        if word.upper() not in GRAYLIST:
            out += f"{word[0].upper()}{word[1:]} "
        else:
            out += f"{word} "
    out = f"{out[0].upper()}{out[1:]}"            
    return out.strip()


titles = _name_list_from_file('/Users/nicktoothaker/Documents/short_97reg.txt')
map = _process_file_list(titles)

# other_titles = get_list('.')
# other_map = _process_file_list(other_titles)

for m in map:
    print(m['to'])



