from django.db import models
from reviews.models import Review
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Represents a comment for each review.
    """
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Comment by {self.user.username} on Review {self.review.id}"