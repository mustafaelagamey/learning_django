from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
months_shorts = [mon[:3] for mon in month_numbers]
# Create your views here.

def index(request):
    return HttpResponse('Challenges Page')


def month_challenge(request,month):
    challenge = MONTHS_CHALLENGES.get(month)
    if not challenge:
        try:
            month_number = months_shorts.index(month) + 1
            return HttpResponseRedirect(reverse('month-ch-by-int',args=[month_number]))
        except ValueError:
            return HttpResponseNotFound("Unknown month")
    return HttpResponse(challenge)


def month_challenge_by_number(request,month):
    if 0 < month < 13:
        challenge = MONTHS_CHALLENGES.get(month_numbers[month - 1])
    else:
        return HttpResponseNotFound("Unknown month number")
    return HttpResponse(challenge)
