from rest_framework import serializers
from reviews.models import Review, ReviewLike
from reviews.utils import get_tmdb_movie_details


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    movie_details = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 
            'user', 
            'movie_title', 
            'review_content', 
            'rating', 
            'created_date',
            'movie_details',
            'like_count',
        ]

    def get_movie_details(self, obj):
        movie_data = get_tmdb_movie_details(obj.movie_title)
        if movie_data:
            return movie_data
        else:
            return {'Error': 'Movie details not found'}

    def validate_rating(self, data):
        if data < 1 or data > 5:
            raise serializers.ValidationError("Rating should be between 1 and 5")
        return data
    
class ReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReviewLike
        fields = ['id', 'user', 'review', 'created_at']