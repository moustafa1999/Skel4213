# Skel4213
Repo for software engineering

In this project I used Heroku to publish my webserver. Heroku allows you to create a user friendly dashboard by using one of its elements ( Ex. DRAXLR , TREVOR)
You can choose which add-on you want to use and link it to the database you already have. the database used in this project is a local  Rest framework Django which was then published on to heroku. 
You can find a step-by-step tutorial below in this file.

 # This is a Youtube video link demonstrating the dashboard design before and after user suggestions: https://youtu.be/JFABvVRNPZw

a CSV file Titled (Readings_table) is included in the repository that has all of the sensor readings used. You can Import all that data if your dashboard program supports importing CSV files.
a Backup file for the data is also Included you can use Heroku's heroku-postgresql extension to import all of the readings as well.

the dashboard link is included below:

# Version1: https://app.trevor.io/share/dashboard/a0115e5e-da83-44bc-9c61-c35059c1acb0/load.html?pin=767a9

# Version2: https://app.trevor.io/share/dashboard/0ca64b01-a373-456f-ad5a-9a9a98041e81/load.html?pin=e84a0


# The raw database link :

http://cloud4213.herokuapp.com/sensors/

# this is a step by step tutorial on creating rest framework API and publishing on heroku app / creating dashboard 

#first python needs to be installed and virtual environment needs to be activted

$ pyenv virtualenv django-rest
$ pyenv local django-rest


# django needs to be installed and new project configured

$pip install django
$django-admin startproject webserver
 
 # If you already have a project and just need to create rest API application start from here 
 
 $ python manage.py startapp myapi
 
 # edit settings.py in (/webserver) to add new app

INSTALLED_APPS = [
    'myapi.apps.MyapiConfig',
    ... # Leave all the other INSTALLED_APPS
]

# migrate database in order to activate SQlite

$ python manage.py migrate

# add the details you want to save in /myapi/models.py  then create file serializers.py in order to convert data to json string to be saved 

#/myapi/models.py

from django.db import models

# Create your models here.
class sensor(models.Model):
    temp = models.CharField(max_length=60)
    ic = models.CharField(max_length=60)
    dist =  models.CharField(max_length=60)
    time =  models.CharField(max_length=60)
    def __str__(self):
        return self.temp
        return self.id
        return self.dist
        return self.time
        
END

# /myapi/serializers.py

from rest_framework import serializers

from .models import sensor

class sensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sensor
        fields = ('id', 'time' ,'temp', 'ic', 'dist')
        
  END
  
  
# update database changes
  
$ python manage.py makemigrations
  
  
#register new database model in myapi/admin
  
from django.contrib import admin
from django.contrib import admin
from .models import sensor
admin.site.register(sensor)


# display your data by editing /myapi/view.py    #P.s. function sensorViewSet allows database to recieve GET or POST requests 

# /webserver/views.py

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import sensorSerializer
from .models import sensor


class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all().order_by('dist')
    serializer_class = sensorSerializer

END

#we need to link the page that we just created to a path so we can access it 

#from /webserver/urls.py we will add the path we want to view the database from 

from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapi.urls")),  # new
     ]

END



# from myapi/urls.py we will link to the same path and also add router function so any updates fron POST or GET request url will actually update the database locally

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sensors', views.sensorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

END


#now our webserver and database are ready and can be deployed locall by 
$ python manage.py runserver


#We choose to run on heroku so that users can easily see our server and dashboard

# first changes need to be done to /webserver/settings.py

1 debug set to false
Debug= False

2 route change to static 
STATIC_ROOT = os.path.join(BASE_DIR, ‘static’)

3 activate heroku
django_heroku.settings(locals())

4 import heroku libraries
import os
import django_heroku

#install django-heroku & gunicorn
$ pip install django-heroku
$ pip install gunicorn

#for heroku to run it needs Procfile to specify the tool used to produce the webserver in OUR case Gunicorn and requirements.txt file to specify all needed libraries and programs used

# in Procfile
web: gunicorn myproject.wsgi

# run command to save all downloaded libraries in requirements.txt
$pip freeze > requirements.txt


# after commiting all changes to git hub repo run next commands to publish webserver
$ heroku login --interactive
$ heroku create skle4213
$ git push heroku master

# run next command to transfer all data in your local database to heroku database
$ heroku run python manage.py migrate

THAT IS ALL ! YOUR HEROKU ONLINE DATABASE IS READY.
