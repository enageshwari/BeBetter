from django.forms import ModelForm, Textarea
from dailydo.models import DailyDo
from django.utils.translation import ugettext_lazy as _

class DailyDoForm(ModelForm):

    class Meta:
        model = DailyDo
	fields = ['date_info_date', 'gratitude1_text', 'gratitude2_text', 'gratitude3_text','positive_exp_text','exercise_bool','meditation_bool','kind_act_text']
	labels = {
	"date_info_date": _("Today's Date"),
	"gratitude1_text": _("Gratitude"),
	"gratitude2_text": _(" "),
	"gratitude3_text": _(" "),
	"positive_exp_text": _("Positive Experience"),
	"exercise_bool": _("Exercise"),
	"meditation_bool": _("Meditation"),
	"kind_act_text": _("Act of Kindness"),
	}
        widgets = {
            "gratitude1_text": Textarea(attrs={'cols': 40, 'rows': 8}),
        }


