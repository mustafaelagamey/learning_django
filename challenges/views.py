from django.http import HttpResponse
from django.shortcuts import render

MONTHS_CHALLENGES = {
    'january':'Jan challenge',
    'february':'Feb challenge',
    'march':'Mar challenge',
    'april':'Apr challenge',
    'may':'May challenge',
    'june':'Jun challenge',
    'july':'Jul challenge',
    'August':'Aug challenge',
    'september':'Sep challenge',
    'october':'Oct challenge',
    'november':'Nov challenge',
    'december':'Dec challenge',
}
# Create your views here.

def index(request):
    return HttpResponse('Challenges Page')


def month_challenge(request,month):
    challenge = MONTHS_CHALLENGES.get(month)
    return HttpResponse(challenge)
