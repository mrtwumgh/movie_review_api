from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id', 'user', 'movie_title', 'review_content', 'rating', 'created_date']

    def validate_rating(self, data):
        if data["rating"] < 1 or data["rating"] > 5:
            raise serializers.ValidationError("Rating should be between 1 and 5")
        return data