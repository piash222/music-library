from django.http import HttpResponse


def redirect(request):
    return HttpResponse("<p>Direction to App : <a href='music'>Music</a></p>")