import json

from kivy.network.urlrequest import UrlRequest

URI_LOGIN='/api/authenticate.json'
URI_LISTAR_GRUPOS='/api/electric_generators.json'
URI_ENVIAR_MAINTENANCE='/api/electric_generators/%s/maintenances.json'
#headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
class WebServer():
    def __init__(self, domain_url, verbose=0):
        if domain_url == "" or domain_url == None:
            raise ValueError('No se ha entregado un nombre de dominio valido', 'Especifique la direccion del servidor '
                                                                               'donde se haran las peticiones')
        print(domain_url)
        print(verbose)

        self.DOMAIN_URL = domain_url
        self.verbose = verbose
        self.auth_token = None

    def set_auth_token(self, auth_token):
        self.auth_token = auth_token

    def headers(self):
        return {'Content-type': 'application/json', 'Accept': 'text/plain'}

    def headers_auth(self):
        return {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization': self.auth_token}

    def login(self, email, password, _on_success=None, _on_redirect=None, _on_failure=None,
              _on_error=None, _on_progress=None):
        if _on_success is None:  _on_success  = self.on_success
        if _on_redirect is None: _on_redirect = self.on_redirect
        if _on_failure is None:  _on_failure  = self.on_failure
        if _on_error is None:    _on_error    = self.on_error
        if _on_progress is None: _on_progress = self.on_progress
        post_data = { "sign_in": { "email": str(email), "password": str(password) } }
        UrlRequest(str(self.DOMAIN_URL) + str(URI_LOGIN), req_body=json.dumps(post_data), on_success=_on_success, on_redirect=_on_redirect,
                   on_failure=_on_failure, on_error=_on_error, on_progress=_on_progress, req_headers=self.headers())

    def listar_grupos(self, _on_success=None, _on_redirect=None, _on_failure=None,
                  _on_error=None, _on_progress=None):
        if _on_success is None:  _on_success  = self.on_success
        if _on_redirect is None: _on_redirect = self.on_redirect
        if _on_failure is None:  _on_failure  = self.on_failure
        if _on_error is None:    _on_error    = self.on_error
        if _on_progress is None: _on_progress = self.on_progress
        UrlRequest(self.DOMAIN_URL + URI_LISTAR_GRUPOS, on_success=_on_success, on_redirect=_on_redirect,
                   on_failure=_on_failure, on_error=_on_error, on_progress=_on_progress, req_headers=self.headers_auth())

    def enviar_maintenance(self, id, prueba_en_reposo, prueba_automatico, prueba_manual, _on_success=None, _on_redirect=None, _on_failure=None,
                  _on_error=None, _on_progress=None):
        if _on_success is None:  _on_success  = self.on_success
        if _on_redirect is None: _on_redirect = self.on_redirect
        if _on_failure is None:  _on_failure  = self.on_failure
        if _on_error is None:    _on_error    = self.on_error
        if _on_progress is None: _on_progress = self.on_progress
        post_data = {"prueba_en_reposo": prueba_en_reposo, "prueba_automatico": prueba_automatico, "prueba_manual": prueba_manual};

        UrlRequest(self.DOMAIN_URL + URI_ENVIAR_MAINTENANCE %(id),
                   req_body=json.dumps(post_data),
                   on_success=_on_success, on_redirect=_on_redirect,
                   on_failure=_on_failure, on_error=_on_error,
                   on_progress=_on_progress,
                   req_headers=self.headers_auth())

    def on_success(self, req, result):
        if self.verbose > 0:
            print("EXITO")
            print(result)

    def on_redirect(self, req, result):
        if self.verbose > 0:
            print("REDIRECCIONAMIENTO")
            print(result)

    def on_failure(self, req, result):
        if self.verbose > 0:
            print("FALLA de cliente/servidor")
            print(result)

    def on_error(self, req, result):
        if self.verbose > 0:
            print("ERROR envio de python")
            print(result)

    def on_progress(self, req, result, chunk):
        if self.verbose > 0:
            print("PROGRESO...")
            print(result)
            print(chunk)


