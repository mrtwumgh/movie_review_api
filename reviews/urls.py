from django.urls import path
from reviews import views as review_views


urlpatterns = [
    path('api/reviews/', review_views.ReviewListView.as_view(), name='review-list'),
    path('api/reviews/create/', review_views.ReviewCreateView.as_view(), name='review-create'),
    path('api/reviews/<int:pk>/', review_views.ReviewDetailView.as_view(), name='review-detail'),
    path('api/reviews/<int:pk>/update/', review_views.ReviewUpdateView.as_view(), name='review-update'),
    path('api/reviews/<int:pk>/delete/', review_views.ReviewDeleteView.as_view(), name='review-delete'),
]