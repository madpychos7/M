import random
import datetime
from telegram.ext import Updater, CommandHandler

# Telegram bot token
BOT_TOKEN = 'your_bot_token'

# Function to generate a random credit card number
def generate_card_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

# Function to generate a random expiration date
def generate_expiration_date():
    current_year = datetime.datetime.now().year
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(current_year, current_year + 5))
    return month + '/' + year

# Function to generate a random CVV
def generate_cvv():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to handle the /start command
def start(update, context):
    card_number = generate_card_number()
    expiration_date = generate_expiration_date()
    cvv = generate_cvv()
    message = f"Your new credit card details:\n\nCard Number: {card_number}\nExpiration Date: {expiration_date}\nCVV: {cvv}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Main function to start the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
