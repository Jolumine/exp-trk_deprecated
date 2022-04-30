import os 

# Logos 

Main_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Main_Logo.png"

Money_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Expense_Logo.png"

Settings_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Admin_Logo.png"

Add_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Add_Logo.png"

Information_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Info_Logo.png"

Delete_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Delete_Logo.png"

Wrong_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Wrong_Icon.png"

Login_Icon = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Login_Icon.png"

New_User_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\New_User_Logo.png"

welcome_logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Welcome.png"

Admin_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Admin_Logo.png"

Graph_Icon = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Graph_Logo.png"

Mod_Icon = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Mod_Icon.png"

Eye_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Eye_Logo.jpg"

Export_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Export_Icon.png"

Transfer_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Transfer_Icon.png"

Warning_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Warning_Logo.png"

Stats_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\resources\\Logos\\Stats_Logo.png"

Exit_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Expense_Tracker\\resources\\Logos\\Exit_Logo.png"

Next_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Expense_Tracker\\resources\\Logos\\Next_Logo.png"

Menu_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Expense_Tracker\\resources\\Logos\\Menu_Logo.png"

Gen_Logo = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Expense_Tracker\\resources\\Logos\\Gen_Logo.png"

# Const 

field_names = ["Amount", "Day", "Month", "Year", "Type", "Description"]

days_list = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months = ["" ,"January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]

wo_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]

months_all = ["All", "January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]

years = [str(i) for i in range(2022, 2031)]

weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

types = ["Cash", "Credit Card", "Cheque"]

types_all = ["All", "Cash", "Credit Card", "Cheque"]

years_all = ["All", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]

days = [str(i) for i in range(1 , 32)]

show_dict = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}

# Passive income

routines = ["daily", "weekly", "monthly", "yearly"]

types = ["Stocks / Yield", "Real estate", "Side-Hustle"]

# Logs 

log_file = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\logs.log"

# Settings std

std_settings = {
    "currency": "USD", 
    "language": "EN", 
    "darkmode": False
}