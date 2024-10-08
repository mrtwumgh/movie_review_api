from django.urls import path
from users import views as users_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/register/', users_views.UserRegistrationView.as_view(), name='register'),
    path('api/login/', obtain_auth_token, name='login'),
    path('api/profile/', users_views.UserProfileDetailView.as_view(), name='profile'),
]