from django.contrib import admin

from .models import DailyDo
from .models import PwdInfo

admin.site.register(DailyDo)
admin.site.register(PwdInfo)

