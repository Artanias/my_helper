from django.db import models


class DailyReview(models.Model):
    review = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return str(self.pub_date) + ': ' + self.review
