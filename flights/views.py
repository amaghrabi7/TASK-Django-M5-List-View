from rest_framework.generics import ListAPIView
from flights.serializers import FlightListSerializer, BookingListSerializer
from .models import Booking, Flight
from django.utils import timezone

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class UpcomingBookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer