import time, praw, requests, pandas as pd


# added text


def main():
    # reddit api authentication
    reddit = praw.Reddit('tennisbot', user_agent = 'Tennis Bot by /u/pillemer')

    # the subreddits you want your bot to live on
    subreddit = reddit.subreddit('tennisbot')

    # phrase to activate the bot
    keyphrase = '!tennisbot '

    # chache comments already responded to
    already_responded = []

    # look for phrase and reply appropriately
    for comment in subreddit.stream.comments():
        if keyphrase in comment.body and comment.id not in already_responded:
            already_responded.append(comment.id)
            player = comment.body.replace(keyphrase, '')
            points = find_points(player)
            try:
                if points:
                    reply = f'you mentioned {player}, he currently has {points} ranking points.'
                    comment.reply(reply)
                    print(f'posted: ({reply}) to comment {comment.id}.')
                else:
                    reply = f'''{player} is not an active player or has no ranking points.
                    Are you sure you spelled the name correcly?'''
                    comment.reply(reply)
                    print(f'posted: ({reply}) to comment {comment.id}.')
                print('sleeping for 10 minutes')
                time.sleep(600)
                print("I'm awake!")
            except Exception as e:
                print(e)


# find current ranking points from atp website
def find_points(player):
    url = 'https://www.atptour.com/en/rankings/singles?&rankRange=1-5000'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    player = df.query(f"Player == '{player.title()}'")
    if player.empty:
        return None
    else:
        return player.iloc[0]['Points']

if __name__ == '__main__':
    main()