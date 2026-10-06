# Album Rating Site
Note: The only working endpoint is **http://127.0.0.1:8000/artists/**

## Basic Setup
### 1. Create a virtual environment
```
python -m venv venv
```

### 2. Activate venv
Windows:
```
venv/Scripts/activate
```
Apple:
```
source venv/bin/activate
```

### 3. Download dependencies
```
pip install -r requirements.txt
```

### 4. Build database
```
python manage.py migrate
```

## Helpful Commands
Run this command to begin the live server:
```
python manage.py runserver
```

An important thing to note is that CSS files will not update on the live server unless the cache is emptied.
You can press **shift + f5** to do a hard refresh.

This command allows you to access the Django shell. The shell can be used for adding stuff to the database directly for testing:
```
python manage.py shell
```

You can use **exit()** inside the shell to exit.

If you ever download any new modules using pip, remember to use this command to save them to **requirements.txt**:
```
pip freeze > requirements.txt
```
