from django.db import models
from django.contrib.auth.models import User

from scripts.utils import jalali_convert
from django.urls import reverse
from django_resized import ResizedImageField

class Category(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):


        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def get_jalali_date(self):

        return jalali_convert(self.created)

    def __str__(self):

        return self.name


class BlogModel(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="blog",null=True,blank=True)
    titel=models.CharField(max_length=200)
    view=models.IntegerField(default=0)
    image=ResizedImageField(size=[1000, 800],upload_to="media/blog/image")
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    category=models.ManyToManyField(Category,related_name="blog")
    status=models.BooleanField(default=True)

    def get_absolut_url(self):


        return reverse("Blog_App:blog_detail",kwargs={"pk":self.id})




    def get_jalali_date(self):


        return jalali_convert(self.created)

    def __str__(self):

        return self.titel
