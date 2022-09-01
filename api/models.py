from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=300)
    def No_rates(self):
        ratings = Rating.objects.all()
        return len(ratings)
    
    def average_rate(self):
        sum =0
        average_rate =0
        ratings = Rating.objects.filter(meal=self)

        if len(ratings) > 0:
            for x in ratings:
                sum +=x.stars
            average_rate =sum/len(ratings)        

        return average_rate
            
    


class Rating(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=(MinValueValidator(1),MaxValueValidator(5)))
    
    def __str__(self):
        return str(self.meal)

    class Meta:
        unique_together = (('user','meal'),)
        index_together = (('user','meal'),)
    
