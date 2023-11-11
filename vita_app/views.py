from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from vita_app.services import read_worksheet, write_worksheet
from vita_app.bot import bot_notification
from vita_app.entities import times
import asyncio


def index(request: HttpRequest):
    if (request.method == 'POST'):
        if request.POST.get('select_month'):
            request.session['month'] = request.POST['select_month']
            request.session['day'] = request.POST['select_day']
            request.session['event'] = request.POST['select_event']
        else:
            request.session['first_name'] = request.POST['first_name']
            request.session['last_name'] = request.POST['last_name']
            request.session['phone'] = request.POST['phone']
            if write_worksheet(
                request.session['month'],
                request.session['day'],
                list(times.keys())[list(times.values()).index(request.session['event'])],
                request.session['phone']
            ):
                asyncio.run(bot_notification(
                    request.session['first_name'],
                    request.session['last_name'],
                    request.session['phone'],
                    request.session['month'],
                    request.session['day'],
                    request.session['event']
                ))
            return render(request, 'vita_app/modal.html')
    return render(request, 'vita_app/index.html')


def load_data(request: HttpRequest):
    months = months_from_db = read_worksheet()
    for month in months:
        for day in month.days:
            day.events = [event for event in day.events if event.is_free]
        month.days = [day for day in month.days if day.is_free]
    json_months = [month.to_dict() for month in months]

    return JsonResponse(json_months, safe=False)


def page_not_found(request: HttpRequest, exception):
    return render(request, 'vita_app/404.html')
