from django.shortcuts import render

# Create your views here
def moviesInfo(request):
    my_dict={'head_msg':'Movies Information',
             'sub_msg1':'sonali slowly getting cured',
            'sub_msg2' : '  Bahubali -3 is just planning',
            'sub_msg3' :'Salman khan ready to marriage',
            'photo'  :'images/sunny.jpg'   }
    return render(request,'newsapp/news.html',context=my_dict)
def sportsInfo(request):

    my_dict={'head_msg':'sports Information',
                 'sub_msg1':'anushka sharma firing like any thing',
                'sub_msg2' : '  Bahubali -3 is just planning',
                'sub_msg3' :'Worst performance by india-shaswat',
                   }
    return render(request,'newsapp/news.html',context=my_dict)

def politicsInfo(request):

    my_dict={'head_msg':'Politics Information',
             'sub_msg1':'Acche din aa gaye',
            'sub_msg2' : '  Bahubali -3 is just planning',
            'sub_msg3' : 'modi is jumlaman-Rahul Gandhi',
                  }
    return render(request,'newsapp/news.html',context=my_dict)

def index(request):
    return render(request,'newsapp/index.html')
