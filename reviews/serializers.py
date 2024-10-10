from rest_framework import serializers
from reviews.models import Review, ReviewLike
from comments.serializers import CommentSerializer
from reviews.utils import get_tmdb_movie_details


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review Model
    """
    user = serializers.ReadOnlyField(source='user.username')
    movie_details = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

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
            'comments',
        ]

    def get_movie_details(self, obj):
        """
        A method that leverages the get_tmdb_movie_details function 
        to retrieve movie details from tmdb based on the movie title
        """
        movie_data = get_tmdb_movie_details(obj.movie_title)
        if movie_data:
            return movie_data
        else:
            return {'Error': 'Movie details not found'}

    def validate_rating(self, data):
        """
        Validation for the rating field to ensure ratings
        are between 1 and 5
        """
        if data < 1 or data > 5:
            raise serializers.ValidationError("Rating should be between 1 and 5")
        return data
    
class ReviewLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the ReviewLike Model
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReviewLike
        fields = ['id', 'user', 'review', 'created_at']