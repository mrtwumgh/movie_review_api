from django.contrib import admin
from reviews.models import Review, ReviewLike


admin.site.register(Review)
admin.site.register(ReviewLike)