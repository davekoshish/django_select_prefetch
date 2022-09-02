


from email.headerregistry import Address
from django.db import models



class Book(models.Model):

    

    title = models.CharField(max_length=100)

    author = models.CharField(max_length=100)

    price = models.IntegerField()

    published_year = models.IntegerField()
    
    def __str__(self):
        return self.title

class Detail(models.Model):

    name=models.ForeignKey(Book,on_delete=models.SET_NULL, blank=True, null=True)
    
    
    def __unicode__(self):return self.name