import urllib.request,json



base_url = None



def configure_request(app):
    global base_url
    base_url_key = app.config['BASE_URL_KEY']
