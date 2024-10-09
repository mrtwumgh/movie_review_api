from django.urls import path
from comments import views as comment_views


urlpatterns = [
    path('api/reviews/<int:review_id>/comments/', comment_views.CommentListAPIView.as_view(), name='comment-list'),
    path('api/reviews/<int:review_id>/comments/create/', comment_views.CommentCreateView.as_view(), name='comment-create'),
    path('api/comments/<int:pk>/', comment_views.CommentDetailView.as_view(), name='comment-detail'),
    path('api/comments/<int:pk>/update/', comment_views.CommentUpdateView.as_view(), name='comment-update'),
    path('api/comments/<int:pk>/delete/', comment_views.CommentDeleteView.as_view(), name='comment-delete'),
]