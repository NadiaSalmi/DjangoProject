from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = ' /music/' + str(album.id)
        html += '<a href ="' + url + '">' + album.album_title + '</a></br>'

    return HttpResponse(html)


"""def index(request):
    return HttpResponse("<h1>This will be a list of albums </h1>")"""


def details(request, album_id):
    return HttpResponse("<h1>Details of album id: " + str(album_id) + "<h1>")
