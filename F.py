import random
import telebot

# Luhn algorithm to generate credit card numbers
def generate_credit_card_number(prefix, length):
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    card_number = prefix
    while len(card_number) < length - 1:
        card_number += str(random.randint(0, 9))
    checksum = luhn_checksum(card_number + '0')
    if checksum == 0:
        return card_number + str(random.randint(1, 9))
    else:
        return card_number + str(10 - checksum)

# Telegram bot configuration
bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)

# Generate and send credit card numbers
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Generating credit card numbers...")
    with open('payment_cards.txt', 'w') as file:
        for i in range(100):  # Generate 100 credit card numbers
            card_number = generate_credit_card_number('5432', 16)  # Example prefix and length
            file.write(card_number + '\n')
            bot.send_message(message.chat.id, card_number)
    bot.send_message(message.chat.id, "Credit card numbers generated and saved to payment_cards.txt")

# Run the bot
bot.polling()
