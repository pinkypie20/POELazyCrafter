import pyautogui
from pynput import keyboard
import pyperclip
import time
import json

ban_list = "ban_map_mod.txt"
with open('ban_map_mod.txt', 'r') as file:
    ban_list = file.readlines()
ban_list = [line.strip() for line in ban_list]

curPostionSettingDict = {}

with open('pos_config.json') as json_file:
    curPostionSettingDict = json.load(json_file)
wisdom_pos = [curPostionSettingDict["Wisdom"]["x"],curPostionSettingDict["Wisdom"]["y"]]
Scouring_pos = [curPostionSettingDict["Scouring"]["x"],curPostionSettingDict["Scouring"]["y"]]
Chisel_pos = [curPostionSettingDict["Chisel"]["x"],curPostionSettingDict["Chisel"]["y"]]
Alchemy_pos = [curPostionSettingDict["Alchemy"]["x"],curPostionSettingDict["Alchemy"]["y"]]

PackSizeTarget = 20
QuantityTarget = 80

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
    for ban_mod in ban_list:
        if ban_mod.lower() in map_mod.lower():
            return False
    return True

def mapCraft():
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
        print(int((qNow/5)//1),4-int((qNow/5)//1))
        if qNow < 20:
            if "Rarity: Normal" not in map_mod:
                usingOrb(Scouring_pos,current_mouse_position)
            for i in range(4-int((qNow/5)//1)):
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
        else :
            usingOrb(Scouring_pos,current_mouse_position)
            usingOrb(Alchemy_pos,current_mouse_position)