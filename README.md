# r/tennis bot

## Overview
This is  simple bot designed to respond to comments calling it for infromation.
It takes the tennis player's name from the comment and returns two pieces of information: That players current ranking points and their current race points.
It uses a web scraping method to get the former and uses an API request to fetch the former.

## Details
This is a bot that only responds to any comment that calls it directly within the r/tennis subreddit only.

It will respond with the number of ATP ranking points the player named in the call has according to the ATPtour.com website.

It will respond with the number of ATP race to London points the player has according to to RapidAPI.

The activation phrase is '!tennisbot' followed by the full name of the player (As spelled on www.ATPtour.com!)

The bot will only work if you the phrase is immediately followed by the player's full name and nothing else.

(example: "!tennisbot Rafael Nadal")

**This project was created as an excercise and the bot is not currently running.**
