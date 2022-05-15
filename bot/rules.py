from bot.callbacks import *
from bot.command import command
from bot.commands import *
from bot.flags import *


# command class dictionary
COMMANDS = {
    BBC_COMMAND: command(BBC_COMMAND, bbc, (HELP_FLAG, NUMBER_FLAG,
                         REPLY_FLAG, FUTURE_FLAG, SPORT_FLAG, TRAVEL_FLAG), BBC_COMMAND_HELP),
    HELP_COMMAND: command(HELP_COMMAND, help, (HELP_FLAG, REPLY_FLAG), HELP_COMMAND_HELP),
    NBCNEWS_COMMAND: command(NBCNEWS_COMMAND, nbcnews, (HELP_FLAG, NUMBER_FLAG, REPLY_FLAG), NBCNEWS_COMMAND_HELP),
    NYTIMES_COMMAND: command(NYTIMES_COMMAND, nytimes, (HELP_FLAG, NUMBER_FLAG,
                             REPLY_FLAG, ART_FLAG, SPORT_FLAG, TRAVEL_FLAG), NYTIMES_COMMAND_HELP),
    START_COMMAND: command(START_COMMAND, start, (HELP_FLAG, REPLY_FLAG), START_COMMAND_HELP),
    UNWATCH_COMMAND: command(UNWATCH_COMMAND, unwatch, (HELP_FLAG,), UNWATCH_COMMAND_HELP),
    WATCH_COMMAND: command(WATCH_COMMAND, watch,
                           (HELP_FLAG, NUMBER_FLAG), WATCH_COMMAND_HELP)
}
