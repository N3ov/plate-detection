import tr
import re
import os
import argparse
import json

class PlateRecognize():

    def __init__(self):
        self.path = opt.path


    def os_path(self):
        dir_list = os.listdir(self.path)
        # print(dir_list)
        dirs = []
        for i in dir_list:
            dirs.append(i)

        return dirs

    def plate_recognize(self):
        
        dirs = PlateRecognize().os_path()
        # print(dirs)

        plate_list = {}
        for filename in dirs:
            pth = self.path + os.sep + filename
         
            plate = tr.recognize(pth)[0].upper()
            last_num = re.findall(r"[0-9A-Z]{4}$", plate)

            if plate[:3].isalpha():
                char = []
                
                for i in last_num[0]:
                    if i == "I":
                        char.append("1") 
                    elif i == "O":
                        char.append("0")        
                    elif i == "Z":
                        char.append("2")
                    elif i == "J":
                        char.append("1")
                    elif i == "L":
                        char.append("2")

                    else:
                        char.append(i)
            #  print(char) 
                
                real_plate = []
                for i in plate[:3]:
                    real_plate.append(i)
               
                real_plate = real_plate + char
                plate_list.update({filename : real_plate})
                
            else: 
            # x = plate[:2].isalpha()
            # print(x)
                old_plate = []
                for i in plate:
                    if i != "-":
                        old_plate.append(i)
                plate_list.update({filename : old_plate})

        return plate_list

    def result_to_json(self):
        
        getDict = PlateRecognize().plate_recognize()
        result_json = json.dumps(getDict)

        return result_json
 
if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("--path", "-p", type=str ,default="/home/ubuntu/Desktop/result", help="pic path")
    opt = parse.parse_args()
    print(opt)

    pr = PlateRecognize()
    print(pr.result_to_json())

