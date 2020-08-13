from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Quote(models.Model):
    author = models.ForeignKey(User,related_name='author',on_delete=models.CASCADE)
    quote = models.CharField(max_length=128,blank=False)
    created_on = models.DateTimeField(auto_now_add=True)


class Publication(models.Model):
    name = models.CharField(max_length=128, blank=False)
    quote = models.ForeignKey(Quote, related_name='publications', on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)



