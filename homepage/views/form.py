from django import forms
from lib import customform
from lib import widgets
from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from homepage import models as hmod

from datetime import datetime

@view_function
def process_request(request):

    if request.method == "POST":
        form = TestForm(request, request.POST)
        if form.is_valid():
            form.commit()
            # user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            # if user.is_active == False:
            #     return HttpResponseRedirect('/account/inactive/' + str(user.id))

    else:
        form = TestForm(request)

    ### get past notes
    notes = hmod.Note.objects.all().order_by('-dateTime')

    template_vars = {
        'now': datetime.now(),
        'form': form,
        'notes': notes,
    }

    return dmp_render_to_response(request, 'form.html', template_vars)




class TestForm(customform.CustomForm):

    def init(self):
        self.fields['name'] = forms.CharField(max_length=30)
        self.fields['content'] = forms.CharField(widget=forms.Textarea, max_length=200)
        self.fields['email'] = forms.EmailField()
        # self.fields['dateTime'] = forms.DateTimeField(widget=widgets.DateDropDownInput(format = '%Y-%m-%d %H:%M'), initial=datetime.now()) #widget=DateDropDownInput, max_length=30)
        self.fields['dateTime'] = forms.CharField(widget=widgets.AjaxUploadInput(format = '%Y-%m-%d %H:%M'), initial=datetime.now()) #widget=DateDropDownInput, max_length=30)

    def commit(self):
        note = hmod.Note()
        note.name = self.cleaned_data['name']
        note.content = self.cleaned_data['content']
        note.email = self.cleaned_data['email']
        note.dateTime = self.cleaned_data['dateTime']
        note.save()

    ### convert the datepicker input into a datetime object
    # def clean(self):
    #     print('1111111111111111111111111111111111111111111')
    #     data = self.cleaned_data['dateTime']
    #     self.cleaned_data['dateTime'] = time.strptime(data, '%Y-%m-%d %H:%M')

        # try:
        #     self.cleaned_data['dateTime'] = time.strptime(data, '%Y-%m-%d %H:%M')
        # except:
        #     raise forms.ValidationError("Please use the date picker to select a date")

        # return data
