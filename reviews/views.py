from reviews.serializers import ReviewSerializer
from reviews.models import Review, ReviewLike
from rest_framework import generics, permissions, filters, views, status
from reviews.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title', 'rating']
    ordering_fields = ['rating', 'created_date']
    filterset_fields = ['movie_title', 'rating']
    ordering = ['-created_date']



class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes =[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

# Like and Unlike Views
class LikeAndUnlikeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
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