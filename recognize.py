import tr
import re
import argparse

def plate_recognize():
    path = opt.path
    plate = tr.recognize(path)[0].upper()
    print(plate)
    last_num = re.findall(r"[0-9A-Z]{4}$", plate)
    #print(plate[:3])
    #print(re.findall(r"[0-9]{4}$", plate))
    # print(type(last_num))
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
        print(real_plate)
        
    else: 
    # x = plate[:2].isalpha()
    # print(x)
        old_plate = []
        for i in plate:
            if i != "-":
                old_plate.append(i)

        print(old_plate)


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("--path", "-p", type=str ,default="/home/ubuntu/Desktop/result/plate.jpg", help="pic path")

    opt = parse.parse_args()
    print(opt)
    plate_recognize()
# path = "/home/ubuntu/Desktop/result/plate.jpg"
#path = "/home/ubuntu/Desktop/data/0013.jpg"
