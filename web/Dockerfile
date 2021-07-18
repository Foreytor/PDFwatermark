FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_django
WORKDIR /web_django
ADD requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_django/
