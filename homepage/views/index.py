from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response

from datetime import datetime

@view_function
def process_request(request):


  print('<><><><><><><><><><><><><><>')
  topic = None
  endpoint_url = '/forum/index.get_table/%s' % (topic if topic else '')

  print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
  print(endpoint_url)

  if topic:
      endpoint_url2 = '/forum/index.get_table/%s' % topic
  else:
      endpoint_url2 = '/forum/index.get_table/'

  print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
  print(endpoint_url2)

  template_vars = {
    'now': datetime.now(),
  }
  return dmp_render_to_response(request, 'index.html', template_vars)
