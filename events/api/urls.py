from django.urls import path, include
from events.api.views import (
    EventListAPIView,
    EventDetailAPIView,
    EventUpdateAPIView,
    EventDeleteAPIView,
    EventCreateAPIView
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', EventListAPIView.as_view(), name='api-home'),
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='api-event-detail'),
    path('event/new/', EventCreateAPIView.as_view(), name='api-event-create'),
    path('event/<int:pk>/update/', EventUpdateAPIView.as_view(), name='api-event-update'),
    path('event/<int:pk>/delete/', EventDeleteAPIView.as_view(), name='api-event-delete'),
    # path('events/', users_views.event, name='event'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('register/', users_views.register, name='register'),
    path('users/', include('users.api.urls')),
]