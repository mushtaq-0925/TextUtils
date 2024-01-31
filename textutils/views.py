from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalise = request.POST.get('capitalise','off')
    spaceremove= request.POST.get('spaceremove','off')
    newlineremover = request.POST.get('newlineremover','off')
    charcount= request.POST.get('charcount','off')

    if removepunc == 'on':
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed

    if capitalise == 'on':
        analyzed=''
        for char in djtext:
            analyzed += char.upper()

        params = {'purpose':'capitalised', 'analyzed_text':analyzed}
        djtext=analyzed
    
    if spaceremove== 'on':
        analyzed=''
        for index in range(len(djtext)-1): 
            if not(djtext[index] ==' ' and djtext[index+1] ==' '):
                analyzed += djtext[index]

        params = {'purpose':'spaceremove', 'analyzed_text':analyzed}
        djtext=analyzed

    if newlineremover =='on':
        analyzed=''
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed += char

        params = {'purpose':'NewLine Removed', 'analyzed_text':analyzed}
        djtext=analyzed
    
    if charcount=='on':
        set1=set(djtext)
        analyzed={}
        for i in set1:
            a=djtext.count(i)
            analyzed[i]=a

        params = {'purpose':'charcount', 'analyzed_text':analyzed}
        djtext=analyzed

    if(removepunc != "on" and capitalise != 'on' and newlineremover != 'on' and spaceremove != 'on' and charcount != 'on'):
        return HttpResponse('please selcet any option to analyze your text:')

    return render(request, 'analyze.html', params)