from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude = models.CharField(max_length=255)
    longtitude = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True, related_name='branch')

class Contact(models.Model):
    class Type(models.IntegerChoices):
        PHONE = 1
        FACEBOOK = 2
        EMAIL = 3

    type = models.IntegerField(choices=Type.choices)
    value = models.CharField(max_length=255)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True, related_name='contact')


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    logo = models.CharField(max_length=25)

    def __str__(self):
        return self.name
