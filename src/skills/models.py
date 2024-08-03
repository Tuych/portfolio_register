from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=100)  # Charfild = input type text
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skills/images/')  # ImageFild = input type= file, rasmlar media papkaning ichida  skills/images kurinishida saqlanadi
    url = models.URLField(blank=True)  # Urlfild = input type = url,   blank=True =  null- bush pulishi mumkin

    def __str__(self):
        return self.title
