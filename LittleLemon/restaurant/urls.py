#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('reservations/', views.reservations, name="reservations"),
    # API paths
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]