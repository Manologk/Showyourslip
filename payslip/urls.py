from django.urls import path
from .views import PayslipListView, PayslipUploadView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('upload/', PayslipUploadView.as_view(), name='upload_payslip'),
    path('list/', PayslipListView.as_view(), name='list_payslip'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]