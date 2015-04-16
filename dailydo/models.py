from django.db import models
from django.forms import ModelForm

# Create your models here.

class DailyDo(models.Model):
    date_info_date = models.DateField(primary_key=True) #todays date
    gratitude1_text = models.CharField(max_length=500, blank=True)
    gratitude2_text = models.CharField(max_length=500, blank=True)
    gratitude3_text = models.CharField(max_length=500, blank=True)
    positive_exp_text = models.CharField(max_length=500, blank=True)
    exercise_bool = models.BooleanField(default=False)
    meditation_bool = models.BooleanField(default=False, blank=True)
    kind_act_text = models.CharField(max_length=500, blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.date_info_date)

class PwdInfo(models.Model):
    pwd_purpose_text = models.CharField(max_length=50, blank=True, primary_key=True)
    pwd_text = models.CharField(max_length=500, blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.pwd_purpose_text)



