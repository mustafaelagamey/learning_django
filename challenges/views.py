from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
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

def generate_month_links(num , month):
    return f"""
<li>
    <a href="{reverse('month-ch-by-int', args=[num])}">{num}</a> 
    <a href="{reverse('month-ch', args=[month])}">{month}</a> 
    <a href="{reverse('month-ch', args=[month[:3]])}">{month[:3]}</a>
</li>
    """


def index(request):
    links = []
    for i,month in enumerate(month_numbers):
        links.append(generate_month_links(i+1,month))

    if links :
        links_text = f"<ul>{''.join(links)}</ul>"
        return HttpResponse("Monthly challenges :" + links_text)


def month_challenge(request,month):
    challenge = MONTHS_CHALLENGES.get(month)
    if not challenge:
        try:
            month_number = months_shorts.index(month) + 1
            return HttpResponseRedirect(reverse('month-ch-by-int',args=[month_number]))
        except ValueError:
            return HttpResponseNotFound(render_to_string('challenges/unknown_month.html'))
    return HttpResponse(challenge)


def month_challenge_by_number(request,month):
    if 0 < month < 13:
        challenge = MONTHS_CHALLENGES.get(month_numbers[month - 1])
    else:
        return HttpResponseNotFound("Unknown month number")
    return HttpResponse(challenge)
