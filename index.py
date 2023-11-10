from waitress import serve
from os import environ
from vita_site.wsgi import application

if __name__ == '__main__':
    serve(application, host='0.0.0.0', port=int(environ['PORT']))
