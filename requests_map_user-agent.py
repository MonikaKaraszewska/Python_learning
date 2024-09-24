import requests


# urls = ["https://elt.oup.com/", "https://www.w3schools.com/", "https://pynative.com/python/basics/"]
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# }
#
# responses = []
#
# for url in urls:
#     response = requests.get(url, headers=headers)
#     responses.append(response)
#
# for url, response in zip(urls, responses):
#     print(f"URL: {url}, Status code: {response.status_code}")
#
# print("responses:", responses)

print(".............................zfunkcja map")
urls = ["https://elt.oup.com/", "https://www.w3schools.com/", "https://pynative.com/python/basics/"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Użycie funkcji map do wykonania wielu żądań na raz
responses = list(map(lambda url: requests.get(url, headers=headers), urls))

# Drukowanie statusu odpowiedzi dla każdego URL-a
for url, response in zip(urls, responses):
    print(f"URL: {url}, Status code: {response.status_code}")
