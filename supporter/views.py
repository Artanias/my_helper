import datetime
import os
import subprocess
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import DailyReview
from .forms import DailyReviewForm, ContribCalcForm
from .static.scripts.others import calc_contrib, save_plot
from decouple import config


def index(request):
    latest_dialy_list = DailyReview.objects.order_by('-pub_date')
    context = {'title': 'Бот'}
    date = datetime.date.today()
    path_to_music = "supporter\\static\\rest_musics\\"
    path_to_video = "supporter\\static\\video\\"
    folders = os.listdir(path_to_music)

    musics = {}
    for folder in folders:
        musics[folder] = (os.listdir(path_to_music + folder))
    context['musics'] = musics
    context['folders'] = folders
    context['notices'] = os.listdir(path_to_music)
    
    # В отдельную функцию вынести на след. итерации
    if len(latest_dialy_list) == 0:
        context['publicated_today'] = False
    elif latest_dialy_list[0].pub_date == date:
        context['publicated_today'] = True
    else:
        context['publicated_today'] = False

    if request.method == 'POST':
        videos = os.listdir(path_to_video)
        if len(videos) != 0:
            warm_up_video = path_to_video + videos[0]
        else:
            warm_up_video = config('WARMUP', default='')
        timer_info = request.POST
        if 'select_folder' in timer_info.keys():
            context['select_folder'] = timer_info['select_folder']
            if 'select_music' in timer_info.keys():
                context['select_music'] = timer_info['select_music']

                path_to_music += timer_info['select_folder']
                path_to_music += "\\"
                path_to_music += timer_info['select_music']

        if 'rest_but' in timer_info.keys():
            context['timer_rest'] = True
            context['timer'] = int(timer_info['time_rest'])

            if 'notification' in timer_info.keys():
                subprocess.Popen('supporter\\static\\exe\\timer.exe '
                                 + timer_info['time_rest'] +
                                 (' \"{}\"'.format(path_to_music)))
            else:
                subprocess.Popen('supporter\\static\\exe\\timer.exe '
                                 + timer_info['time_rest']
                                 + ' -')
        elif 'work_but' in timer_info.keys():
            context['timer_work'] = True
            context['timer'] = int(timer_info['time_work'])
            if 'notification' in timer_info.keys():
                subprocess.Popen('supporter\\static\\exe\\timer.exe '
                                 + timer_info['time_work']
                                 + (' \"{}\" '.format(path_to_music))
                                 + warm_up_video)
            else:
                subprocess.Popen('supporter\\static\\exe\\timer.exe '
                                 + timer_info['time_work']
                                 + ' - '
                                 + warm_up_video)

        return render(request, 'Helper/index.html', context)

    return render(request, 'Helper/index.html', context)


def diary(request):
    latest_dialy_list = DailyReview.objects.order_by('-pub_date')
    serialized = serializers.serialize("json", latest_dialy_list)
    form = DailyReviewForm()
    date = datetime.date.today()

    context = {
        'ser_diary': serialized,
        'form': form,
        'date': date,
        'title': 'Ежедневник'
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
        'form': form,
        'title': 'Калькулятор вкладов'
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
