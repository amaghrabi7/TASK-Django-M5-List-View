from rest_framework.generics import ListAPIView, RetrieveAPIView
from flights.serializers import BookingDetailSerializer, FlightListSerializer, BookingListSerializer
from .models import Booking, Flight
from django.utils import timezone

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class UpcomingBookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
