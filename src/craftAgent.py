import pyautogui
from pynput import keyboard
import pyperclip
import time
import json

with open('./config/mapcraftrunning.json', 'r') as f:
    json_data = f.read()
    mapCraftDict = json.loads(json_data)
with open('./config/curPos.json', 'r') as f:
    json_data = f.read()
    curPosDict = json.loads(json_data)
ban_list = mapCraftDict['mapModList']

wisdom_pos   = [int(curPosDict['Wisdom'  ].split(",")[0]),int(curPosDict['Wisdom'  ].split(",")[1])]
Scouring_pos = [int(curPosDict['Scouring'].split(",")[0]),int(curPosDict['Scouring'].split(",")[1])]
Chisel_pos   = [int(curPosDict['Chisel'  ].split(",")[0]),int(curPosDict['Chisel'  ].split(",")[1])]
Alchemy_pos  = [int(curPosDict['Alchemy' ].split(",")[0]),int(curPosDict['Alchemy' ].split(",")[1])]


PackSizeTarget = int(mapCraftDict['MonPk'])
QuantityTarget = int(mapCraftDict['ItemQ'])
mapQTarget     = int(mapCraftDict['MapQ'])


def usingOrb(orbType,currentPosition):
    pyautogui.moveTo(x=orbType[0], y=orbType[1])
    time.sleep(0.0001)
    pyautogui.rightClick()
    time.sleep(0.0001)
    pyautogui.moveTo(x=currentPosition.x, y=currentPosition.y)
    time.sleep(0.0001)
    pyautogui.click()
    time.sleep(0.0001)
def checkMapMod(map_mod):
    map_mod_list = map_mod.split("\r\n--------\r\n")[-2].split("\r\n")
    for ban_mod in ban_list:
        for mapModLine in map_mod_list:
            ban_mod_split = ban_mod.split("#")
            match_count = 0
            for k in ban_mod_split:
                if k.lower() in mapModLine.lower():
                    match_count+=1
            if match_count == len(ban_mod_split):
                return False
    return True
current_mouse_position = pyautogui.position()
pyautogui.hotkey('ctrl', 'c')
map_mod = pyperclip.paste()
if "Unidentified" in map_mod:
    usingOrb(wisdom_pos,current_mouse_position)
pyautogui.hotkey('ctrl', 'c')
map_mod = pyperclip.paste()
if "Quality: +" not in map_mod:
    if "Rarity: Normal" not in map_mod:
        usingOrb(Scouring_pos,current_mouse_position)
    for i in range(4):
        usingOrb(Chisel_pos,current_mouse_position)
else:
    qNow = int(map_mod.split("Quality: +")[1].split("%")[0])
    if qNow < mapQTarget:
        if "Rarity: Normal" not in map_mod:
            usingOrb(Scouring_pos,current_mouse_position)
        for i in range(int(mapQTarget/5)+1-int((qNow/5)//1)):
            usingOrb(Chisel_pos,current_mouse_position)
stop_flg = True
while stop_flg:
    cond_count = 0
    pyautogui.hotkey('ctrl', 'c')
    map_mod = pyperclip.paste()
    packSize = 0
    Quantity = 0
    if "Monster Pack Size: +" in map_mod:
        packSize = int(map_mod.split("Monster Pack Size: +")[1].split("%")[0])
    if "Item Quantity: +" in map_mod:
        Quantity = int(map_mod.split("Item Quantity: +")[1].split("%")[0])
    if packSize >= PackSizeTarget:
        cond_count+=1
    if Quantity >= QuantityTarget:
        cond_count+=1
    if checkMapMod(map_mod):
        cond_count+=1
    if cond_count == 3:
        stop_flg = False
        print('\a')
    else :
        usingOrb(Scouring_pos,current_mouse_position)
        usingOrb(Alchemy_pos,current_mouse_position)