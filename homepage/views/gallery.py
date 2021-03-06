from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from homepage import models as hmod

from datetime import datetime

@view_function
def process_request(request):

  galleryImages = hmod.GalleryImage.objects.all()

  template_vars = {
    'now': datetime.now(),
    'galleryImages': galleryImages,
  }
  return dmp_render_to_response(request, 'gallery.html', template_vars)
