
### Objectives
YWBAT 
* describe the init method of a class
* compare and contrast class methods with static methods
* write methods to successfully execute sql queries in a repeated fashion
* analyze how OOP can benefit coding

### Situation
You are working with a database for a company and want to make querying more automated.  We're going to build a class that will bundle our most frequently used queries into methods and execute them for us. 


```python
from importlib import reload # used to reload a file after changes have been made

import pandas as pd
import numpy as np

import sql_file as sf # load in file with alias
reload(sf) # reload file everytime it has been updated
```




    <module 'sql_file' from '/Users/rafael/flatiron_dsc/curriculum/section06/mod01-section06-oop00-lesson-plan/sql_file.py'>



### Instantiate class object

### let's build a  method that lists all of the tables in our database

### Let's build a method that selects all of the items from a given table_name

### Let's build a method that returns a table as a dataframe

### what are some other methods we can create?
