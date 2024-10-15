from reviews.serializers import ReviewSerializer
from reviews.models import Review, ReviewLike
from rest_framework import generics, permissions, filters, views, status
from reviews.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from reviews.filters import ReviewFilter



class ReviewListView(generics.ListAPIView):
    """
    Class based view to List All Reviews
    """
    queryset = Review.objects.select_related("user")
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ReviewFilter
    search_fields = ['movie_title']
    ordering_fields = ['rating', 'created_date']
    ordering = ['-created_date']



class ReviewCreateView(generics.CreateAPIView):
    """
    Class Based View to create a review
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes =[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Overrides the default perform create method to assign the user to a review
        """
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveAPIView):
    """
    Class based view to view an individual review based on the primary key
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class ReviewUpdateView(generics.UpdateAPIView):
    """
    Class Based view to update an individual review
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class ReviewDeleteView(generics.DestroyAPIView):
    """
    Class Based view to delete an individual review
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

# Like and Unlike Views
class LikeAndUnlikeView(views.APIView):
    """
    Class Based view that defines the like and unlike feature
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """
        Defines the like feature
        """
        review = get_object_or_404(Review, pk=pk)
        like, created = ReviewLike.objects.get_or_create(user=request.user, review=review)
        if not created:
            return Response({
                "detail": "You already liked this review"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "detail": "Review Liked"
        }, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        """
        Defines the unlike feature
        """
        review = get_object_or_404(Review, pk=pk)
        like = ReviewLike.objects.filter(user=request.user, review=review)
        if like.exists():
            like.delete()
            return Response({
                "detail": "Like removed"
            }, status=status.HTTP_204_NO_CONTENT)
        return Response({
            "detail": "You have not liked this review"
        }, status=status.HTTP_400_BAD_REQUEST)