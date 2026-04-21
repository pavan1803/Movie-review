from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userdetails')

    phone = models.BigIntegerField()
    age = models.IntegerField()
    userpic = models.ImageField(upload_to='userimg/',blank=True,null=True)

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=200)
    rating = models.IntegerField()
    review = models.TextField(blank=True)

    def __str__(self):
        return self.movie_title


# Create your models here.
