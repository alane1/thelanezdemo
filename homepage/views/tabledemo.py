from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from lib.table import Table
from django.contrib.auth.models import User

from datetime import datetime

@view_function
def process_request(request):

    ### make it so initial page can be set with urlparams?
    pageNum = 0

    template_vars = {
        'now': datetime.now(),
        'pageNum': pageNum
    }

    return dmp_render_to_response(request, 'tabledemo.html', template_vars)


@view_function
def get_table(request):
    fullQry = User.objects.all().order_by('id')#.order_by('first_name')#.filter(first_name='asdf')

    table = UserTable(request, fullQry)
    table.paginate(request)

    if table.qry.count() == 0: #does this run the full qry? (that would be bad)
        'No Records Returned'

    template_vars = {
        'now': datetime.now(),
        'table': table,
    }

    return dmp_render_to_response(request, 'tabledemo.get_table.html', template_vars)


class UserTable(Table):
    headers = [ 'First Name', 'Last Name', 'Email' ]
    fields = ['first_name', 'last_name', 'email']

    endpoint = '/homepage/tabledemo.get_table/'
    rows_per_page = 5
