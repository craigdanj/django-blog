from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=80)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)

class Post(models.Model):
	#description = models.CharField(max_length=5000)
	#pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.post_title
