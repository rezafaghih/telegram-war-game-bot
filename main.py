from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters , ConversationHandler
from telegram.error import BadRequest, Forbidden
from telegram.constants import ParseMode
from server import *


ROBOT_TOKEN = "7471717943:AAEaYH7yPFb8tpuqr9oOzSjHxZrHq995m7g"


async def startRobot(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegramID = update.message.from_user.id
    fullName = f"{update.message.from_user.first_name} {update.message.from_user.last_name}"
    chatID = update.message.chat.id
    keyboardButtons = (
        [InlineKeyboardButton("لشکر کشی 🗡️", callback_data="start_game"), InlineKeyboardButton("🛠️ ارتقا", callback_data="information")],
        [InlineKeyboardButton("اطلاعات لشکر 🛡️", callback_data="information")],
        [InlineKeyboardButton("تنظیمات لشکر", callback_data="support")]
    )

    keyboard = InlineKeyboardMarkup(keyboardButtons)
    isChatExist = server.isGroupExist(chatID)
    if (isChatExist == False):
        server.createNewChat(chatID, update.message.chat.title,telegramID)
    

    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text=f"سلام {fullName} به ربات بازی جنگی خوش آمدید 🤖 \n\n برای ادامه استفاده از ربات میتوانید از دکمه های زیر استفاده کنید",
        reply_markup=keyboard
    )

async def fightCallBack(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegramID = update.callback_query.from_user.id
    chatID = update.callback_query.message.chat.id
    if (server.isFactionOwner(telegramID, chatID)):
        await update.callback_query.delete_message()  
        if (server.isArmyExist(chatID) == False):
            server.createNewArmy(chatID)
        if (server.isArmyExist(chatID)):
            armyInformation = server.getArmyInformation(chatID)
            await context.bot.send_message(
                chat_id=chatID,
                text=f"وضعیت ارتش 🗡️ \n\n سرباز : {armyInformation[1]} \n سواره نظام : {armyInformation[6]} \n کماندار : {armyInformation[3]}\n نردبان : {armyInformation[7]} \n\n سلاح های پیشرفته : \n کمان خودکار : {armyInformation[8]}\n \n\n نیروی دریایی : \n کشتی چوبی : {armyInformation[2]} \n کشتی وایکینگ ها : {armyInformation[4]} \n کشتی پیشرفته : {armyInformation[5]}"
            )
    else :
        await context.bot.send_message(
            chat_id=chatID,
            text="تنها فرمانده ارتش امکان لشکرکشی دارد ❌"
        )

app = ApplicationBuilder().token(ROBOT_TOKEN).build()
app.add_handler(CommandHandler("start", startRobot))
app.add_handler(CallbackQueryHandler(fightCallBack, "start_game"))
app.run_polling()