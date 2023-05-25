from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse

# Create your views here.

class cbv(TemplateView):
    template_name='cbv.html'

    def get_context_data(self, **kwargs):
        EDVO=super().get_context_data(**kwargs)
        EDVO['name']='Thilak Chandhra'
        EDVO['age']='23'
        EDVO['qualification']='MCA'
        return EDVO
    
class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs):
        EDFO=super().get_context_data(**kwargs)
        TFO=TopicForm()
        EDFO['TFO']=TFO
        return EDFO
    
    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data is inserted!....')