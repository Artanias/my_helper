import datetime
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DailyReview
from .forms import DailyReviewForm, ContribCalcForm
from .static.scripts.others import calc_contrib, save_plot


def index(request):
    latest_dialy_list = DailyReview.objects.order_by('-pub_date')
    context = {'title': 'Главная страница'}
    date = datetime.date.today()
    context['notices'] = os.listdir(path="supporter/static/notice_sounds/")
    
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
        daily_review = DailyReview(review=review_info['review'],
                                   pub_date=date)
        daily_review.save()
        return redirect('diary')

    return render(request, 'Helper/diary.html', context)


def contrib_calc(request):
    form = ContribCalcForm()
    fields = form.fields
    fields['percentage'].initial = 5.0
    fields['years'].initial = 5
    fields['start_val'].initial = 10000
    fields['add'].initial = 5000
    context = {
        'form': form
    }

    if request.method == 'POST':
        values = request.POST
        earn = calc_contrib(percentage=float(values['percentage']),
                            years=int(values['years']),
                            start_val=int(values['start_val']),
                            add=int(values['add']),
                            capitaliz=int(values['capitaliz']))
        fields = context['form'].fields
        fields['percentage'].initial = float(values['percentage'])
        fields['years'].initial = int(values['years'])
        fields['start_val'].initial = int(values['start_val'])
        fields['add'].initial = int(values['add'])
        fields['capitaliz'].initial = int(values['capitaliz'])
        context['img'] = './static/scripts/temp.png'
        save_plot(earn, 'supporter/static/scripts/temp.png')
        summ = round(earn.iloc[int(values['years']), 0], 2)
        context['summ'] ='{0:,}'.format(summ).replace(",", " ")

    return render(request, 'Helper/contrib_calc.html', context)