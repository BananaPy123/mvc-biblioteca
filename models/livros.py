import requests

def buscar_livro_google(titulo):
    url = f"https://www.googleapis.com/books/v1/volumes?q={titulo}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        
        if 'items' in dados:
            livro = dados['items'][0]['volumeInfo']

            resultado = {
                'titulo': livro.get('title', 'Sem título'),
                'autor': ', '.join(livro.get('authors', ['Desconhecido'])),
                'isbn': next((isbn['identifier'] for isbn in livro.get('industryIdentifiers', []) if isbn['type'] == 'ISBN_13'), 'Sem ISBN'),
                'descricao': livro.get('description', 'Sem descrição disponível'),
                'link': livro.get('previewLink', 'Sem link de visualização'),
                'imagem': livro.get('imageLinks', {}).get('thumbnail', ''),
            }

            return resultado

    return None
