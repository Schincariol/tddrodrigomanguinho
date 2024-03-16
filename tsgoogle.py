from googleapiclient.discovery import build

API_KEY = 'sua_chave_de_api'
CX_ID = 'seu_id_da_pesquisa_personalizada'

def google_custom_search(query, num_results=10):
    service = build('customsearch', 'v1', developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CX_ID, num=num_results).execute()

    for item in res['items']:
        print(f"Resultado: {item['title']} - {item['link']}")

query = input("Digite o termo de pesquisa: ")
num_results = int(input("Quantidade de resultados desejados: "))

google_custom_search(query, num_results)