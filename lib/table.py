import django

class Table(object):
    # subclasses should override the headings variable
    headers = [ 'Column 1', 'Column 2', 'Column 3' ]
    fields = [ 'Field 1', 'Field 2', 'Field 3' ]

    rows_per_page = 5

    css_class = "table table-bordered table_striped"

    # the url to request table pages from
    endpoint = '/app/view.table/pagenum/'

    def __init__(self, request, qry, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.webid = request.generator()
        self.qry = qry

    def paginate(self, request):
        try:
            pageNum = int(request.REQUEST.get('table_page'))
            if pageNum < 0 :
                pageNum = 0
        except:
            pageNum = 0

        self.qry = self.qry[pageNum*self.rows_per_page:(pageNum+1)*self.rows_per_page]

        ####### How to build in a cap on the highest page
        ####### and also a 'No records' message
        # if pageNum >= 0 and fullQry.count() > 0 :
        #     qry = fullQry[pageNum*ROWS_PER_PAGE:(pageNum+1)*ROWS_PER_PAGE]
        #     # back up until you have a record
        #     while qry.count() < 1 :
        #         print('<><><><><<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        #         pageNum -= 1
        #         print(pageNum)
        #         qry = fullQry[pageNum*ROWS_PER_PAGE:(pageNum+1)*ROWS_PER_PAGE]
        #
        #     table = UserTable(request, qry)
        #     table.paginate(request, qry)
        # else:
        #     table = 'No Records Returned'


    def __str__(self):
        # output the table html here
        html = []
        html.append('<table class="{}">'.format(self.css_class))

        html.append('<tr>')
        for header in self.headers:
            html.append('<th>{}</th>'.format(header))
        html.append('</tr>')

        for item in self.qry:
            # output each row
            html.append('<tr>')

            for field in self.fields:
                html.append('<td>{}</td>'.format(getattr(item,field)))

            html.append('</tr>')

        html.append('</table>')

        return ''.join(html)
