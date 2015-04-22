from django.conf import settings
from django import forms
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django.http import HttpResponse
from lib import widgets
import os.path

from datetime import datetime

@view_function
def process_request(request):

    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            # use upload_fullname to tie model to file
            print(form.cleaned_data['upload_fullname'])
            form = UploadForm()

    template_vars = {
        'form': form,
        'now': datetime.now(),
    }

    return dmp_render_to_response(request, 'uploader.html', template_vars)

@view_function
def upload(request):

    fullname = ''

    if request.method == 'POST':
        uploadfile = request.FILES['uploadfile']
        # get save location name
        fullname = os.path.join('/temp/uploaded_files', uploadfile.name)

        # save file
        with open(request.FILES['uploadfile'].name, 'wb') as destination:
            print('test')
            for chunk in uploadfile.chunks():
                destination.write(chunk)

        ### alternate save method
        # f = open(request.FILES['uploadfile'].name, 'wb')
        # f.write(request.FILES['uploadfile'])
        # f.close()

    return HttpResponse(fullname)


class UploadForm(forms.Form):
    user_name = forms.CharField()
    upload_fullname = forms.CharField(widget=forms.HiddenInput())
    upload = forms.FileField(widget=widgets.AjaxUploadInput(), required=False)
