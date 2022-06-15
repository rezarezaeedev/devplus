from django.db import models


class SiteInfo(models.Model):
    title = models.CharField(max_length=50)
    admin_name = models.CharField(max_length=50)
    buildtext=models.CharField(max_length=50,null=1)
    fortext=models.CharField(max_length=50,null=1)
    copyright=models.CharField(max_length=50,null=1)
    is_active = models.BooleanField(default=1)


    def __str__(self) -> str:
        return f'Post:{self.title} - {self.admin_name}'

