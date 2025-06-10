import datetime
import os
import shutil
from statistics import mean
import argparse


__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.path.dirname(os.path.abspath(__file__))

BLACKLIST = ['97TH', 'REGIMENTAL', 'STRING', 'BAND', '-', '', '(CIVIL', 'WAR', 'MUSIC)']
GRAYLIST = ['THE', 'A', 'AN','OF','ON','AND','TO', 'AND']



### Main



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
    
def name_list_from_file(filepath):
    out = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
    for line in lines:
        out.append(str(line))
    return out

def process_file_list(titles: list) -> list:
    out = []
    for title in titles:
        buffer = {}
        title = title.strip()
        filename, ext = os.path.splitext(title)
        filename = remove_blacklist(filename)
        rename = f"{make_title(filename)}{ext}"
        buffer["from"] = title
        buffer["to"] = rename
        buffer["filename"] = filename
        buffer["extention"] = ext
        out.append(buffer)
    return out

def remove_blacklist(filename: str) -> str:
    out = filename
    tmp = filename.split(" ")
    for x in tmp:
        if x.upper() in BLACKLIST:
            out = out.replace(str(x),"")
    out = out.strip()
    if '-' in out:
        out = out.replace('-', ' ').strip()
        out =  remove_blacklist(out)
    return out.strip()

def make_title(filename: str) -> str:
    out = ""
    tmp = filename.split()
    for word in tmp:
        if word.upper() not in GRAYLIST:
            out += f"{word[0].upper()}{word[1:]} "
        else:
            out += f"{word} "
    out = f"{out[0].upper()}{out[1:]}"            
    return out.strip()

def rename(file_list: dict):
    for file in file_list:
        process = f"RENAMING: {file["from"]} -> {file["to"]}"
        cmd_rename = f'mv "{file["from"]}" "{file["to"]}"'
        print(cmd_rename)
        os.system(f'mv "{file["from"]}" "{file["to"]}"')

### Main

def rename_files(source):
    file_list = get_list(source)
    file_map = process_file_list(file_list)
    rename(file_map)


