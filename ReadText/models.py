from django.db import models

class Book(models.Model):

    Title = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)

    def __str__(self):
        return self.Title

    
    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['-published_date']
