import requests
from bs4 import BeautifulSoup

def extrairDados(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"DEBUG: Tentando fazer requisição para: {url}")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("DEBUG: Requisição HTTP bem-sucedida. Status:", response.status_code)

        soup = BeautifulSoup(response.text, 'html.parser')

        citacao_elemento = soup.find('span', class_='text')
        if citacao_elemento:
            citacao = citacao_elemento.get_text(strip=True)
            print(f"DEBUG: Citação encontrada: {citacao}")
        else:
            citacao = "Citação não encontrada"
            print("DEBUG: Citação NÃO encontrada com o seletor 'text'.")

        autor_elemento = soup.find('small', class_='author')
        if autor_elemento:
            autor = autor_elemento.get_text(strip=True)
            print(f"DEBUG: Autor encontrado: {autor}")
        else:
            autor = "Autor não encontrado"
            print("DEBUG: Autor NÃO encontrado com o seletor 'author'.")

        return {
            'citacao': citacao,
            'autor': autor,
            'url': url
        }

    except requests.exceptions.HTTPError as e:
        print(f"ERRO HTTP ao acessar a URL {url}: {e.response.status_code} - {e.response.reason}")
        print("DEBUG: Pode ser um bloqueio do site (menos provável para quotes.toscrape.com).")
        return None
    except requests.exceptions.RequestException as e:
        print(f"ERRO DE CONEXÃO ao acessar a URL {url}: {e}")
        print("DEBUG: Verifique sua conexão com a internet ou se a URL está correta.")
        return None
    except Exception as e:
        print(f"OCORREU UM ERRO INESPERADO: {e}")
        return None

if __name__ == "__main__":
    url_do_site_teste = 'http://quotes.toscrape.com/'

    print(f"Iniciando tentativa de obter dados do site de teste: {url_do_site_teste}\n")
    dados_extraidos = extrairDados(url_do_site_teste)

    if dados_extraidos:
        print("\n--- Dados Extraídos com Sucesso ---")
        print(f"Citação: {dados_extraidos['citacao']}")
        print(f"Autor: {dados_extraidos['autor']}")
        print(f"URL: {dados_extraidos['url']}")
    else:
        print("\n--- FALHA NA EXTRAÇÃO DE DADOS ---")
        print("Não foi possível obter os dados. Verifique as mensagens de debug acima para mais detalhes.")