import django
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.utils import formats


class AjaxUploadInput(django.forms.FileInput):
    input_type = 'file'
    needs_multipart_form = True

    def render(self, name, value, attrs=None):
        #add class for javascript event
        attrs['class'] = 'upload'

        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        return format_html('<input {0} /><div class="upload_progress"></div>', flatatt(final_attrs))


    def value_from_datadict(self, data, files, name):
        "File widgets take data from FILES, not POST"
        return files.get(name, None)


class DateDropDownInput(django.forms.DateTimeInput):

    class Media:
        css = {
            'all': ('/static/lib/jquery.datetimepicker.css',)
        }
        js = ('/static/lib/jquery.datetimepicker.js', '/static/lib/init_datetimepicker.js')


    def _format_value(self, value):
        return formats.localize_input(value,
            self.format or formats.get_format(self.format_key)[0])


    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        if attrs is None:
            attrs = []

        attrs['class'] = 'datetimepicker'
        final_attrs = self.build_attrs(attrs, name=name)

        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))

        # return format_html(str(self.media) + '<input type="text" class="datetimepicker">')

        return format_html(str(self.media) + '<input{0} />', flatatt(final_attrs))
