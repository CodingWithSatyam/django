from django.db import models

class PostApi(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    desc = models.TextField()

    def __str__(self):
        return self.title