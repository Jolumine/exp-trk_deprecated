# :notebook: Setup Documentation 

Full documentation for Setup, including <b>method</b>, <b>parameter</b> and <b>output specification</b>. 

<hr>

## :bookmark_tabs: Table of contents:

- 1.0 Used libraries 
- 2.0 Class Variables 
- 3.0 Class Methods
  - 3.1 dirs()
  - 3.2 cache()
  - 3.3 get_os()
  - 3.4 download()
  - 3.5 create_log()
  - 3.6 check()
  - 3.7 check_connection()
- 4.0 Documentation of dependencies 

<br>
<hr>

### :clipboard: 1.0 Used libaries: 

- os 
- platform 
- urllib.request
- requests
- logging 
- threading 

<br>
<hr>

### :clipboard: 2.0 Class Variables 
```text
The class variables include 12 links for the 12 different logos, which are downloaded by the download() method. 
```

```python
Add_Logo_Link = "https://cdn-icons-png.flaticon.com/512/992/992651.png"
Admin_Logo_Link = "https://cdn-icons-png.flaticon.com/512/2099/2099058.png"
Delete_Logo_Link = "https://cdn-icons-png.flaticon.com/512/3096/3096673.png"
Expense_Logo_Link = "https://cdn-icons-png.flaticon.com/512/61/61584.png"
Eye_Logo_Link = "https://cdn-icons-png.flaticon.com/512/159/159604.png"
Graph_Icon_Link = "https://cdn-icons-png.flaticon.com/512/3121/3121571.png"
Login_Icon_Link = "https://cdn-icons-png.flaticon.com/512/126/126486.png"
Main_Logo_Link = "https://cdn-icons-png.flaticon.com/512/2/2144.png"
New_User_Logo_Link = "https://cdn1.iconfinder.com/data/icons/avatar-1-2/51Add_User1-512.png"
Wrong_Logo_Link = "https://cdn-icons-png.flaticon.com/512/1828/1828665.png"
Mod_Logo_Link = "https://cdn-icons-png.flaticon.com/512/61/61456.png"
Export_Logo_Link = "https://cdn-icons-png.flaticon.com/512/151/151900.png"
```


<br>
<hr>

### :arrow_right: 3.0 Methods: 
<br>

#### :arrow_right: 3.1 Method: dirs()
```text
This method create every folder and files which will be used by the application. 
```

```python
paramter = None
output = None
```

It will access your ./AppData/local folder an create an <b>Expense_Tracker</b> folder. 
Folders created: <br> 
- users
- resources + resources/Logos
- cache 
- admin

Files created: <br>
- admin/admin_data.json 
- logs.log
- settings.json

<br>


#### :arrow_right: 3.2 Method: cache()

```text
This method is used one time. It will create a .cache file with which the application can   
check if the Welcome Window will be displayed or not. 
```

```python
paramter = None
output = None
```

<br>

#### :arrow_right: 3.3 Method: get_os()

```text
This method return the current os. So the application can check if the Operating System is Windows or something else. 
```

```python
paramter = None
output = str
```

```python
platform.system()   

# simplified by

get_os()
```

<br>

#### :arrow_right: 3.4 Method: download()

```text
This method is responsable for downloading every necessary logo, which will be used in the User Interface. 
The logos will be stored in the, from dirs() Method created directory /resources/Logos/.
```

```python
paramter = None
output = None
```

<br>

#### :arrow_right: 3.5 Method: create_log()

```text
This Method is creating the log file in which, the logs are stored. The file will be stored in the main folder of the application. 
```

```python
paramter = None
output = None
```

<br>

#### :arrow_right: 3.6 Method: check()

```text
This method is checking if a given path is existing on the machine or not. 
```

```python
parameter = path to the folder the functions needs to check (Type: str)
output = True: if folder exists on the machine; False: otherwise
```

<br>

#### :arrow_right: Method: 3.7 check_connection()

```text
This method is checking the internet connection. It sends requests to "https://www.google.com", with a timout of 5.
```

```python
parameter = None
outout = True: if connection is available ; False : otherwise
```

<br>
<hr>

### :page_with_curl: 4. Documentations of dependecies