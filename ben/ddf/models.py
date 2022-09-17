from django.db import models
class post(models.Model):

    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/')
    image3=models.ImageField(upload_to='images/',default="")
    image4=models.ImageField(upload_to='images/',default="")
    image5=models.ImageField(upload_to='images/',default="")
    image6=models.ImageField(upload_to='images/',default="")
    image7=models.ImageField(upload_to='images/',default="")
    image8=models.ImageField(upload_to='images/',default="")
    image9=models.ImageField(upload_to='images/',default="")
    image10=models.ImageField(upload_to='images/',default="")
    image11=models.ImageField(upload_to='images/',default="")
    image12=models.ImageField(upload_to='images/',default="")
    image13=models.ImageField(upload_to='images/',default="")
    image14=models.ImageField(upload_to='images/',default="")
    image15=models.ImageField(upload_to='images/',default="")
    image16=models.ImageField(upload_to='images/',default="")
    image17=models.ImageField(upload_to='images/',default="")
    image18=models.ImageField(upload_to='images/',default="")
    image19=models.ImageField(upload_to='images/',default="")
    image20=models.ImageField(upload_to='images/',default="")
    image21=models.ImageField(upload_to='images/',default="")
    image22=models.ImageField(upload_to='images/',default="")

class pot(models.Model):
    
    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/')
    image3=models.ImageField(upload_to='images/')
    image4=models.ImageField(upload_to='images/')
    image5=models.ImageField(upload_to='images/')
    image6=models.ImageField(upload_to='images/')

class pat(models.Model):
    
    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/')
    image3=models.ImageField(upload_to='images/')

class con(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.email
