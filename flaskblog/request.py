import urllib.request,json



base_url = None



def configure_request(app):
    global base_url

    base_url = app.config['BASE_QUOTES_API_URL']
