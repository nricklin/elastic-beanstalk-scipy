def wsgi_app(environ, start_response):
    import sys
    status = '200 OK'
    headers = [('Content-type', 'text/plain'),
               ('Content-Length', str(len(output)))]
    start_response(status, headers)

    import scipy
    yield scipy.version.version

application = wsgi_app
