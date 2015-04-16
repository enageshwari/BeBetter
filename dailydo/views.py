from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from dailydo.forms import DailyDoForm
from dailydo.models import DailyDo, PwdInfo
from django import forms
from Crypto.Cipher import AES
import base64
import datetime
from datetime import date, timedelta


MASTER_KEY="Some-long-base-key-to-use-as-encyrption-key"
	
# Create your views here.


def disp(request):
	return HttpResponse("Your data has been saved")

def activity_entry(request):
    # sticks in a POST or renders empty form
	try:
    		today_do = DailyDo.objects.get(pk=date.today())
	except DailyDo.DoesNotExist:
		form = DailyDoForm(initial={'date_info_date': date.today()},label_suffix="")
		form.fields['date_info_date'].widget = forms.HiddenInput()
		return render_to_response('dailydo/activity_entry.html',
				      {'activity_form': form, 'today_date':str(date.today())},
				      context_instance=RequestContext(request))
	else:

	    form = DailyDoForm(None, instance=today_do,label_suffix="")	
            form.fields['date_info_date'].widget = forms.HiddenInput()
	    return render_to_response('dailydo/activity_entry.html',
				      {'activity_form': form, 'today_date':str(date.today())},
				      context_instance=RequestContext(request))



def save(request):
	try:
    		today_do = DailyDo.objects.get(pk=date.today())
	except DailyDo.DoesNotExist:
	    form = DailyDoForm(request.POST,label_suffix="")

	else:
	    form = DailyDoForm(request.POST, instance=today_do, label_suffix="")	
	finally:
		if form.is_valid():
			form.fields['date_info_date'].widget = forms.HiddenInput()
			cmodel = form.save()
			cmodel.save()
#			return redirect(disp)
			return render_to_response('dailydo/disp.html',
				      {'activity_form': form, 'today_date':str(date.today()), 'msg': 'Data is saved!',  'backto':'/bebetter/' },
				      context_instance=RequestContext(request))
		else:
			return render_to_response('dailydo/disp.html',
				      {'activity_form': form, 'today_date':str(date.today()), 'msg': 'Error! Data is not saved!' ,  'backto':'/bebetter/'},
				      context_instance=RequestContext(request))

def yesterday(request):
    # sticks in a POST or renders empty form
	try:
		yest_date = date.today() - timedelta(1)
    		today_do = DailyDo.objects.get(pk=yest_date)
	except DailyDo.DoesNotExist:
		form = DailyDoForm(initial={'date_info_date': yest_date},label_suffix="")
		form.fields['date_info_date'].widget = forms.HiddenInput()
		return render_to_response('dailydo/yesterday.html',
				      {'activity_form': form, 'today_date':str(yest_date)},
				      context_instance=RequestContext(request))
	else:

	    form = DailyDoForm(None, instance=today_do,label_suffix="")	
            form.fields['date_info_date'].widget = forms.HiddenInput()
	    return render_to_response('dailydo/yesterday.html',
				      {'activity_form': form, 'today_date':str(yest_date)},
				      context_instance=RequestContext(request))



def save_yest(request):
	try:
		yest_date = date.today() - timedelta(1)
		print str(yest_date)
    		today_do = DailyDo.objects.get(pk=yest_date)
	except DailyDo.DoesNotExist:

	    form = DailyDoForm(request.POST,label_suffix="")

	else:

	    form = DailyDoForm(request.POST, instance=today_do, label_suffix="")	
	finally:

		if form.is_valid():

			form.fields['date_info_date'].widget = forms.HiddenInput()
			cmodel = form.save()
			cmodel.save()
#			return redirect(disp)
			return render_to_response('dailydo/disp.html',
				      {'activity_form': form, 'today_date':yest_date, 'msg': 'Data is saved!', 'backto':'/bebetter/yesterday/' },
				      context_instance=RequestContext(request))
		else:

			return render_to_response('dailydo/disp.html',
				      {'activity_form': form, 'today_date':yest_date, 'msg': 'Error! Data is not saved!',  'backto':'/bebetter/yesterday/' },
				      context_instance=RequestContext(request))
def cal(request):
	mon = datetime.datetime.now().month
	yr = datetime.datetime.now().year
        history_list = DailyDo.objects.filter(date_info_date__year=yr,date_info_date__month=mon).order_by('-date_info_date')

	return render_to_response('dailydo/cal.html',{'month':str(mon),'year':str(yr),'history_list': history_list, }, context_instance=RequestContext(request))


def authenticate(request):
	return render_to_response('dailydo/pass_chk.html',{"pass": "pass",},
				      context_instance=RequestContext(request))

def history(request):



    try:
	clear_text=request.POST["passwd1"]
	enc_secret = AES.new(MASTER_KEY[:32])
	tag_string = (str(clear_text) +
		  (AES.block_size -
		   len(str(clear_text)) % AES.block_size) * "\0")
	cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
	print 'Encrypted pwd:', cipher_text

        hist_pwd = PwdInfo.objects.get(pk='history')
    except PwdInfo.DoesNotExist:
	print 'hist no'
        mon = datetime.datetime.now().month
        yr = datetime.datetime.now().year
        history_list = DailyDo.objects.filter(date_info_date__year=yr,date_info_date__month=mon).order_by('-date_info_date')
        return render_to_response('dailydo/history.html',
                                  {'month':str(mon),'year':str(yr),'history_list': history_list,'disp_type':'first', 'acty_list':'all'},
                                  context_instance=RequestContext(request))
    else:
	print 'hist yes'

        
	if cipher_text == hist_pwd.pwd_text:

		mon = datetime.datetime.now().month
		yr = datetime.datetime.now().year
		history_list = DailyDo.objects.filter(date_info_date__year=yr,date_info_date__month=mon).order_by('-date_info_date')
		return render_to_response('dailydo/history.html',{'month':str(mon),'year':str(yr),'history_list': history_list, 'pwd': cipher_text, 'disp_type':'first', 'acty_list':'all' }, context_instance=RequestContext(request))
        else:
		return redirect(authenticate)

def show_history(request):
	print 'selected activities:', request.POST.getlist("acty_list1")
	acty_list = request.POST.getlist("acty_list3")
	mon = int('0'+request.POST["month"])
	yr = int('0'+request.POST["year"])
	history_list = DailyDo.objects.filter(date_info_date__year=yr,date_info_date__month=mon).order_by('-date_info_date')
	return render_to_response('dailydo/history.html',{'month':str(mon),'year':str(yr),'history_list': history_list, 'acty_list':acty_list, 'disp_type':'subsequent' }, context_instance=RequestContext(request))

 


