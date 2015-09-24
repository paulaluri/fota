from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	text = models.CharField(max_length=200, blank=False)
	country_code = models.CharField(max_length=2, blank=False, default="us")
	time = models.DateTimeField(auto_now=False, auto_now_add=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.text