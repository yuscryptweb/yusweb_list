from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self): #to return the direct name of serached object in the admin page
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural ='searches' #to define the plural of search
