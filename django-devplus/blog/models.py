from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='media/posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=1)


    def __str__(self) -> str:
        return f'Post:{self.title} - {self.author}'

