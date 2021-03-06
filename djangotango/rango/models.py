from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = 0
    likes = 0

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'

        def __str__(self):
            return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
