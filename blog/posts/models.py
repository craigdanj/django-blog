from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	description = models.TextField(default="")
	pub_date = models.DateTimeField('date published', default=None)
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	tag = models.ManyToManyField(Tag, blank=True)

	def __str__(self):
		return self.title
