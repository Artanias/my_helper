from django.db import models


class DailyReview(models.Model):
    review = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
    	return str(self.pub_date) + ': ' + self.review


class Task(models.Model):
    task_info = models.CharField(max_length=300)
    completed = models.BooleanField()
    date_of_create = models.DateField()

    def __str__(self):
    	return str(self.date_of_create) + ': ' + self.task_info