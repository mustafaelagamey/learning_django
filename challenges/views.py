from django.http import HttpResponse, HttpResponseNotFound
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
month_numbers = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'August', 'september', 'october',
                 'november', 'december']
# Create your views here.

def index(request):
    return HttpResponse('Challenges Page')


def month_challenge(request,month):
    challenge = MONTHS_CHALLENGES.get(month)
    if not challenge:
        return HttpResponseNotFound("Unknown month")
    return HttpResponse(challenge)


def month_challenge_by_number(request,month):
    if 0 < month < 13:
        challenge = MONTHS_CHALLENGES.get(month_numbers[month - 1])
    else:
        return HttpResponseNotFound("Unknown month number")
    return HttpResponse(challenge)
