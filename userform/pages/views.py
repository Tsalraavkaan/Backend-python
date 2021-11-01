from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .forms import UserForm

USER_BASE = {"surname" : [],
            "name" : [],
            "age" : [],
            "study" : [],
            "email" : []}

def get_data(ind):
    return {"surname" : USER_BASE["surname"][ind],
            "name" : USER_BASE["name"][ind],
            "age" : USER_BASE["age"][ind],
            "study" : USER_BASE["study"][ind],
            "email" : USER_BASE["email"][ind]}

def form(request):
    if request.method == "POST":
        USER_BASE["surname"].append(request.POST.get("surname"))
        USER_BASE["name"].append(request.POST.get("name"))
        USER_BASE["age"].append(request.POST.get("age"))
        USER_BASE["study"].append(request.POST.get("place_of_studying"))
        USER_BASE["email"].append(request.POST.get("email"))
        data = get_data(-1)
        return render(request,  "data.html", data)
    elif request.method == "GET":
        name = request.GET.get("name", None)
        if not name:
            userform = UserForm()
            return render(request, "form.html", {"form": userform})
        for ind, elem in enumerate(USER_BASE["name"]):
            if elem == name:
                data = get_data(ind)
                return render(request,  "data.html", data)
        raise Http404
    else:
        raise Http404
def info(request):
    return render(request,  "data_all.html", USER_BASE)