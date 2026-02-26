from flask import session
import re

def autentica_session():
    if 'conta_conectada' not in session or session['conta_conectada'] == None:
        return False
    return True

def verifica_cpf(cpf:str):
    regex=r'^\d{11}$'
    valida=bool(re.fullmatch(regex,cpf))
    return valida

def verifica_cnpj(cnpj:str):
    regex=r'^\d{14}$'
    valida=bool(re.fullmatch(regex,cnpj))
    return valida
    