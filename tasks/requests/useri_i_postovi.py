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
        print('GET zahtjev neuspjesan, status kod: ', response.status_code)

# get users and posts
users = users_request(base_url).json()
posts = get_user_posts(base_url).json()

# turn users into dictionary with id as pk
users_dict = {user['id']: user for user in users}


# iterate over posts, match id=userId, and create new dict in list
combined = [
    {
        "id": users_dict[post['userId']]['id'],
        "name": users_dict[post['userId']]['name'],
        "username": users_dict[post['userId']]['username'],
        "email": users_dict[post['userId']]['email'],
        "post_id": post['id'],
        "post_title": post['title'],
        "post_body": post['body'],
    }
    for post in posts if post['userId'] in users_dict
]

# write to JSON file
with open('users-posts.json', 'w') as f:
    json.dump(combined, f)
    