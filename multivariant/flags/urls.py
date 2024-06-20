from django.urls import path
from .views import FeatureFlagView

urlpatterns = [
    path('feature-flag/<str:user_email>/', FeatureFlagView.as_view(), name='feature-flag'),
]
