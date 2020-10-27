from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


#model for users
class User(AbstractUser):
    #full_name = models.CharField(max_length=250)
    #email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #phone = models.IntegerField()
    #assword = models.CharField(max_length=50)
    post_perm = models.BooleanField(default=False)

    
    class Meta:
        ordering: '-date_joined'
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        #return reverse('user-detail', args=[str(self.pk)])
        return f"/product/{self.pk}"



class Post(models.Model):
    #id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, )
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=False)
    price = models.CharField(blank=False, null=False, max_length=5000000)   

    class Meta:
        ordering: '-date'

    def __str__(self):
        '''retuns the title of the instance when called upon by the admin'''
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular Post instance."""
        #return reverse('model-detail-views', args=[str(self.pk)])
        return f"/product/{self.pk}"

    def get_owner(self):
        """ returns the field {owner} of a model instance """
        return self.owner
   

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=5000)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_owner(self):
        return self.owner
   

