

```sh
python3.10 -m venv _venv

source _venv/bin/activate

pip install -r requirements.txt

django-admin startproject project .


python manage.py startapp main

python manage.py makemigrations
python manage.py migrate
```


## Fonts
- https://fonts.google.com/selection/embed 

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
```