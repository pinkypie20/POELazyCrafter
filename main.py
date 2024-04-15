import tkinter as tk
import tkinter.font
import pyglet
import json
from mapcraft import mapCraft
import threading

nowSettingCurIndex = -1
nowSettingCurButton = -1
curPositionNameArray = ["Wisdom","Alchemy","Scouring","Chisel"]
posDisArraylable = []
curPostionSettingDict = {}
def reloadSetting():
    global curPostionSettingDict
    try:
        with open('pos_config.json') as json_file:
            curPostionSettingDict = json.load(json_file)
    except:
        return False
    for i in range(len(posDisArraylable)):
        try:
            x_tmp = curPostionSettingDict[curPositionNameArray[i]]["x"]
            y_tmp = curPostionSettingDict[curPositionNameArray[i]]["y"]
            text_show = "("+str(x_tmp)+","+str(y_tmp)+")"
            posDisArraylable[i].config(text=text_show)
        except:
            pass
def setPos(arg):
    global nowSettingCurIndex
    global nowSettingCurButton
    global curPostionSettingDict
    if nowSettingCurIndex == -1:
        return False
    mouse_x = app.winfo_pointerx()
    mouse_y = app.winfo_pointery()
    curPostionSettingDict[curPositionNameArray[nowSettingCurIndex]] = {"x":mouse_x,"y":mouse_y}
    nowSettingCurButton.config(bg="#49243E")
    nowSettingCurButton.config(fg="#DBAFA0")
    nowSettingCurButton.config(text="Click for set")
    nowSettingCurIndex = -1
    nowSettingCurButton = -1
    with open('pos_config.json', 'w', encoding='utf-8') as f:
        json.dump(curPostionSettingDict, f, ensure_ascii=False, indent=4)
    reloadSetting()
def setPosActive(btnItem,curIndex):
    global nowSettingCurIndex
    global nowSettingCurButton
    if nowSettingCurIndex != -1:
        return False
    btnItem.config(bg="#BB8493")
    btnItem.config(fg="#49243E")
    btnItem.config(text="(F1) For set ")
    nowSettingCurIndex = curIndex
    nowSettingCurButton = btnItem
def mapCraftCaller(arg):
    print(arg)
    thread = threading.Thread(target=mapCraft)
    thread.start()
app = tk.Tk()
app.geometry("300x160")
app.iconbitmap(r'icon.ico')
app.title("POE Lazy Crafter")
app.configure(bg="#49243E")
app.resizable(False, False)
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file("Kanit-Regular.ttf")
app.attributes("-topmost", True)

label = tk.Label(app, text=" Currency position", bg="#49243E", fg="#DBAFA0")
label.config(font=("Kanit", 16))
label.pack(side=tk.TOP, fill=tk.X)

curFrame = tk.Frame(master=app, bg="#49243E")
curFrame.grid_columnconfigure(0, weight=1)
curFrame.grid_columnconfigure(1, weight=1)
curFrame.grid_columnconfigure(2, weight=1)
curFrame.grid_columnconfigure(3, weight=1)

label11 = tk.Label(curFrame, text="Wisdom  ",   bg="#49243E", fg="#DBAFA0")
label12 = tk.Label(curFrame, text="Alchemy ",  bg="#49243E", fg="#DBAFA0")
label13 = tk.Label(curFrame, text="Scouring", bg="#49243E", fg="#DBAFA0")
label14 = tk.Label(curFrame, text="Chisel  ",   bg="#49243E", fg="#DBAFA0")
label11.config(font=("Kanit", 10))
label12.config(font=("Kanit", 10))
label13.config(font=("Kanit", 10))
label14.config(font=("Kanit", 10))
label11.grid(sticky="news",row=0,column=0)
label12.grid(sticky="news",row=0,column=1)
label13.grid(sticky="news",row=0,column=2)
label14.grid(sticky="news",row=0,column=3)

label21 = tk.Label(curFrame, text="not set",   bg="#49243E", fg="#DBAFA0")
label22 = tk.Label(curFrame, text="not set",  bg="#49243E", fg="#DBAFA0")
label23 = tk.Label(curFrame, text="not set", bg="#49243E", fg="#DBAFA0")
label24 = tk.Label(curFrame, text="not set",   bg="#49243E", fg="#DBAFA0")
label21.config(font=("Kanit", 7))
label22.config(font=("Kanit", 7))
label23.config(font=("Kanit", 7))
label24.config(font=("Kanit", 7))
label21.grid(sticky="news",row=1,column=0)
label22.grid(sticky="news",row=1,column=1)
label23.grid(sticky="news",row=1,column=2)
label24.grid(sticky="news",row=1,column=3)
posDisArraylable.append(label21)
posDisArraylable.append(label22)
posDisArraylable.append(label23)
posDisArraylable.append(label24)


button31 = tk.Button(curFrame,text="Click for set",bg="#49243E", fg="#DBAFA0")
button32 = tk.Button(curFrame,text="Click for set",bg="#49243E", fg="#DBAFA0")
button33 = tk.Button(curFrame,text="Click for set",bg="#49243E", fg="#DBAFA0")
button34 = tk.Button(curFrame,text="Click for set",bg="#49243E", fg="#DBAFA0")
button31.config(command = lambda: setPosActive(button31,0))
button32.config(command = lambda: setPosActive(button32,1))
button33.config(command = lambda: setPosActive(button33,2))
button34.config(command = lambda: setPosActive(button34,3))
button31.config(font=("Kanit", 7))
button32.config(font=("Kanit", 7))
button33.config(font=("Kanit", 7))
button34.config(font=("Kanit", 7))
button31.grid(row=2,column=0)
button32.grid(row=2,column=1)
button33.grid(row=2,column=2)
button34.grid(row=2,column=3)

curFrame.pack(side=tk.TOP,fill=tk.X)

label = tk.Label(app, text="MAP Craft ( F2 )", bg="#49243E", fg="#DBAFA0")
label.config(font=("Kanit", 16))
label.pack(side=tk.TOP, fill=tk.X)

reloadSetting()
app.bind_class("all","<F1>", setPos )
app.bind_class("all","<F2>", mapCraftCaller )
app.mainloop()