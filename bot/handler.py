from xmlrpc.client import Boolean
from bot.chatting import *
from bot.responses import *
from bot.rules import *

from dotenv import load_dotenv
from threading import Thread
from time import sleep

import os
import telebot


load_dotenv()  # take environment variables from .env
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

is_watching = False
last_message = None


@bot.message_handler(commands=['unwatch'])
def command_unwatch(message):
    if not validate(message):
        return

    global is_watching
    is_watching = False
    response(bot, message, UNWATCH_PREFIX + last_message.text.lower())


@bot.message_handler(commands=['watch'])
def command_watch(message):
    if not validate(message):
        return

    global is_watching
    global last_message

    if last_message is None:
        response(bot, message, WATCH_ERROR)
        return

    n = WATCH_DEFAULT_PERIOD
    parameters = message.text.lower().split()[1:]

    if NUMBER_FLAG in parameters:
        try:
            n = int(parameters[parameters.index(NUMBER_FLAG) + 1])
        except:
            response(bot, message, PARSING_ERROR)
            response(bot, message, INVALID_WATCH_PERIOD)

    is_watching = True
    response(bot, message, WATCH_PREFIX + last_message.text.lower())
    thread = Thread(target=watching, args=(n,))
    thread.start()


@bot.message_handler()
def general(message):
    global last_message
    last_message = message

    if not validate(message):
        return

    message_parts = message.text.lower().split()
    command = COMMANDS[message_parts[0]]
    command.callback(bot, message, message_parts[1:])


def validate(message) -> Boolean:
    message_parts = message.text.lower().split()

    if not message.text.startswith(COMMAND_PREFIX) or not message_parts[0] in COMMANDS:
        response(bot, message, UNKNOWN_COMMAND_PREFIX +
                 '`' + message.text + '`')
        response(bot, message, HELP_INFO)
        return False

    command = COMMANDS[message_parts[0]]

    if HELP_FLAG in message_parts[1:]:
        response(bot, message, command.help)
        return False

    response(bot, message, VALID_PARAMETERS_PREFIX +
             '`' + '`, `'.join(command.flags) + '`.')

    for part in message_parts[1:]:
        if not part.isdigit() and not part in command.flags:
            response(bot, message, UNKNOWN_COMMAND_PREFIX +
                     '`' + message.text + '`')
            return False

    return True


def watching(n: int):
    global is_watching
    global last_message

    while(is_watching):
        general(last_message)
        sleep(n)
