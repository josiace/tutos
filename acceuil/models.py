from django.db import models

# Create your models here.
class Contenus(models.Model):
    titre=models.CharField(max_length=100)
    blog=models.TextField()
    auteur=models.CharField(max_length=100)
    mail=models.EmailField()
    date_creation=models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.titre

class Acceuilperso(models.Model):
    titre=models.CharField(max_length=100)
    description=models.TextField()



    def __str__(self):
        return self.titre