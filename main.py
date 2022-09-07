import telebot
#Py packages pyTelegramBotAPI

API_KEY = '5700894477:AAG2WsgUrR00JKL15fomwm6EJZ9DpUFGHfg'
bot = telebot.TeleBot(API_KEY)

#Start Commands
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Hello, Let's Start Learn about Programming //Click_to_Navigate_the_List                 **📖*/Study_dadas** (or) **😏*/fun**"
    )

@bot.message_handler(commands=["Study_dadas"])
def Study_dadas(message):
    bot.reply_to(message, "👨‍💻/Technical * Categories * ⚙️/nonTechnical")


@bot.message_handler(commands=["Technical", "technical"])
def Technical(message):
    bot.send_message(
      message.chat.id,
     "😊Don't Worry Guys😊..we Will explore everything.")
    bot.reply_to(message, ["💻/Beginner :-: /Advance"])


@bot.message_handler(commands=["Beginner", "beginner"])
def Beginner(message):
  bot.send_message(message.chat.id, "Guys,Trending Technology for Beginner...")
  bot.reply_to(message," /Python , /Java , /Js ,/CSharp")


@bot.message_handler(commands=["java", "Java"])
def Java(message):
    bot.reply_to(message, [
        "Learn (Oak)Java with this Ref_Link  : https://www.python.org/search/?q=study"
    ])


@bot.message_handler(commands=["Python", "python"])
def Python(message):
    bot.reply_to(message, [
        "Learn Python with this Ref_Link  : https://www.python.org/search/?q=study"
    ])
@bot.message_handler(commands=['fun'])
def send_welcome(message):
    msg = bot.reply_to(message, "Your name please😊..Your Patner waiting for you!")
    bot.register_next_step_handler(msg, define)


def define(message):
    chat_id = message.chat.id
    word = message.text
    bot.send_message(chat_id, f'I love you ❤️{word},I never leave you alone  ')
    bot.send_message(message.chat.id, 'By😘 Technology😘')

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling()
