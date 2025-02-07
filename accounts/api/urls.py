from django.urls import path
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.api.views import SignUpView, EmailTokenObtainPairView

urlpatterns = [
    path('', RedirectView.as_view(url='signup/', permanent=False), name='root'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]