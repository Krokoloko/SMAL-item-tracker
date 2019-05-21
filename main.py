import json
import sys
file = open("save.json", "r")

try:
    context = file.read()
    saveData = json.loads(file)
except:
    saveData = []

try:
    indexCount = 0
    for i in saveData:
        if i["index"] > indexCount:
            indexCount = i["index"]
except:
    indexCount = 0

file.close()
commandDict = []

def about():
    print("This python script helps you to keep track on the items you have picked up.")

def help_me():
    print("commands\n")
    for i in commandDict:
        print("\'command name\': {} \n\'description\': {}\n".format(i["command"],i["description"]))

def close():
    sys.exit(0)

def save_list():
    file = open("save.json", "w")
    file.write(json.dumps(saveData))

def add_item():
    global indexCount
    item = input("What item did you find? \n")
    location = input("Where did you find it? \n")
    picked_up = input("Did you pick it up? \n")

    if "y" in picked_up.lower():
        picked_up = "yes"
    if "n" in picked_up.lower():
        picked_up = "no"

    indexCount += 1
    saveData.append({"index": indexCount, "item": item, "location": location, "picked_up": picked_up})

def delete_item():
    index = input("Give the index of the item you want to delete: ")

def show_list():
    if len(saveData) == 0:
        print("list is empty, find some items and \'add\' them")
    else:
        for i in saveData:
            print("\'index\':{}, \'item\':{}, \'location\':{}, \'picked_up\':{}".format(i["index"],i["item"],i["location"],i["picked_up"]))

commandDict = [
    {"command": "about", "description": "A description about this program.", "function": about},
    {"command": "help", "description": "Prints all commands and usage.", "function": help_me},
    {"command": "add", "description": "Adds a new item to the list.", "function": add_item},
    {"command": "delete", "description": "Deletes item from the list based on its index.", "function": delete_item},
    {"command": "list", "description": "Shows the list of items that you have been tracking.", "function": show_list},
    {"command": "savelist", "description": "Saves the list you have been tracking.", "function": save_list},
    {"command": "close", "description": "Exits and terminates the program", "function": close}
]

while True:
    command = input("Type Command here: ")
    for cmd in commandDict:
        if command.lower() == cmd["command"]:
            cmd["function"]()
