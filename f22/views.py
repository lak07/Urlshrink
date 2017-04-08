from .forms import PostForm
import webbrowser
from .urlshorten import ShortenURL
from django.shortcuts import render
Surl='None'
response=''
def post_new(request):
    Surl='None'
    form = PostForm() 
    link=ShortenURL()
    response=request.GET.get('Url')
    if response is not None and response.startswith('lakshay.ly/') :
        ori=link.getoriurl(response.split('/')[1])
        if ori=="No Record exist for given short url":
            return render(request, 'f22/base.html', {'form':form,'Surled': 'No Record exist for given short url'})
        else:
          if ori.startswith('http'):
              webbrowser.open_new_tab(ori)
          else:
              webbrowser.open_new_tab('http://'+ori)
          Surl='None'
    elif response is not None:
       sid=link.inserturl(response)
       Surl='lakshay.ly/'+link.createurl(int(sid))
    return render(request, 'f22/base.html', {'form':form,'Surled': Surl})
