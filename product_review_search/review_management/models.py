from django.db import models

# Create your models here.
class Review(models.Model):
    "for storing review datasets "
    product_id =  models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    profile_name = models.CharField(max_length=50)
    helpfulness = models.CharField(max_length=50)
    score = models.FloatField()
    time = models.DateTimeField()
    summary = models.CharField(max_length=255)
    text = models.TextField()
    helpfulness_score = models.FloatField()

    def __str__(self):
        return f"user : {self.user_id} product : {self.product_id}, summary : {self.summary}"

