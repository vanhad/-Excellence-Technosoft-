import requests

# Answer Number 1
PostsComments = []
posts = requests.get("https://my-json-server.typicode.com/typicode/demo/posts").json()
comments = requests.get("https://my-json-server.typicode.com/typicode/demo/comments").json()
for comment in comments:
    for post in posts:
        if post['id']==comment['id']:
            PostsComments.append({'id': post['id'], 'title': post['title'],'body':comment['body'],'postId':comment['postId']})

print(PostsComments)


# Answer Number 2
users_count = 0

for i in range(1,13):
    page = requests.get(f"https://reqres.in/api/users?page={i}").json()
    user_page_i= len(page['data'])
    users_count += user_page_i


print(users_count)