from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    This class represents a Movie Review
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    movie_title = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} review by {self.user.username}"