from django.db import models

# Create your models here.
class Review(models.Model):
    "for storing review datasets "
    product_id =  models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    profile_name = models.CharField(max_length=50)
    helpfulness = models.CharField(max_length=50)
    score = models.FloatField(db_index=True)
    time = models.CharField(max_length=30)
    summary = models.CharField(max_length=255)
    text = models.TextField()
    helpfulness_score = models.FloatField(db_index=True)

    def __str__(self):
        return f"user : {self.user_id} product : {self.product_id}, summary : {self.summary}"


