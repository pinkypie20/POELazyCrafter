import json
import os
currencyList = []

currencyList.append("Alchemy")
currencyList.append("Alteration")
currencyList.append("Augmentation")
currencyList.append("Wisdom")
currencyList.append("Chisel")
currencyList.append("Scouring")
filename = "./config/curPos.json"
def loadCurSetting():
    try:
        returnArray = []
        with open(filename, 'r') as f:
            json_data = f.read()
            data_dict = json.loads(json_data)
        for i in currencyList:
            if data_dict[i] != "":
                returnArray.append(1)
            else :
                returnArray.append(0)
        return returnArray
    except:
        data_dict = {}
        for i in currencyList:
            data_dict[i] = ""
        with open(filename, 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
        return [0,0,0,0,0,0]
def loadMapModList():
    with open('./config/map.txt', 'r') as file:
        mapModArray = file.readlines()
    for i in range(len(mapModArray)):
        mapModArray[i] = mapModArray[i].replace("\n","")
    return mapModArray
def saveCurPos(index,x,y):
    with open(filename, 'r') as f:
        json_data = f.read()
        data_dict = json.loads(json_data)
    data_dict[currencyList[index]] = str(x)+","+str(y)
    with open(filename, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
    return True
def saveMapCraft(configName,MapQ,ItemQ,MonPk,mapModList):
    if configName == "jcko12316#21ncnuw":
        fileNameMapConfig = "./config/mapcraftrunning.json"
    else:
        fileNameMapConfig = "./config/user/"+configName+".json"
    configDict = {}
    configDict['MapQ'] = MapQ
    configDict['ItemQ'] = ItemQ
    configDict['MonPk'] = MonPk
    configDict['mapModList'] = mapModList
    with open(fileNameMapConfig, 'w') as json_file:
        json.dump(configDict, json_file, indent=4)
def getListMapCraftConfig():
    returnArray = []
    files = os.listdir("./config/user")
    for file in files:
        returnArray.append(file.split(".")[0])
    return returnArray
def loadMapCraft(configSelect):
    fileNameMapConfig = "./config/user/"+configSelect+".json"
    with open(fileNameMapConfig, 'r') as f:
        json_data = f.read()
        data_dict = json.loads(json_data)
    return data_dict['MapQ'],data_dict['ItemQ'],data_dict['MonPk'],data_dict['mapModList']