from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone #make sure to set the timezone 
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
import uuid

def url_validation(value):
    # this is a last line check if the client side check let through a non-url value
    # this was taken out of django in v1.5
    if URLValidator():
        raise ValidationError("{} is invalid, try entering in a valid URL".format(value))

class Url(models.Model):
    actual = models.URLField(max_length=120)
    key = models.CharField(max_length=40) # got rid of UUID
    created_at = models.DateTimeField(default = timezone.now,editable=False)
    count = models.IntegerField(default = 0)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Url, self).save(*args, **kwargs)

    # def clean(self):
    #     url_validation(self.actual)








