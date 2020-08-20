from django.db import models

# Create your models here.

#Category Model with two fields namely - ID and category
class Category(models.Model):
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.category

#Movies Model with 4 fields - ID, moviename, category(Foreign key), rating
class Movies(models.Model):
    rating_choices = ((1,1),(2,2),(3,3),(4,4),(5,5))
    moviename = models.CharField(max_length=50)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating_choices)


    def __str__(self):
        return self.moviename