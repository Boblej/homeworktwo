from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
