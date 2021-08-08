from django.shortcuts import render,redirect
from django.conf import settings
import os


def index(request):
    items = os.listdir(settings.VIDEO_HOME_BASE_PATH)
    res = {}
    res['items_'] = items
    res['paths'] = request.path.split('/')
    return render(request, 'stuff/list.html', context={'res': res})

def icon(request):

    return redirect("/static/favicon.ico")


def getList(request):
    out_path =request.path
    if out_path.endswith(".mp4"):
        tmp = out_path.split("/")
        if tmp[1] == tmp[2]:
            tmp.pop(1)
            out_path =  "/".join(tmp)
    inline_path = os.path.join(settings.VIDEO_HOME_BASE_PATH,out_path.lstrip('/'))
    if  os.path.isdir(inline_path):
        items = os.listdir(inline_path)
        items = [ os.path.join(inline_path,it.lstrip('/')).replace(settings.VIDEO_HOME_BASE_PATH,"").replace("""\\""",'/') for it in items]
        res = {}
        res['items_'] = items
        res['paths'] = out_path.split('/')

        return render(request, 'stuff/list.html', context={'res': res})
    else:

        return render(request, 'stuff/item.html', context={'videoPath':out_path,"pathList" : out_path.split('/'),'url_prefix':settings.NGINX_VIDEO_URL_PREFIX})