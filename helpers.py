from flask import session

def autentica_session():
    if 'conta_conectada' not in session or session['conta_conectada'] == None:
        return False
    return True