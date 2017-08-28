from django.db import models
from django.contrib.auth.models import User

Choice = (
(1, 'Home'),
(2, 'About'),
(3, 'Contact')

)

class Header(models.Model):
    header_text = models.CharField(max_length=200)
    sub_header_text = models.CharField(max_length=200, null=True, blank=True)
    choose = models.IntegerField(choices=Choice, default=1)

    #class Meta:
        #verbose_name = 'Bashliq'
        #verbose_name_plural = 'Bashliqlar'

    def __str__(self):
        return self.header_text

class News(models.Model):
    post_title = models.CharField(max_length=200)
    post_sub_title = models.CharField(max_length=200)
    post_context = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.post_title

class About(models.Model):
    current_text = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.current_text

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=15)
    message = models.TextField( max_length=2000)

    def __str__(self):
        return self.name
