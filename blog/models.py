from django.db import models

class Blog(models.Model) :
    title = models.CharField(max_length = 200)
    date = models.DateTimeField('date published')
    writer = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.writer[:100]

        