from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import loadSetting
from pynput import keyboard
from ttkwidgets.autocomplete import AutocompleteCombobox

window = Tk()
window.geometry(  '400x490')
window.title(     "POE Lazy Crafter")
window.iconbitmap("./img/icon.ico")
window.config(bg= '#3E3232')
window.attributes("-topmost", True)

CurSettingLabel = Label(window ,text="Currency position setting", font=("Consolas", 12), bg='#3E3232', fg="#A87C7C")
CurSettingLabel.pack(side=TOP, fill=X, padx=2, pady=2)
CurSettingDes1 = Label(window ,text="Red = No seting , Blue = WIP , Green = Setted", font=("Consolas", 8), bg='#3E3232', fg="#A87C7C")
CurSettingDes1.pack(side=TOP, fill=X, padx=2, pady=2)

AlchemyImg      = ImageTk.PhotoImage(Image.open("./img/Alchemy.png").resize((     40, 40)))
AlterationImg   = ImageTk.PhotoImage(Image.open("./img/Alteration.png").resize((  40, 40)))
AugmentationImg = ImageTk.PhotoImage(Image.open("./img/Augmentation.png").resize((40, 40)))
WisdomImg       = ImageTk.PhotoImage(Image.open("./img/Wisdom.png").resize((      40, 40)))
ChiselImg       = ImageTk.PhotoImage(Image.open("./img/Chisel.png").resize((      40, 40)))
ScouringImg     = ImageTk.PhotoImage(Image.open("./img/Scouring.png").resize((    40, 40)))
MapImg          = ImageTk.PhotoImage(Image.open("./img/Map.png").resize((         27, 27)))

#CurrencySettingFrame1
CurrencySettingFrame1 = Frame(window, bg='#3E3232')
AlchemyBtn = Button(     CurrencySettingFrame1, image = AlchemyImg,      bg="#3E3232", height= 40, width=40)
AlterationBtn = Button(  CurrencySettingFrame1, image = AlterationImg,   bg='#3E3232', height= 40, width=40)
AugmentationBtn = Button(CurrencySettingFrame1, image = AugmentationImg, bg='#3E3232', height= 40, width=40)
WisdomBtn = Button(      CurrencySettingFrame1, image = WisdomImg,       bg='#3E3232', height= 40, width=40)
ChiselBtn = Button(      CurrencySettingFrame1, image = ChiselImg,       bg='#3E3232', height= 40, width=40)
ScouringBtn = Button(    CurrencySettingFrame1, image = ScouringImg,     bg='#3E3232', height= 40, width=40)
AlchemyBtn.pack(     side=LEFT, padx=(2,0), pady=2, expand=YES, anchor=CENTER)
AlterationBtn.pack(  side=LEFT, padx=(2,0), pady=2, expand=YES, anchor=CENTER)
AugmentationBtn.pack(side=LEFT, padx=(2,0), pady=2, expand=YES, anchor=CENTER)
WisdomBtn.pack(      side=LEFT, padx=(2,0), pady=2, expand=YES, anchor=CENTER)
ChiselBtn.pack(      side=LEFT, padx=(2,0), pady=2, expand=YES, anchor=CENTER)
ScouringBtn.pack(    side=LEFT, padx=(2,2), pady=2, expand=YES, anchor=CENTER)
CurrencySettingFrame1.pack(side=TOP, fill=X, padx=2, pady=2)

CurSettingDes2 = Label(window , font=("Consolas", 8), bg='#3E3232', fg="#A87C7C")
CurSettingDes2.config(text = "Click set and move mouse to currency.\nThen , press F1 for set position")
CurSettingDes2.pack(side=TOP, fill=X, padx=2, pady=2)

