# :bar_chart:Expense_Tracker (Development)

<b>You always searched a way to track your money? Than the search ends here. </b>

This is a program with which you can track and store your income and your expenses for Windows (not available for MacOs or Linux because of the filesystem). <br>
Including a user interface for easy usage and detailled data storage based on .csv files and JSON.
<br>You have the possibility to check everything with bar graphs and assuredly more specific in the future.  
<br>

## :white_check_mark:Installation 

```bash
git clone https://github.com/Jolumine/exp-trk.git
cd exp-trk
python -m pip install -r requirements.txt
python run.py
```
<br>

## :hammer_and_wrench:Usage

The user interface is mostly self-explanatory but I'll give you a quick guide for the setup: 
<br>

1. The setup will run automatically when you start the application. It will download the logos and create all necessary files, if you are connected to the internet. :arrow_heading_down::file_folder:
2. A window will be created and you have to set a admin username and a password for it. 
3. Then the login will appear. 
4. Click to create new user and fill in the requested information. :new:
5. After finishing the user creation, you can login and start using the application.:white_check_mark:

<br>

## :warning:Bugs / Problems

1. Delete a user in the admin window (get a PermissionError when you try to delete the folder).
2. Cannot close Matplotlib window without having to close every window before.
   
<br>

## :soon:Coming soon

1. More explicitly specified logs 
2. Better Analytics
3. Password Encryption
4. Global and private Settings

<br>

## :wrench:Contributing 

Pull requests are welcome, if you have major changes please create an issue first or <br>contact me on Reddit or Twitter.

<br>

## :link:Contact

:iphone:  Twitter: https://twitter.com/Leo_Becker09 <br>
:computer: Reddit: https://www.reddit.com/user/Jolumine1