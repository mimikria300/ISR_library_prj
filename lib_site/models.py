from django.db import models
import uuid
from django.forms import ValidationError

#id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    birth_year = models.PositiveIntegerField()
    country = models.CharField(blank = True, max_length=200)

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    genres = models.ManyToManyField('Genre', related_name='books') #todo:: how do i limit choice to genres? if they are precreated, will they generate automatically??
    pub_year = models.PositiveIntegerField()

    def check_pubdate(self):
        if self.pub_year < self.author.birth_year:
            #todo:: where will it raise? html form OR???
            raise ValidationError("Publication year must be greater than the author's birth year.") 
    
    def save(self, *args, **kwargs):
        self.check_pubdate()
        super().save(*args, **kwargs) #super = models.Model, right?

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre_name = models.CharField(max_length=200)
    genre_rating = models.PositiveIntegerField()

    

    
    


