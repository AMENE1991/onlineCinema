from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Film, Review
from .serializers import FilmSerializer, ReviewSerializer


class FilmListCreate(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetailView(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer




class ReviewListCreate(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class 

# Create your views here.
