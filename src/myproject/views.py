from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def merge_pdf(request):
    return render(request, "tools.html", {"page": "merge"})
