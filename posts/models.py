from django.db import models

# Create your models here.
class Post(models.Model):
    موضوع = models.CharField(max_length=50)
    اجاره = models.BooleanField(default=False)
    فروش = models.BooleanField(default=False)
    توضیحات = models.TextField(blank=True,null=True)
    ویلا = models.BooleanField(default=False)
    آپارتمان = models.BooleanField(default=False)
    زمین = models.BooleanField(default=False)
    location = models.TextField(default="sari")
    متراژ = models.IntegerField(default=1)
    بر = models.IntegerField(default=1)
    سند = models.CharField(default='',max_length=10)
    قیمت_هر_متر = models.IntegerField(default=0)
    قیمت_کل = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}- {}".format(self.pk, self.موضوع)

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    کامنت = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)