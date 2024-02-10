from django.shortcuts import render

def home(request):
    return render(request,'input.html')
def calculate(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    operation=request.GET["op"]
    res=None
    if operation=="add":
        res="THE SUM IS: "+str(x+y)
    elif operation=="sub":
        res="THE SUB IS: "+str(x-y)
    elif operation=="mul":
        res="THE MUL IS: "+str(x*y)
    else:
        res="THE DIV IS: "+str(x/y)
    con_dict={"result":res}
    return render(request,template_name='result.html',context=con_dict)


