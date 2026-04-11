from django.urls import path
from accounts.views import ProfileView
from django.contrib.auth.decorators import login_required
app_name = 'accounts'
urlpatterns = [
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
]