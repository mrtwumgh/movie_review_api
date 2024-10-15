import django_filters
from reviews.models import Review


class ReviewFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='iexact')

    class Meta:
        model = Review
        fields = ['movie_title', 'rating', 'username']