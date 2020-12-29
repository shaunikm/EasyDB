## Easy DB
This simple and easy-to-use library comes with a few important functions to start storing data easier! It comes
loaded with functions to read, write, and delete data. This doesn't require too much setup, but it still requires some
user input and data to setup tables. Tables are made in JSON (JavaScript Object Notation), so they are very easy to
read.

## Dependencies

- Python 3.8 or above

## Docs

### Table(filename, tablename) | Class
This is the table class, which holds all the information for one table.

#### Parameters

- filename [type: string]: file the table will be or is stored in
- tablename [type: string]: the name of your table

#### Attributes

- deleted [type: boolean, default: False]: if the table is deleted (using a method in the class), the value of the 
   variable changes to True, methods cannot be carried out without the variable being True
- set [type: boolean, default: False]: value changes to True if table is set, methods cannot be carried out without
the variable being True
- filename [type: string]: file the table will be or is stored in
- tablename [type: string]: the name of your table

#### Example
```python
example = Table('example_file.json', 'Example Table')
```

#### Methods

---

##### `setup_table(args, already_set)`

**Use** \
Sets up the table and sets the **set** attribute to True so that other methods in the table can be carried out.

**Parameters**
- already_set [type: bool, default: False]: if the table is already setup, set the value to True and ignore **args**
- args [type: list, default: None]: should be ignored if table is already setup, if table is not setup, this is a list
all the columns of the table

**Example** \
If table is not set
```python
example.setup_table(args=['name', 'state', 'country'])
```
If table is set
```python
example.setup_table(already_set=True)
```
---
##### `apdata(primary_key, args)`

**Use** \
Can add and update rows of data using the primary key passed in.

**Parameters**
- primary_key [type: string]: distinct identifier of each row in the table, if the primary key passed as a parameter
doesn't exist in the table already a new row will be added with the primary key as the identifier,
if the primary key already exists in the table all data corresponding to the primary key will be updated with new data
- args [type: list]: the data corresponding to the primary, should be placed in the order of the table's columns

**Raises**
- ValueError - if number of arguments does not correspond to the number of columns in the table

**Example**
```python
example.apdata('Person1', ['John', 'Texas', 'US'])
# adds data to a table with the primary key as "Person1"
```
---
##### `get_keys(*key)`
**Use** \
Returns data from specific columns in the form of a dictionary.

**Parameters**
- key [type: string]: column names

**Example**
```python
data = example.get_keys('name', 'state')
print(data)
# returns data from only the "name" and "state" column
```
---
##### `get(primary_key)`
**Use** \
Returns all the data that corresponds to a primary key in the dictionary.

**Parameters**
- primary_key [type: string]: the primary key that corresponds to the row of data you want to get

**Example**
```python
data = example.get('Person1')
print(data)
```
---
##### `delete(primary_key)`
**Use** \
Deletes a row from the table, using the primary key to identify the row.

**Parameters**
- primary_key [type: string]: the primary key that corresponds to the row of data you want to delete

**Example**
```python
example.delete('Person1')
```
---
##### `req_args()`
**Use** \
Returns all the column names of the table.

**Parameters** \
None

**Example**
```python
arguments = example.req_args()
print(arguments)
```
---
##### `check_if_table_setup()`
**Use** \
Checks if the table is setup and sets the set attribute to True.

**Parameters** \
None

**Raises**
- ValueError: if the table is not setup

**Example**
```python
example.check_if_table_setup()
```
---
##### `deltable()`
**Use** \
Deletes the table.

**Parameters** \
None

**Example**
```python
example.deltable()
```
---
##### `check_if_table_is_deleted()`
**Use** \
Checks if the table is deleted and sets the deleted attribute to True.

**Parameters** \
None

**Raises**
- ValueError: if the table has been deleted

**Example**
```python
example.check_if_table_is_deleted()
```
---
##### `number_of_args()`
**Use** \
Returns the number of columns in the table.

**Parameters** \
None

**Example**
```python
number = example.number_of_args()
print(number)
```
---
##### `number_of_rows()`
**Use** \
Returns the number of rows in the table.

**Parameters** \
None

**Example**
```python
number = example.number_of_rows()
print(number)
```

## To-Do
- Make a library for EasyDB
- Make CLI using EasyDB functions and classes