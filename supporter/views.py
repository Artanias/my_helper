import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyReview
from .forms import DailyReviewForm


def index(request):
    latest_dialy_list = DailyReview.objects.order_by('-pub_date')
    context = {'title': 'Главная страница'}
    date = datetime.date.today()
    
    # В отдельную функцию вынести на след. итерации
    if len(latest_dialy_list) == 0:
        context['publicated_today'] = False
    elif latest_dialy_list[0].pub_date == date:
        context['publicated_today'] = True
    else:
        context['publicated_today'] = False

    return render(request, 'Helper/index.html', context)

def diary(request):
    latest_dialy_list = DailyReview.objects.order_by('-pub_date')
    form = DailyReviewForm()
    date = datetime.date.today()

    context = {
        'diary': latest_dialy_list,
        'form': form,
        'date': date
    }

    if len(latest_dialy_list) == 0:
        context['publicated_today'] = False
    elif latest_dialy_list[0].pub_date == date:
        context['publicated_today'] = True
    else:
        context['publicated_today'] = False

    if request.method == 'POST':
        review_info = request.POST
        print(review_info)

    return render(request, 'Helper/diary.html', context)