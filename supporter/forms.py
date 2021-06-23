from .models import DailyReview
from django.forms import ModelForm, Textarea, Form
from django.forms import ChoiceField, IntegerField, FloatField


class DailyReviewForm(ModelForm):
    class Meta:
        model = DailyReview
        fields = ["review"]
        widgets = {"review": Textarea(attrs={
                                                'class': 'form-control',
                                                'placeholder': 'Описание сегодняшнего дня',
                                                'cols': 150
                                            })
                  }


class ContribCalcForm(Form):
    percentage = FloatField(max_value=100, min_value=0,
                            help_text="Процентная ставка")
    percentage.widget.attrs.update(style="margin: 5px; width: calc(100vw / 12);")
    years = IntegerField(max_value=200, min_value=1,
                         help_text="Количество лет")
    years.widget.attrs.update(style="margin: 5px; width: calc(100vw / 12);")
    start_val = IntegerField(min_value=1, help_text="Начальный вклад")
    start_val.widget.attrs.update(style="margin: 5px; width: calc(100vw / 10);")
    add = IntegerField(min_value=0,
                       help_text="Сумма ежемесячного пополнения")
    add.widget.attrs.update(style="margin: 5px; width: calc(100vw / 10);")
    capitaliz = ChoiceField(choices=[(0, 'Ежемесячно'),
                                     (1, 'Ежеквартально'),
                                     (2, 'Раз в пол года'),
                                     (3, 'Ежегодно')],
                            help_text="Капитализация")
    capitaliz.widget.attrs.update(style="margin: 5px;")
