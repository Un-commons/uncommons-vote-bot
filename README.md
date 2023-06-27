# uncommons-vote-bot
uncommons-vote-bot in telegram



## Introduction

Deciding where you and your friends are going for lunch today can be a real hassle...
Or, for instance, deciding which games should be played at the next LAN-Party.

Since no other telegram poll/vote bot offered the full feature set my friends and I needed, I decided to write the ULTIMATE pollbot. A bot which combines all good features of all existing bots and even stuff beyond that.

## Features

The  Pollbot delivers a full set of well-tested and battle proven features.
It's capable of handling hundreds of voters for a single poll, while offering a high customizability and a wide range of different poll types to choose from.

Here is a list of the most important features:

### Poll types

This bot has 6 different vote modi. Each mode is useful for various scenarios. Choose wisely.

- Single vote: User get a single vote to allot
- Doodle: Users can vote with `yes`, `no` and `maybe` for each option.
- Block vote: Users can vote without restriction, but only one vote per option.
- Limited vote: Each user gets X votes for distribution, but only one vote per option.
- Cumulative vote: Every user gets X votes they can distribute as they like.
- Unlimited votes (Also called the shopping list): Every user can vote as often as they like, pretty much like a distributed shopping list.

### Anonymity settings

Polls can be configured to be anonymous, with the result that names of users are not visible.
Polls can be made anonymous subsequently, but as soon as a poll is anonymous it stays that way forever!

Further it's possible to hide the results of the poll until it gets closed.
As soon as such a poll is closed, the results will be visible. **Beware!**: such a poll cannot be reopened.

### Poll Management

- Addition and removal of options
- Allow other users to add new options
- Polls can be closed
- Polls can be reopened unless the poll is configured to hide the results until it has been closed.
- Polls can be completely deleted, which means that all non-forwarded occurrences of the poll will be removed.
- Polls can be reseted (Delete all votes). Poll needs to be closed first
- Polls can be cloned (New poll with same options, but without votes). Poll needs to be closed first

### Misc

- Internationalization
- Polls sync between groups in real time.
- Polls can be shared via link. This allows other users to spread the poll to arbitrary groups.
- A date picker for easier creation of poll options
- Specify a due date, at which the poll will be automatically closed.
- Activate notifications in chats to notify users that the poll will close soon.

### Sorting and Appearance

- Results can be displayed in a detailed or summarized manner.
- The percentage bar in the vote message can be disabled.
- The bot allows to configure the sorting of the option list and the user list for each option.
- Users can be sorted by vote date or username. Options can be sorted by highest percentage, name or by the order they've been added.



## Commands

```text
/start          Start the bot
/settings       Open the user settings menu
/create         Create a new poll
/list           List all active polls and manage them
/list_closed    List all closed polls and manage them
/notify         Activate notifications in a external chats
/help           Display the help
```


## Botfather Commands
- 菜单命令  
```txt
start - Start the bot
stop - Stop the bot
delete_me - Remove me from the bot. Forever
settings - Open the user settings menu
create - Create a new poll
cancel - Cancel poll creation
list - List all active polls and manage them
list_closed - List all closed polls and manage them
notify - Activate notifications in external chats
help - Show the help text
```
- inline命令  
```
search - Search your polls by name or description
```


## Build
```
1. poetry install
2. edit pollbot/config.py 
   config_path = "/root/uncommons-vote-bot/pollbot.toml"
   cp ultimate_pollbot.toml pollbot.toml
3. poetry run python main.py initdb
3. poetry run python main.py run
```
## Run 
- Linux后台运行
```
poetry run python main.py run > myout.log 2>&1 &
```