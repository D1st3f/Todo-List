
![Logo](https://cdn-icons-png.flaticon.com/512/6194/6194029.png)


# ToDO List

This project was created to create and track tasks.


## 👩‍💻 _Installation & Run_
### 🧠 Set up the environment 


 On Windows:
```python
python -m venv venv 
venv\Scripts\activate
 ```

 On macOS:
```python
python3 -m venv venv 
source venv/bin/activate
 ```

### 👯 Set up requirements 
```python
pip install -r requirements.txt
```


### 🤔 Make migrations and migrate
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
### 📫 Install database fixture
```python
python manage.py loaddata data.json
```
### ⚡️ Run server
```python
python manage.py runserver
```
### 😄 Go to site [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- After loading data from fixture you can use following superuser (or create another one by yourself):
    - Login: ```Admin```
    - Password: ```Admin123```