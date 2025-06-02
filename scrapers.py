import requests
from bs4 import BeautifulSoup

def extrairDados(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        nomeElemento = soup.find('span', id='productTitle')
        if nomeElemento:
            nome = nomeElemento.get_text(strip = True)
        else:
            nome = "Nome não encontrado"
            
        precoElementoInteiro = soup.find('span', class_= 'a-price-whole')
        preco = "Nome não encontrado"
        
        if precoElementoInteiro:
            preco_str = precoElementoInteiro.get_text(strip = True)
            
            precoElementoDecimal = soup.find('span', class_= 'a-price-fraction')
            if precoElementoDecimal:
                preco_str += "," + precoElementoDecimal.get_text(strip = True)
                
            precoElementoSimbolo = soup.find('span', class_= 'a-price-symbol')
            if precoElementoSimbolo:
                preco = f"{precoElementoSimbolo.get_text(strip = True)}{preco_str}"
            else:
                preco = f"{preco_str}"
        else:
            precoElementoOffscreen = soup.find('span', class_= 'a-offscreen')
            if precoElementoOffscreen:
                preco = precoElementoOffscreen.get_text(strip = True)
                
        return {
            'nome': nome,
            'preco': preco,
            'url': url
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None
    
if __name__ == "__main__":
    urlDoProduto = 'https://www.amazon.com.br/Pense-enrique%C3%A7a-Napoleon-Hill/dp/8582713725/'
    
    print(f"Tentando obter dados do produto {urlDoProduto}\n")
    dadosProduto = extrairDados(urlDoProduto)
    
    if dadosProduto:
        print("\n--- Dados do produto obtidos com sucesso ---")
        print(f"Nome do produto: {dadosProduto['nome']}")
        print(f"Preço do produto: {dadosProduto['preco']}")
        print(f"URL do produto: {dadosProduto['url']}")
    else:
        print("Não foi possível obter os dados do produto.")
        