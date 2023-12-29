from django.db import models

# Create your models here.


class Message(models.Model):

    def __str__(self):
        return self.message_text[0:10]

    message_text = models.TextField(max_length=500)
