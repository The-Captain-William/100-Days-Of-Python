facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:  # note the try block is inside the for loop to keep the program iterating
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0
        pass

print(total_likes)
print(facebook_posts)