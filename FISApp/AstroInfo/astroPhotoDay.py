#Import required libraries:
from django.shortcuts import render
import nasapy
import os
from datetime import datetime, timedelta
import urllib.request


def astroPhotoOftheDay(request):
    # Initialize Nasa class by creating an object:
    k = "523p5hPYHGzafYGLCkqa54kKMTV2vbP0XcPxkcLm"
    nasa = nasapy.Nasa(key = k)
    #Get today's date in YYYY-MM-DD format:
    d = datetime.today() - timedelta(days=1)
    d.strftime('%Y-%m-%d')
    #Get the image data:
    apod = nasa.picture_of_the_day(date=d, hd=True)
    # POINT A:
    # Check the media type available:
    Date_of_release = ""
    image_owner = ""
    image_title = ""
    img_description = ""
    img_url = ""
    if (apod["media_type"] == "image"):
        # POINT B:
        # Displaying hd images only:
        if ("hdurl" in apod.keys()):

            # Displaying information related to image:
            if ("date" in apod.keys()):
                Date_of_release = apod["date"]
            if ("copyright" in apod.keys()):
                image_owner = apod["copyright"]
            if ("title" in apod.keys()):
                image_title = apod["title"]
            if ("explanation" in apod.keys()):
                img_description = apod["explanation"]
            if ("hdurl" in apod.keys()):
                img_url = apod["hdurl"]

            context = {
                'Date_of_release' : Date_of_release,
                'image_owner' : image_owner,
                'image_title' : image_title,
                'img_description' : img_description,
                'img_url' : img_url,
            }
            return render(request, 'astroPhotoDay.html', context)

def astroPhotoOfYesterday(request):
    # Initialize Nasa class by creating an object:
    k = "523p5hPYHGzafYGLCkqa54kKMTV2vbP0XcPxkcLm"
    nasa = nasapy.Nasa(key = k)
    #Get today's date in YYYY-MM-DD format:
    d = datetime.today() - timedelta(days=2)
    d.strftime('%Y-%m-%d')
    #Get the image data:
    apod = nasa.picture_of_the_day(date=d, hd=True)
    # POINT A:
    # Check the media type available:
    Date_of_release = ""
    image_owner = ""
    image_title = ""
    img_description = ""
    img_url = ""
    if (apod["media_type"] == "image"):

        # POINT B:
        # Displaying hd images only:
        if ("hdurl" in apod.keys()):

            # Displaying information related to image:
            if ("date" in apod.keys()):
                Date_of_release = apod["date"]
            if ("copyright" in apod.keys()):
                image_owner = apod["copyright"]
            if ("title" in apod.keys()):
                image_title = apod["title"]
            if ("explanation" in apod.keys()):
                img_description = apod["explanation"]
            if ("hdurl" in apod.keys()):
                img_url = apod["hdurl"]

            context = {
                'Date_of_release' : Date_of_release,
                'image_owner' : image_owner,
                'image_title' : image_title,
                'img_description' : img_description,
                'img_url' : img_url,
            }
            return render(request, 'astroPhotoYesterday.html', context)