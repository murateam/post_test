from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField(blank=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='posts/images/')

	class Meta:
		ordering = ['-date_pub']

	def __str__(self):
		return self.title