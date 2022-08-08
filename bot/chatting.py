def reply(bot, message, response: str) -> None:
    bot.reply_to(message, response)


def response(bot, message, response: str) -> None:
    bot.send_message(message.chat.id, response)
