# S linkova sa slike dohvatit 
# Postove
# Usere
# Upraite ih u jedan objekt (post ce u podatcima imat userId po kojem ce te znati tko pase di)
# UserPost koji ce imat podatke i o useru i postu
# Konacno tu listu UserPostova zapiste u lokalni file i na ekran


from urllib.parse import urljoin
import requests
import json

base_url = ('https://jsonplaceholder.typicode.com')


# fetch users
def users_request(url):
    response = requests.get(urljoin(url, "users"))

    if response.status_code == 200:
        return response
    else:
        print('GET zahtjev neuspjesan, status kod: ', response.status_code)


# fetch posts
def get_user_posts(url):
    response = requests.get(urljoin(url, "posts"))

    if response.status_code == 200:
        return response
    else:
        print('GETsssss zahtjev neuspjesan, status kod: ', response.status_code)

users = users_request(base_url).json()
posts = get_user_posts(base_url).json()

dict_posts = {d['id']: d for d in posts}

combined = [{**item1, **dict_posts.get(item1['id'], {})} for item1 in users]


# Write to JSON file
with open('output.json', 'w') as f:
    json.dump(combined, f)
    