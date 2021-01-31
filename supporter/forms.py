from .models import DailyReview
from django.forms import ModelForm, Textarea

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
