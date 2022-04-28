import os
import platform
import urllib.request
import requests
import logging 
import threading

class Setup:
    Add_Logo_Link = "https://cdn-icons-png.flaticon.com/512/992/992651.png"
    Admin_Logo_Link = "https://cdn-icons-png.flaticon.com/512/2099/2099058.png"
    Delete_Logo_Link = "https://cdn-icons-png.flaticon.com/512/3096/3096673.png"
    Expense_Logo_Link = "https://cdn-icons-png.flaticon.com/512/61/61584.png"
    Eye_Logo_Link = "https://cdn-icons-png.flaticon.com/512/159/159604.png"
    Information_Logo_Link = "https://cdn-icons-png.flaticon.com/512/1/1176.png"
    Graph_Icon_Link = "https://cdn-icons-png.flaticon.com/512/3121/3121571.png"
    Login_Icon_Link = "https://cdn-icons-png.flaticon.com/512/126/126486.png"
    Main_Logo_Link = "https://cdn-icons-png.flaticon.com/512/2/2144.png"
    New_User_Logo_Link = "https://cdn1.iconfinder.com/data/icons/avatar-1-2/512/Add_User1-512.png"
    Wrong_Logo_Link = "https://cdn-icons-png.flaticon.com/512/1828/1828665.png"
    Mod_Logo_Link = "https://cdn-icons-png.flaticon.com/512/61/61456.png"
    Export_Logo_Link = "https://cdn-icons-png.flaticon.com/512/151/151900.png"
    Transfer_Logo_Link = "https://cdn-icons-png.flaticon.com/512/876/876784.png"
    Warning_Logo_Link = "https://cdn-icons-png.flaticon.com/512/159/159469.png"
    Stats_Logo_Link = "https://cdn-icons-png.flaticon.com/512/876/876171.png"

    Next_Logo_Link = "https://cdn-icons-png.flaticon.com/512/318/318476.png"
    Menu_Logo_Link = "https://cdn-icons-png.flaticon.com/512/56/56763.png"
    Exit_Logo_Link = "https://cdn-icons-png.flaticon.com/512/1286/1286853.png"

    def __init__(self):
        self.root = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker"
        
        if self.get_os() == "Windows":
            self.dirs()
            thread1 = threading.Thread(target=self.download(), args=(None,))
            thread2 = threading.Thread(target=self.create_log(), args=(None,))

            thread1.start()
            thread2.start()

        else: 
            raise OSError("[!] Unsupported OS")

    
    def dirs(self) -> None:
        if self.check(self.root) == False:
            os.chdir(f"C:/Users/{os.getlogin()}/AppData\\local")
            os.mkdir("Expense_Tracker")
            os.chdir(self.root)
            os.mkdir("resources")
            os.chdir(self.root+"\\resources")
            os.mkdir("Logos")
            os.chdir(self.root)
            os.mkdir("cache")
            os.mkdir("users")
            os.mkdir("admin")

            with open(self.root+"\\admin\\admindata.json", "w") as f: 
                f.close()

            with open(self.root+"\\logs.log", "w") as f:
                f.close()

            logging.basicConfig(filename=f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
            logging.info("Folder creation [OK]")

            

    def cache(self) -> None:
        os.chdir(self.root+"\\cache")

        with open(".cache", "w") as f: 
            f.close()

    def get_os(self) -> str:
        return platform.system()
        

    def download(self) -> None: 
        if self.check_connection() and self.check(self.root+"\\resources\\Add_Logo.png") == False:
            urllib.request.urlretrieve(self.Add_Logo_Link, f'{self.root+"/resources/"}Logos/Add_Logo.png')
            urllib.request.urlretrieve(self.Admin_Logo_Link, f'{self.root+"/resources/"}Logos/Admin_Logo.png')
            urllib.request.urlretrieve(self.Main_Logo_Link, f'{self.root+"/resources/"}Logos/Main_Logo.png')
            urllib.request.urlretrieve(self.Delete_Logo_Link, f'{self.root+"/resources/"}Logos/Delete_Logo.png')
            urllib.request.urlretrieve(self.Expense_Logo_Link, f'{self.root+"/resources/"}Logos/Expense_Logo.png')
            urllib.request.urlretrieve(self.Eye_Logo_Link, f'{self.root+"/resources/"}Logos/Eye_Logo.jpg')
            urllib.request.urlretrieve(self.Graph_Icon_Link, f'{self.root+"/resources/"}Logos/Graph_Logo.png')
            urllib.request.urlretrieve(self.Login_Icon_Link, f'{self.root+"/resources/"}Logos/Login_Icon.png')
            urllib.request.urlretrieve(self.New_User_Logo_Link, f'{self.root+"/resources/"}Logos/New_User_Logo.png')
            urllib.request.urlretrieve(self.Information_Logo_Link, f'{self.root+"/resources/"}Logos/Info_Logo.png')
            urllib.request.urlretrieve(self.Admin_Logo_Link, f'{self.root+"/resources/"}Logos/Welcome.png')
            urllib.request.urlretrieve(self.Wrong_Logo_Link, f'{self.root+"/resources/"}Logos/Wrong_Icon.png')
            urllib.request.urlretrieve(self.Mod_Logo_Link, f'{self.root+"/resources/"}Logos/Mod_Icon.png')
            urllib.request.urlretrieve(self.Export_Logo_Link, f'{self.root+"/resources/"}Logos/Export_Icon.png')
            urllib.request.urlretrieve(self.Transfer_Logo_Link, f'{self.root+"/resources/"}Logos/Transfer_Icon.png')
            urllib.request.urlretrieve(self.Warning_Logo_Link, f'{self.root+"/resources/"}Logos/Warning_Logo.png')
            urllib.request.urlretrieve(self.Stats_Logo_Link, f'{self.root+"/resources/"}Logos/Stats_Logo.png')

            urllib.request.urlretrieve(self.Stats_Logo_Link, f'{self.root+"/resources/"}Logos/Next_Logo.png')
            urllib.request.urlretrieve(self.Stats_Logo_Link, f'{self.root+"/resources/"}Logos/Menu_Logo.png')
            urllib.request.urlretrieve(self.Stats_Logo_Link, f'{self.root+"/resources/"}Logos/Exit_Logo.png')

            logging.basicConfig(filename=f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
            logging.info("Logo Download [OK]")


    def create_log(self) -> None:
        if self.check(self.root+"//logs.log"):
            pass 
        else:        
            with open(f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\logs.log", "w") as file: 
                file.close()


    def check(self, folder) -> bool:
        if os.path.exists(folder):
            return True
        else:
            return False

    def check_connection(self) -> bool:
        try: 
            request = requests.get("https://www.google.com", timeout=5)
        except Exception:   
            return False
        else: 
            logging.info("Internet Connection [OK]")
            return True

    