#MapCraftFrame1
MapCraftFrame1 = Frame(window, bg='#3E3232')
MapCraftIcon = Label(MapCraftFrame1 , bg='#3E3232', image=MapImg)
MapCraftLabel = Label(MapCraftFrame1 , bg='#3E3232', text="Map craft", font=("Consolas", 12), fg="#A87C7C")
MapCraftLabel2 = Label(MapCraftFrame1 , bg='#3E3232', text="Load setting :", font=("Consolas", 8), fg="#A87C7C")
SettingListLoadCombo = ttk.Combobox(MapCraftFrame1, width=17)
LoadSaveBtn = Button(MapCraftFrame1,font=("Consolas", 10), bg='#3E3232', fg="#A87C7C", text="Load")
MapCraftIcon.pack(side=LEFT, padx=(2,0), pady=2)
MapCraftLabel.pack(side=LEFT, padx=(2,0), pady=2)
MapCraftLabel2.pack(side=LEFT, padx=(2,0), pady=2)
SettingListLoadCombo.pack(side=LEFT, padx=(2,0), pady=2)
LoadSaveBtn.pack(side=LEFT, padx=(2,2), pady=2)
MapCraftFrame1.pack(side=TOP, fill=X, padx=2, pady=2)
#MapCraftFrame2-5
MapCraftFrame2 = Frame(window, bg='#3E3232')
MapCraftFrame3 = Frame(window, bg='#3E3232')
MapCraftFrame4 = Frame(window, bg='#3E3232')
MapCraftFrame5 = Frame(window, bg='#3E3232')
MapQLabel  = Label(MapCraftFrame2 , text="MAP Quality (Min)       : ", font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
ItemQLabel = Label(MapCraftFrame3 , text="Item Quantity (Min)     : ", font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
MonPkLabel = Label(MapCraftFrame4 , text="Monster Pack Size (Min) : ", font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
MonPkLabel = Label(MapCraftFrame4 , text="Monster Pack Size (Min) : ", font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
MapMoLabel = Label(MapCraftFrame5 , text="MAP Mod void :"           , font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
MapQInput =  Entry(MapCraftFrame2 , font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
ItemQInput = Entry(MapCraftFrame3 , font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
MonPkInput = Entry(MapCraftFrame4 , font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
mapModArray = loadSetting.loadMapModList()
MapMoInput = AutocompleteCombobox(MapCraftFrame5 ,completevalues=mapModArray,width=32)
MapMoAddBtn = Button(MapCraftFrame5,font=("Consolas", 10), bg='#3E3232', fg="#A87C7C", text="Add")
MapQLabel.pack(side=LEFT, padx=(2,0), pady=2)
MapQInput.pack(side=LEFT, padx=(2,2), pady=2, anchor=NE)
ItemQLabel.pack(side=LEFT, padx=(2,0), pady=2)
ItemQInput.pack(side=LEFT, padx=(2,2), pady=2, anchor=NE)
MonPkLabel.pack(side=LEFT, padx=(2,0), pady=2)
MonPkInput.pack(side=LEFT, padx=(2,2), pady=2, anchor=NE)
MapMoLabel.pack(side=LEFT, padx=(2,0), pady=2)
MapMoInput.pack(side=LEFT, padx=(2,0), pady=2)
MapMoAddBtn.pack(side=LEFT, padx=(4,2), pady=2, anchor=NE)
MapCraftFrame2.pack(side=TOP, fill=X, padx=6)
MapCraftFrame3.pack(side=TOP, fill=X, padx=6)
MapCraftFrame4.pack(side=TOP, fill=X, padx=6)
MapCraftFrame5.pack(side=TOP, fill=X, padx=6)

#Map avoid table
MapModTree = ttk.Treeview(window, height=5)
MapModTree["columns"] = ("MAP_MOD")
MapModTree.column("#0", width=5)
MapModTree.heading("#0",      text="No.")
MapModTree.heading("MAP_MOD", text="MAP Mod")
MapModTree.pack(side=TOP, fill=X, padx=6)

MapCraftFrame6 = Frame(window, bg='#3E3232')
MapMoSaveLabel = Label(MapCraftFrame6 , text="Save setting :", font=("Consolas", 10), bg='#3E3232', fg="#A87C7C")
MapMoSaveInput = Entry(MapCraftFrame6 , font=("Consolas", 10), bg='#3E3232', fg="#A87C7C",width=20)
MapMoSaveAddBtn = Button(MapCraftFrame6,font=("Consolas", 10), bg='#3E3232', fg="#A87C7C", text="Save")
MapMoSaveLabel.pack(side=LEFT, padx=(2,0), pady=2)
MapMoSaveInput.pack(side=LEFT, padx=(2,0), pady=2)
MapMoSaveAddBtn.pack(side=LEFT, padx=(4,2), pady=2)
MapCraftFrame6.pack(side=TOP, fill=X, padx=6,anchor=CENTER)

MapCraftDes = Label(window , font=("Consolas", 8), bg='#3E3232', fg="#A87C7C")
MapCraftDes.config(text = "( F2 ) Start craft ,  ( F3 ) Stop craft")
MapCraftDes.pack(side=TOP, fill=X, padx=2, pady=(3,2))

### Logic part
#Load cursetting
currentBtnArray = []
currentBtnArray.append(AlchemyBtn)
currentBtnArray.append(AlterationBtn)
currentBtnArray.append(AugmentationBtn)
currentBtnArray.append(WisdomBtn)
currentBtnArray.append(ChiselBtn)
currentBtnArray.append(ScouringBtn)
def setCurPos():
    settingIndex = -1
    for i in range(len(currentBtnArray)):
        bg_color = currentBtnArray[i].cget("background")
        if bg_color == "Blue":
            settingIndex = i
    if settingIndex == -1:
        return False
    mouse_x = window.winfo_pointerx()
    mouse_y = window.winfo_pointery()
    loadSetting.saveCurPos(settingIndex,mouse_x,mouse_y)
    reloadCurSetting()
def reloadCurSetting():
    returnArray = loadSetting.loadCurSetting()
    for i in range(len(returnArray)) :
        if returnArray[i] == 1:
            currentBtnArray[i].config(bg="Green")
        else :
            currentBtnArray[i].config(bg="Red")
reloadCurSetting()
#Blind onclick
def Curbutton_clicked(event):
    button = event.widget
    reloadCurSetting()
    button.config(bg="Blue")
for i in currentBtnArray:
    i.bind("<Button-1>", Curbutton_clicked)


#SaveMapCraftSetting
defaultMapSetting = ""
def reloadMapCraftSettingList():
    MapCraftListArray = loadSetting.getListMapCraftConfig()
    SettingListLoadCombo['values'] = tuple(MapCraftListArray)
    SettingListLoadCombo.set(defaultMapSetting)
def saveMapCraftConfig(event):
    global defaultMapSetting
    configName = MapMoSaveInput.get()
    MapQ  = MapQInput.get()
    ItemQ = ItemQInput.get()
    MonPk = MonPkInput.get()
    mapModList = []
    items = MapModTree.get_children()
    for item in items:
        data = MapModTree.item(item, "values")
        mapModList.append(data[0])
    loadSetting.saveMapCraft(configName,MapQ,ItemQ,MonPk,mapModList)
    defaultMapSetting = configName
    reloadMapCraftSettingList()
def loadMapCraftConfig(event):
    configSelect = SettingListLoadCombo.get()
    MapQ,ItemQ,MonPk,mapModList = loadSetting.loadMapCraft(configSelect)
    MapQInput.delete(0,  END)
    ItemQInput.delete(0, END)
    MonPkInput.delete(0, END)
    MapQInput.insert(0, MapQ)
    ItemQInput.insert(0, ItemQ)
    MonPkInput.insert(0, MonPk)
    for item in MapModTree.get_children():
        MapModTree.delete(item)
    for i in range(len(mapModList)):
        MapModTree.insert("", END, text=str(i+1), values=(mapModList[i],""))
    MapMoSaveInput.delete(0, END)
    MapMoSaveInput.insert(0, configSelect)
def mapModAddToTable(event):
    mapModTmp = MapMoInput.get()
    count = 1
    for item in MapModTree.get_children():
        count+=1
    MapModTree.insert("", END, text=str(count), values=(mapModTmp,""))
reloadMapCraftSettingList()
MapMoSaveAddBtn.bind("<Button-1>", saveMapCraftConfig)
LoadSaveBtn.bind("<Button-1>", loadMapCraftConfig)
MapMoAddBtn.bind("<Button-1>", mapModAddToTable)

def delete_selected_item(event):
    selected_item = MapModTree.focus()  # Get the selected item
    data = []
    if selected_item:  # If an item is selected
        MapModTree.delete(selected_item)  # Delete the selected item
    for item in MapModTree.get_children():
        data.append(MapModTree.item(item, "values")[0])
        MapModTree.delete(item)
    for i in range(len(data)): 
        MapModTree.insert("", END, text=str(i+1), values=(data[i],""))
MapModTree.bind("<Delete>", delete_selected_item)


def autoCompMapMod(event):
    selected_item = event.widget.get()
MapMoInput.bind("<<ComboboxSelected>>", autoCompMapMod)

def saveMapCraftBeforeRun():
    configName = "jcko12316#21ncnuw"
    MapQ  = MapQInput.get()
    ItemQ = ItemQInput.get()
    MonPk = MonPkInput.get()
    mapModList = []
    items = MapModTree.get_children()
    for item in items:
        data = MapModTree.item(item, "values")
        mapModList.append(data[0])
    loadSetting.saveMapCraft(configName,MapQ,ItemQ,MonPk,mapModList)

import subprocess

def on_press(key):
    global MapCraftProcess
    if key == keyboard.Key.f1:
        setCurPos()
    if key == keyboard.Key.f2:
        try:
            MapCraftProcess.terminate()
        except:
            pass
        saveMapCraftBeforeRun()
        MapCraftProcess = subprocess.Popen(["pythonw", "./src/craftAgent.py"])
        
    if key == keyboard.Key.f3:
        MapCraftProcess.terminate()
listener = keyboard.Listener(on_press=on_press)
listener.start()

def winclose():
    try:
            MapCraftProcess.terminate()
    except:
            pass
    window.destroy()

window.protocol("WM_DELETE_WINDOW", winclose)

mainloop()