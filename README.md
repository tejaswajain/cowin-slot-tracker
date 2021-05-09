# cowin-slot-tracker
Script to look for vaccination slots in the CoWin portal and send the message in Telegram if slots are available for 18+

First of all to send slot notification, create a bot using Telegram BotFather. To create a BotFather follow the below steps –

Open the telegram app and search for @BotFather(Case Sensitive).
* Click on the start button or send “/start”.
* Then send “/newbot” message to set up a name and a username.
* After setting name and username BotFather will give you an API token which is your bot token.

Then create an app on the telegram. Follow the below steps –
* Log into the telegram core: https://my.telegram.org
* Go to ‘API development tools’ and fill out the form.
* You will get the api_id and api_hash parameters required for user authorization.

NOTE: Before using the script to send youself messages, send a Hi to bot from your app. Bots in Telegram do not have permission to initaite chats.
