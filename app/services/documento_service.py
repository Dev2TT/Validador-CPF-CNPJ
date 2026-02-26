from extensions import db
import requests

open_cnpj_api="https://api.opencnpj.org/"

class DocumentoService:

    @staticmethod
    def puxa_cnpj(cnpj:str):
        url_completa=open_cnpj_api+cnpj

        try:
            request= requests.get(url_completa)
            return request.json()
        
        except Exception:
            return False
        

    

