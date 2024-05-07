from telegram import Bot
from telegram.error import TelegramError

# Replace 'YOUR_BOT_TOKEN' with the token provided by BotFather
bot_token = 'YOUR_BOT_TOKEN'

def join_group_or_channel(chat_id):
    try:
        bot = Bot(token=bot_token)
        bot.join_chat(chat_id)
        print(f"Successfully joined the group/channel with ID: {chat_id}")
    except TelegramError as e:
        print(f"Failed to join the group/channel: {e}")

if __name__ == "__main__":
    # Replace 'GROUP_OR_CHANNEL_ID' with the ID of the group or channel you want to join
    group_or_channel_id = 'GROUP_OR_CHANNEL_ID'
    join_group_or_channel(group_or_channel_id)
