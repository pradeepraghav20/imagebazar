from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length= 100)
    description=models.TextField()
    def __str__(self):
        return self.title
    
    

class Image(models.Model):
    title=models.CharField(max_length=100)
    decription=models.TimeField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
