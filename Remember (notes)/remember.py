import os
from colorama import Fore


class Remember:
    def __init__(self):
        self.cli()
        
    
    
    def cli(self):
        tool = input(f"1. Write \n2. Read \n3. Open\nSelect tool : ")
        
        if tool == "1":
            self.write()
            
        elif tool == "2":
            self.read()
        
        elif tool == "3":
            self.openChategory()
    
    def write(self):
        category = input(f"Category (? for list) : ")
        
        
            
        if category == "?" or category == "؟":
            for file in os.listdir(f"{os.getcwd()}/Archives"):
                if os.path.isfile(f"{os.getcwd()}/Archives/{file}"):
                    print(file)

            self.write()
            
        elif category == "":
            category = "onFly"
        

        while True:
            text = input(f">> ")
        
            if text == "":
                quit()
            
            else:
                with open(f"./Archives/{category+'.txt'}", "a") as file:
                    file.write(
                        text+"\n"
                    )
                print("Added!")
            

    def read(self):
        category = input(f"Category (? for list) : ")

        if category == "?" or category == "؟":
            for file in os.listdir(f"{os.getcwd()}/Archives"):
                if os.path.isfile(f"{os.getcwd()}/Archives/{file}"):
                    print(file)
            
            self.read()

        elif category == "":
            category = "onFly"

        num = input("1. Head    2. Read all\nSelect : ")
        
        with open(f"./Archives/{category+'.txt'}", "r") as file:
            if num == "1":
                print("".join(file.readlines()[-5:]))
                wait = input("Enter to quit >> ")
                quit()
                
            elif num == "2":
                print("".join(file.readlines()))
                wait = input("Enter to quit >> ")
                quit()
        
    def openChategory(self):
        category = input(f"Category (? for list) : ")

        if category == "?" or category == "؟":
            for file in os.listdir(f"{os.getcwd()}/Archives"):
                if os.path.isfile(f"{os.getcwd()}/Archives/{file}"):
                    print(file)
            
            self.openChategory()

        elif category == "":
            category = "onFly"


        try:
            os.startfile(f"{os.getcwd()}/Archives/{category+'.txt'}")
        except:
            print("error, try again...")
            self.openChategory()
        
        
rem = Remember()

