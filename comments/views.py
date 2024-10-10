
from rest_framework import generics, permissions
from reviews.permissions import IsOwnerOrReadOnly
from comments.serializers import CommentSerializer
from comments.models import Comment


class CommentListAPIView(generics.ListAPIView):
    """
    API view to list comments for a specific review.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        return Comment.objects.filter(review__id=review_id)
    
class CommentCreateView(generics.CreateAPIView):
    """
    API view to create a new comment.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        serializer.save(user=self.request.user, review_id=review_id)

class CommentDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single comment by its ID
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

class CommentUpdateView(generics.UpdateAPIView):
    """
    API view to update a comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class CommentDeleteView(generics.DestroyAPIView):
    """
    API view to delete a comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]