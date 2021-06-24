
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from . import models, forms, settings
import requests
import time, datetime

def start(request):
    if request.POST:
        form=request.POST
        if len(form):
            form=dict(form)
            c_happening=form['c_happening'][0]
            c_start=form['c_start'][0]
            c_status=form['c_status'][0]
            channel=form['channel'][0]
            channel=models.Channel.objects.filter(title=channel)[0]
            models.CountDown(c_status=c_status,c_happening=c_happening,c_start=c_start,channel=channel).save()
            time.sleep(2)
            # if settings.error==True:
            #     error="da stimmt was nicht"
            #     countdown_form=forms.CountDownForm()
            #     all_channels=models.Channel.objects.all()
            #     context={'channels': all_channels, 'countdown_form':countdown_form, 'error':error} #, 'countdowns': countdowns}
            #     return render(request,'index.html',context)
            # else:
            #     error=None
            return HttpResponseRedirect('/')
    else:
        error=None
        countdown_form=forms.CountDownForm()
        all_channels=models.Channel.objects.all()
        context={'channels': all_channels, 'countdown_form':countdown_form, 'error':error} 
        return render(request,'index.html',context)


def delete_countdown(request,pk):
    countdown_to_delete=models.CountDown.objects.get(id=pk)
    countdown_to_delete.c_status="deleting"
    countdown_to_delete.save()
    return HttpResponseRedirect('/')

#### Die hier brauch ich noch
# def error_view(request):
#     countdown_form=forms.CountDownForm()
#     all_channels=models.Channel.objects.all()
#     error="da lief was schief"
#     print("errorVIew+++++++++++++++++++++++++++++++++++++")
#     context={'channels': all_channels, 'countdown_form':countdown_form, 'error': error} #, 'countdowns': countdowns}
#     return render(request,'index.html',context)

