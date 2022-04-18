# :notebook:Folder Algorithms Documentation 

This is a quick documentation for every algorithm used for the folderstructure of every user. 

<hr>

## :bookmark_tabs: Table of contents 

- 1.0 used libraries 
- 2.0 Methods 
  - 2.1 Method: get_all_users()
  - 2.2 Method: get_new_number()
  - 2.3 Method: get_folder_number()
  - 2.4 Method: get_password()
- 3.0 Documentation of dependecies

<br>
<hr>

### :clipboard: 1.0 Used libraries: 

- os
- json

<br>
<hr>

## :arrow_right:2.0 Methods: 

<br>

### :arrow_right: 2.1 get_all_users()

```text
This method is responsable for the content of every QComboBox which is displaying the userinformations. 
The method is iterating trough the users folder in the AppData and returns a list where the indexes are Username-Firstname-Lastname. 
```

```python
parameter = None 
output = [Username-Firstname-Password](Type: str)
```

<br>

### :arrow_right: 2.2 get_new_number()

```text
This method returns an integer which is used as new number for the user folder in the creation process. The folder names are numbers starting at 1 and the method returns the actual length of the folder + 1 
```

```python
parameter = None
output = number (type: str)
```

<br>

### :arrow_right: 2.3 get_folder_number()

```text
This method returns the number of the folder with the username and the password as parameter. This method is used among other use cases in the login process to give the folder number of the active user to the main windonw. 
```

```python
parameter = Username (type: str), Password (type: str)
output = number (type: str)
```

<br>


### :arrow_right: 2.4 get_password()

```text
This method returns the password correspondent to the given username. It is used for example in the modifing process when the get_folder_number() method needs the password with the username of the given selected list.
```

```python
parameter = Username (type: str)
output = Password (type: str)
```

<br>
<hr>

### :page_with_curl: 3.0 Documentations of dependecies

- os module: [Documentation](https://docs.python.org/3/library/os.html)
- json module: [Documentation](https://docs.python.org/3/library/os.html)

