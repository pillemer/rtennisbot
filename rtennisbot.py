import time, praw, requests, json, pandas as pd

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
            ranking_points = get_ranking_points(player)
            race_points = get_race_points(player)
            try:
                if ranking_points:
                    reply = f'you mentioned {player}, he currently has {ranking_points} ranking points and {race_points} race points'
                    comment.reply(reply)
                    print(f'posted: ({reply}) to comment {comment.id}.')
                else:
                    reply = f'''{player} is not an active player.
                    Are you sure you spelled the name correcly?'''
                    comment.reply(reply)
                    print(f'posted: ({reply}) to comment {comment.id}.')
                print('sleeping for 10 minutes')
                time.sleep(600)
                print("I'm awake!")
            except Exception as e:
                print(e)


# find current ranking points from scraping atp website
def get_ranking_points(player):
    url = 'https://www.atptour.com/en/rankings/singles?&rankRange=1-5000'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    player = df.query(f"Player == '{player.title()}'")
    if player.empty:
        return None
    else:
        return player.iloc[0]['Points']

# find current race points useing API
def get_race_points(player):
    url = "https://tennis-live-data.p.rapidapi.com/rankings/race/ATP"

    headers = {
        'x-rapidapi-host': "tennis-live-data.p.rapidapi.com",
        'x-rapidapi-key': "b959b7f4e4msh4dbb30d178cbca2p19d665jsn323d6128e891"}

    response = requests.request("GET", url, headers=headers)
    response_json = response.json()
    for item in response_json['results']['rankings']:
        if item['full_name'] == player.title():
            return item['race_points']
    return None

if __name__ == '__main__':
    main()

