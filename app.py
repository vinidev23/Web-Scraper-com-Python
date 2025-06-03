from flask import Flask, render_template, request
from scrapers import extrairDados

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dadosExtraidos = None
    urlDigitada = ""
    
    if request.method == 'POST':
        urlDigitada = request.form['url_input']
        if urlDigitada:
            print(f"Flask: Recebida url para scraping: {urlDigitada}")
            dadosExtraidos = extrairDados(urlDigitada)
            if dadosExtraidos:
                print("Flask: Dados extraídos com sucesso!")
            else:
                print("Flask: Falha na extração de dados.")
        else:
            print("Flask: URL vazia.")
            
    return render_template('index.html', dados=dadosExtraidos, urlAnterior=urlDigitada)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
