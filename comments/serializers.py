from rest_framework import serializers
from comments.models import Comment



class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    user = serializers.ReadOnlyField(source='user.username')
    created_date = serializers.ReadOnlyField()
    updated_date = serializers.ReadOnlyField()
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'review', 'user', 'content', 'created_date', 'updated_date']

    def validate_content(self, value):
        """
        custom validation for content
        """
        if not value.strip():
            return serializers.ValidationError("Comment cannot be empty")
        return value