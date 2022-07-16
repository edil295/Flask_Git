from . import views, app

app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
app.add_url_rule('/add', view_func=views.add_transaction, methods=['GET', 'POST'], endpoint='transaction')
