from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
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
    'december':'',
}
month_numbers = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'August', 'september', 'october',
                 'november', 'december']
# Create your views here.


def index(request):
    return render(request, 'challenges/index.html', {'month_numbers': month_numbers})


def month_challenge(request,month):
    challenge = MONTHS_CHALLENGES.get(month)
    if challenge is None:
        return render(request, '404.html')
    return render(request, 'challenges/month_challenge.html', {'challenge': challenge, 'access_method':'full month name'})


def month_challenge_by_number(request,month):
    if 0 < month < 13:
        challenge = MONTHS_CHALLENGES.get(month_numbers[month - 1])
    else:
        raise Http404
    return render(request, 'challenges/month_challenge.html', {'challenge': challenge, 'access_method': 'month number'})
