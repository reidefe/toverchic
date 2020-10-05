from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

#model for users
class User(AbstractUser):
    full_name = models.CharField(max_length=250)
    #email = models.EmailField()
    phone = models.IntegerField()
    #assword = models.CharField(max_length=50)
    post_perm = models.BooleanField(default=False)

    
    class Meta:
        ordering: '-date'
    def __str__(self):
        return self.full_name
    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user-detail', args=[str(self.id)])


class Post(models.Model):
    #id = models.UUIDField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, uploaod_to='/Posts_images')
    date = models.DateTimeField(auto_now_add=True)

   

    class Meta:
        ordering: '-date'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular Post instance."""
        return reverse('post-detail', args=[str(self.id)])

   

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


