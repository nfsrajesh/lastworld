from django.shortcuts import render

def custom404(request,exception):

    return render(request,"myapp/404.html",status=404)

def custom500(request):

    return render(request,"myapp/500.html",status=500)