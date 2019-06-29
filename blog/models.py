from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    writer = models.ForeignKey(User, editable =False, null=True, blank=True, on_delete=models.SET_NULL,)
    title=models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    explain = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]
    