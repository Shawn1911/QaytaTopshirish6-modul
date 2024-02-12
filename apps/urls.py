from django.urls import path

from apps.views import IndexView, AdCreateView, AdDeleteView, AdUpdateView, CustomLoginView, RegisterFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('create/', AdCreateView.as_view(), name='create'),
    path('delete/<int:pk>', AdDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', AdUpdateView.as_view(), name='update'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterFormView.as_view(), name='register'),
]
