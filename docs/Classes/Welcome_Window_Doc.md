# :notebook:Welcome screen documentation

This is a documentation of the class named Welcome_Interface, which gives you detailled overview of the class without having to read the code. 

<hr>

## :bookmark_tabs:Table of contents

- 1.0 Importsection 
  - 1.1 Packages 
  - 1.2 Relative imports 
- 2.0 Classvariables 
  - 2.1 Normal attributes 
  - 2.2 Local attributes (in Constructor)
  - 2.3 GUI attributes
- 3.0 Classmethods 
  - 3.1 closeEvent()
  - 3.2 next()
  - 3.3 show_pass_func()
- 4.0 Documentation of dependecies 

<br>
<hr>

### :arrow_right: 1.0 Importsection 
<br>

#### :arrow_right: 1.1 Packages 

- <b>PyQt5.QtWidgets</b>:
  - QPushButton 
  - QDialog
  - QLineEdit
  - QHBoxLayout
  - QVBoxLayout
  - QLabel
- <b>PyQt5.QtGui</b>: 
  - QIcon
- os 
- json 
- logging

#### :arrow_right: 1.2 Relative imports 

- vars.py:
  - Logo of the UI (welcome_logo)
  - Path to the log file (log_file)
  - Logo for the error message UI (Wrong_logo)
  - Logo for the button, which is switching thhe password beetween visible and invisible (Eye_Logo)

<br>
<hr>

### :arrow_right: 2.0 Classvariables 

<br>

#### :arrow_right: 2.1 Normal attributes 

```python
click = False
```
```text
This variable is used to check the current state when the user wants to exit the program. When this is False the application can'tbe closed but othwerwise it's possible.
```

<br>

```python
root_folder = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker"
```

```text
This is the path to the folder which contains the used data. 
```

#### :arrow_right: 2.2 Local attributes  

```python
username = QHBoxLayout()
```
```text
This attribute contains a layout, with which the UI arranges the QLabel and the QLineEdit of the username. 
```

<br>

```python 
password = QHBoxLayout()
```

#### :arrow_right: 2.3 GUI attributes

<br>
<hr>

### :arrow_right: 3.0 Classmethods 

<br>

#### :arrow_right: 3.1 closeEvent()

#### :arrow_right: 3.2 next()

#### :arrow_right: show_pass_func()


<br>
<hr>

### :arrow_right: 4.0 Documentation of dependencies 