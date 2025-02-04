"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights.views import BookingDeleteView, BookingDetailUpdateDeleteView, BookingDetailView, BookingUpdateView, FlightListView, UpcomingBookingListView, BookingCreateView
from users.views import RegisterAPIView, UserLoginAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", FlightListView.as_view(), name="flights_list"),
    path("upcoming-bookings/", UpcomingBookingListView.as_view(), name="upcoming_bookings_list"),
    path("book/<int:flight_id>/", BookingCreateView.as_view(), name="book_flight"),
    path("bookings/<int:booking_id>/", BookingDetailView.as_view(), name="booking_details"),
    path("bookings/<int:booking_id>/edit/", BookingUpdateView.as_view(), name="update_booking"),
    path("bookings/<int:booking_id>/cancel/", BookingDeleteView.as_view(), name="cancel_booking"),
    path("bookings/<int:booking_id>/view-edit-cancel/", BookingDetailUpdateDeleteView.as_view(), name="detail_update_cancel_booking"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),

]
