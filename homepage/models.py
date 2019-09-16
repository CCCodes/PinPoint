from django.db import models


# Create your models here.
class HomeText(models.Model):
    heading = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.heading


class AboutText(models.Model):
    text = models.TextField()
    position = models.CharField(max_length=5,
                                choices=[("main", "Main"), ("col1", "Column 1"), ("col2", "Column 2")],
                                default="main")
