from googlesearch import search

query = "loja ferramentas mercadoshops"
num_results = 10

for result in search(query, num_results=num_results):
    print(result)