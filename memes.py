#!/usr/bin/env python3

def setup():
    """
    Create and set up teh config file for MemeDownloader.py
    """
    # import praw
    f = open('config.py','a')
    f.write('import praw\n')
    f.close()
    # Define Meme directory
    Dr = input('Type the Directory for your memes.\n')
    f = open('config.py', 'a')
    f.write(f'D = "{Dr}"\n')
    f.close()
    # Set up praw app
    print(
    "Go here while logged into the account you want to get memes from: "
    "https://www.reddit.com/prefs/apps/"
    )
    print(
    "Click the create an app button. Put something in the name field and select the"
    " script button."
    )
    print("Put http://localhost:8080 in the redirect uri field and click create app")
    client_id = input(
    "Enter the client ID, it's the line just under Personal use script at the top: "
    )
    client_secret = input("Enter the client secret, it's the line next to secret: ")
    user = input('Enter your reddit username: ')
    word = input('Enter your reddit password: ')


    f = open('config.py','a')
    f.write(f'reddit = praw.Reddit(\n    client_id="{client_id.strip()}",\n    client_secret="{client_secret.strip()}",\n    user_agent="meme_bot",\n    username = "{user.strip()}",\n    password = "{word.strip()}")')
    f.close()
    quit()


def get_post(l,Directory):
    urls = []
    posts = []
    subreddit = reddit.subreddit("memes").top("day",limit=l)
    for submission in subreddit:
        urls.append(submission.url)
        posts.append(submission)
    for i in range(l):
        post = urls[i]
        name = posts[i]
        end = urls[i][-4:]
        print(f'Downloading {post}\n')
        file_name = wget.download(post, f'{Directory}{name}{end}')
        print('\n')

def main():
    print('Welcome to MemeDownloader.py!')
    sleep(1)        
    r = reddit
    print('memes are saved to ' + D)
    count = int(input('How many memes would you like?\n'))
    get_post(count,D)

import praw
import wget
from time import sleep
try:
    from config import D,reddit
except:
    setup()

if __name__ == '__main__':
    main()
