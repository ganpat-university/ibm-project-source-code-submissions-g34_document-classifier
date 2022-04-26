from django.db import models

# Create your models here.
class UploadImage(models.Model):  
    caption = models.CharField(max_length=200)  
    # image = models.ImageField(upload_to='images')  
    driving = models.ImageField(upload_to='images')  
    pancard = models.ImageField(upload_to='images')  
    cheque = models.ImageField(upload_to='images')  
    salaryslip = models.ImageField(upload_to='images')  

    def __str__(self):  
        return self.caption 