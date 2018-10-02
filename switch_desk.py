import os
index = 4
dir = os.listdir("/Users/KevinGao/Desktop/switch.app/desktop_images/")
content = []
with open(__file__, "r") as f:
    for line in f:
        content.append(line)
with open(__file__, "w") as f:
    content[1] = "index = {n}\n".format(n = (index+1) % len(dir))
    for i in range(len(content)):
        f.write(content[i])

cmd = """osascript -e 'tell Application "Finder"' -e 'set the desktop picture to {"Users:KevinGao:Desktop:switch.app:desktop_images:""" + dir[index] + """"} as alias' -e 'end tell'"""

def change_pic():
    os.system(cmd)
change_pic() 

