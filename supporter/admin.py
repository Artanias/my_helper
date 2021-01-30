from django.contrib import admin

from .models import DailyReview, Task

admin.site.register(DailyReview)
admin.site.register(Task)
