from bot.definitions import *
from bot.flags import *

# commands
BBC_COMMAND = COMMAND_PREFIX + 'bbc'
HELP_COMMAND = COMMAND_PREFIX + 'help'
NBCNEWS_COMMAND = COMMAND_PREFIX + 'nbcnews'
NYTIMES_COMMAND = COMMAND_PREFIX + 'nytimes'
START_COMMAND = COMMAND_PREFIX + 'start'
UNWATCH_COMMAND = COMMAND_PREFIX + 'unwatch'
WATCH_COMMAND = COMMAND_PREFIX + 'watch'

# command list
VALID_COMMANDS = (BBC_COMMAND, HELP_COMMAND, NBCNEWS_COMMAND,
                  NYTIMES_COMMAND, START_COMMAND, UNWATCH_COMMAND, WATCH_COMMAND)

# flags help
HELP_FLAG_HELP = '\n\t' + HELP_FLAG + '\tShow help'
REPLY_FLAG_HELP = '\n\t' + REPLY_FLAG + '\tReply on request'
NUMBER_FLAG_HELP = '\n\t' + NUMBER_FLAG + \
    '\tSpecify the desired number of news'

# commands help
BBC_COMMAND_HELP = 'Get news from the `BBC` (https://www.bbc.com):' + \
    HELP_FLAG_HELP + \
    NUMBER_FLAG_HELP + \
    REPLY_FLAG_HELP + \
    '\n\t' + FUTURE_FLAG + '\tGet news from the `future` section' + \
    '\n\t' + SPORT_FLAG + '\tGet news from the `sport` section' + \
    '\n\t' + TRAVEL_FLAG + '\tGet news from the `travel` section'

HELP_COMMAND_HELP = 'Simple help command:' + \
    HELP_FLAG_HELP + \
    REPLY_FLAG_HELP

NBCNEWS_COMMAND_HELP = 'Get news from the `NBC News` (https://www.nbcnews.com):' + \
    HELP_FLAG_HELP + \
    NUMBER_FLAG_HELP + \
    REPLY_FLAG_HELP

NYTIMES_COMMAND_HELP = 'Get news from the `The New York Times` (https://www.nytimes.com):' + \
    HELP_FLAG_HELP + \
    NUMBER_FLAG_HELP + \
    REPLY_FLAG_HELP + \
    '\n\t' + ART_FLAG + '\tGet news from the `art` section' + \
    '\n\t' + SPORT_FLAG + '\tGet news from the `sport` section' + \
    '\n\t' + TRAVEL_FLAG + '\tGet news from the `travel` section'

START_COMMAND_HELP = 'Bot hello command:' + \
    HELP_FLAG_HELP + \
    REPLY_FLAG_HELP

UNWATCH_COMMAND_HELP = 'Unsubscribe from the previous `/watch` command:' + \
    HELP_FLAG_HELP

WATCH_COMMAND_HELP = 'Re-execute the previous command with a time delay:' + \
    HELP_FLAG_HELP + \
    '\n\t' + NUMBER_FLAG + '\tSpecify delay time (s)'
