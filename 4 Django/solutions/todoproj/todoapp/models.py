from django.db import models



class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    notes = models.TextField()
    priority = models.BooleanField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.text


