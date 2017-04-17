from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from f22.models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .urlshorten import ShortenURL
from django.shortcuts import render,redirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

Surl='None'
response=''
def post_new(request):
    Surl='None'
    form = PostForm() 
    link=ShortenURL()
    response=request.GET.get('Url')
    val = URLValidator(verify_exists=False
    try:
        val('http://www.google.com')
    except ValidationError, e:
          return render(request, 'f22/base.html', {'form':form,'Surled': 'Url entered is not valid'})
    if response is not None:
       sid=link.inserturl(response)
       Surl='https://urlshrink.herokuapp.com/'+link.createurl(int(sid))
    return render(request, 'f22/base.html', {'form':form,'Surled': Surl})

def post_redr(request):
        Url = request.get_full_path()
        Surl='None'
        form = PostForm() 
        link=ShortenURL()
        if Url is not None :
          ori=link.getoriurl(Url.split('/')[1])
          if ori=="No Record exist for given short url":
            return render(request, 'f22/base.html', {'form':form,'Surled': 'No Record exist for given short url'})
          else:
            if ori.startswith('http'):
              return redirect(ori)
            else:
              return redirect('http://'+ori)
            Surl='None'
        return render(request, 'f22/base.html', {'form':form,'Surled': Surl})
