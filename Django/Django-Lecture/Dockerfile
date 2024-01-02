FROM python:3.12

RUN mkdir /home/django-tutorial

WORKDIR /home/django-tutorial/jeseo_site

RUN pip install --upgrade pip &&\
    pip install django

CMD [ "python", "/home/django-tutorial/jeseo_site/manage.py", "runserver", "0.0.0.0:8000" ]