from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.safestring import mark_safe

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
    return render(request, 'challenges/index.html', {'month_numbers': month_numbers})


def month_challenge(request,month):
    challenge = MONTHS_CHALLENGES.get(month)
    if not challenge:
        return render(request, 'challenges/unknown_month.html')
    return render(request, 'challenges/month_challenge.html', {'text': challenge, 'access_method':'full month name'})


def month_challenge_by_number(request,month):
    if 0 < month < 13:
        challenge = MONTHS_CHALLENGES.get(month_numbers[month - 1])
    else:
        return HttpResponseNotFound("Unknown month number")
    return HttpResponse(challenge)
