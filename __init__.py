from cryptography.fernet import Fernet, InvalidToken
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<key>/<valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur dans l'encryptage : {str(e)}"

@app.route('/decrypt/<key>/<valeur>')
def decryptage(key, valeur):
    try:
        f = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        original = f.decrypt(valeur_bytes)
        return f"Valeur déchiffrée : {original.decode()}"
    except InvalidToken:
        return "Clé invalide ou token corrompu."
    except Exception as e:
        return f"Erreur dans le déchiffrement : {str(e)}"

# Bonus : une route pour générer une clé personnelle
@app.route('/generate-key')
def generate_key():
    return f"Voici votre clé personnelle : {Fernet.generate_key().decode()}"

if __name__ == "__main__":
    app.run(debug=True)
