import django

#######################################
####  Custom Form class
####  - started with Conan Albrecht code from jr. core

class CustomForm(django.forms.Form):
    '''documentation'''

    multipartForm = False

    hiddenFields = []

    submitButtonHtml = '<button type="submit" class="btn btn-default">Submit</button>'

    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.form_id = request.generator()

        super().__init__(*args, **kwargs)
        self.init()


    def init(self):
        # define fields here - in each form that extends customform
        pass

    def commit(self):
        # set this in the form that extends customform
        pass

    def html_escape(text):
        text = text.replace('&', '&amp;')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&#39;')
        text = text.replace(">", '&gt;')
        text = text.replace("<", '&lt;')
        return text


    def format_attrs(attrs):
        '''Flattens a dict of attributes for an html tag'''
        flat = []
        for key, val in attrs.items():
            if val != None:
                  flat.append('%s="%s"' % (key, html_escape(val)))
            return ' '.join(flat)


    ### Html for table
    def as_full(self, width=None, align=None):
        '''return Html of this form as a table'''

        html = []

        # html.append('<form %s>' % format_attrs({
        #     'id': id,
        #     'method': 'post',
        #     'action': action,
        #     'role': 'form',
        # }))

        #for loop thru fields also works
        if self.multipartForm:
            html.append('<form id=' + self.form_id + ' enctype="multipart/form-data" method="POST">')
        else:
            html.append('<form id=' + self.form_id + ' method="POST">')



        html.append('<table>')

        for error in self.non_field_errors():
            html.append('<tr><td><div class="alert alert-danger">%s</div></td></tr>' % error)

        ### print out hidden fields
        for field in self.hiddenFields:
            html.append('<tr><td>')
            html.append(field.as_widget(attrs={ 'class': 'form-control' }))
            html.append('</td></tr>')


        ### go through the fields one by one and display them
        for field in self:

            if field.label_tag:
                html.append('<tr><td>')
                html.append(field.label_tag(label_suffix=':'))
                html.append('</td></tr>')

            html.append('<tr><td>')
            html.append(field.as_widget(attrs={ 'class': 'form-control' }))
            html.append('</td></tr>')

            if field.help_text:
                  html.append('<tr><td><div class="text-muted">%s</div></td></tr>' % field.help_text)

            if field.errors:
                  html.append('<tr><td><div class="label label-danger">%s</div></td></tr>' % field.errors.as_text())

        html.append('<tr><td>')
        html.append(self.submitButtonHtml)
        html.append('</td></tr>')

        html.append('</table>')

        html.append('</form>')

        return '\n' + ' '.join(html)


    def __str__(self):
        print('........................................test1')
        return self.as_full()
