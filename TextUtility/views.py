from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def View(request):
    return render(request,'textutil.html')

def remove(text):
    punc = """~`!@#$%^&*()_-+={}[]"":;\|/?.,<>"""
    new = ""
    for char in text:
        if char not in punc:
            new = new + char
    return new

def remove_space(text):
    new = ""
    text = text.strip()
    for index,char in enumerate(text):
        if index in range(len(text)-1):
            if not(text[index] == " " and text[index+1] == " "):
                new = new + char
    return new

def remove_line(text):
    new = ""
    for char in text:
        if char != "\n" and char!="\r":
            new = new + char
    #print(new)
    return new

def on_caps_lock(text):
        new = ""
        for char in text:
                new = new + char.upper()
        return new

def off_caps_lock(text):
        return text.lower()

def titlepara(text):
        return text.title()

def count_char(text):
        char_num = 0
        white_space = 0
        num =0
        punc =0
        for char in text:
                if char in "0123456789":
                        num = num+1
                elif char == " ":
                        white_space += 1
                elif char in "~`!@#$%^&*()_-+={}[]:;\|/?.,<>":
                        punc += 1
                else :
                        char_num += 1
        return char_num,white_space,num,punc

def analyze(request):
    text = request.POST['text']
    removepunc = request.POST.get('removepunc','off')
    removeextraspace = request.POST.get('removeextraspace','off')
    removeline = request.POST.get('removeline','off')
    capital =request.POST.get('upper','off')
    small = request.POST.get('lower','off')
    titled = request.POST.get('title','off')
    counting = request.POST.get('counting','off')
    if removepunc == 'on':
        result = remove(text)
        params = {'purpose':'Remove Puncutations','analyze_text':result}
        #return render(request,'utilresult.html',params)
    elif removeextraspace == 'on':
        result = remove_space(text)
        params = {'purpose':'Remove Extra Spaces','analyze_text':result}
        #return render(request,'utilresult.html',params)
    elif removeline == 'on':
        result = remove_line(text)
        params = {'purpose':'Remove Extra Spaces','analyze_text':result} 
        #return render(request,'utilresult.html',params)  
    elif capital == 'on':
        result = on_caps_lock(text)
        params = {'purpose':'Capitalize Text','analyze_text':result} 
        #return render(request,'utilresult.html',params) 
    elif small == 'on':
        result = off_caps_lock(text)
        params = {'purpose':'Capitalize Text','analyze_text':result}
        #return render(request,'utilresult.html',params)
    elif titled == 'on':
        result = titlepara(text)
        params = {'purpose':'Titled Text','analyze_text':result}   
        #return render(request,'utilresult.html',params)
    elif counting == 'on':
        r = list(count_char(text))
        result=f"""'Number of character :' {r[0]} 
'Number of spaces :' {r[1]} 
'Number of Integer :' {r[2]} 
'Number of punctuation :'{r[3]}"""
        #print(type(result))
        params = {'purpose':'counting','analyze_text':result}
    else:
        params = {'purpose':'No text to transform or you forget to switch on for transform','analyze_text':''}
    
    return render(request,'utilresult.html',params)
