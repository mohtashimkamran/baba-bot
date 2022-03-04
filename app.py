from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Bot, Update, ReplyKeyboardMarkup
import textt


def start(update: Update, context: CallbackContext) -> None:
    author = update.message.from_user.first_name
    reply = "Hi! {} ".format(author)
    update.message.reply_text(reply+"\n"+textt.welcome_text)

def startt(update,context):
    user_input = update.message.text
    if user_input in textt.greet:
        author = update.message.from_user.first_name
        reply = "Hi! {}".format(author)
        update.message.reply_text(reply+"\n"+textt.welcome_text)


def help(update,context) -> None:
    update.message.reply_text(textt.help_text)

def donate(update,context):
    update.message.reply_text(textt.donate_text)
    

def info(update,context):
    update.message.reply_text("Choose a category",reply_markup=ReplyKeyboardMarkup(keyboard=textt.topics_keyboard, one_time_keyboard=True)) 

def reply(update, context):
    update.message.reply_text(textt.no_text_found)

#disease

def IT(update,context):
    update.message.reply_text(textt.IT)
def ECE(update,context): 
    update.message.reply_text(textt.ECE)
def EE(update,context):
    update.message.reply_text(textt.EE)
def ME(update,context):
    update.message.reply_text(textt.ME)
def AI(update,context):
    update.message.reply_text(textt.AI)
def CE(update,context):
    update.message.reply_text(textt.CE)
def CSE(update,context):
    update.message.reply_text(textt.CSE)
def IOT(update,context):
    update.message.reply_text(textt.IOT)
def ABOUT(update,context):
    update.message.reply_text(textt.ABOUT)
def ADMISSION(update,context):
    update.message.reply_text(textt.ADMISSION)

def main():
    updater = Updater("t", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("donate",donate))
    dispatcher.add_handler(CommandHandler("IT",IT))
    dispatcher.add_handler(CommandHandler("ME",ME))
    dispatcher.add_handler(CommandHandler("CE",CE))
    dispatcher.add_handler(CommandHandler("EE",EE))
    dispatcher.add_handler(CommandHandler("ECE",ECE))
    dispatcher.add_handler(CommandHandler("AI",AI))
    dispatcher.add_handler(CommandHandler("IOT",IOT))
    dispatcher.add_handler(CommandHandler("CSE",CSE))
    dispatcher.add_handler(CommandHandler("ABOUT",ABOUT))
    dispatcher.add_handler(CommandHandler("ADMISSION",ADMISSION))

    dispatcher.add_handler(MessageHandler(Filters.text, startt))
    dispatcher.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
