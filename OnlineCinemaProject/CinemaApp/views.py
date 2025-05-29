from django.shortcuts import render
from rest_framework import generics
from .models import Film, Review
from .serializers import FilmSerializer, ReviewSerializer


class FilmListCreate(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Create your views here.
