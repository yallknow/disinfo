from bot.commands import HELP_COMMAND


# standart responses
HELP_INFO = '⚙ Type `' + HELP_COMMAND + '` to learn commands.'
START_INFO = '🤖 Hello there!'

# response prefixes
UNKNOWN_COMMAND_PREFIX = '⚠ Unknown command: '
VALID_COMMANDS_PREFIX = '❕ Valid command(s) is: '
VALID_PARAMETERS_PREFIX = '❕ Valid parameter(s) is: '

# errors
INVALID_NUMBER_PARAMETER = '🔢 Invalid number parameters. I will send you all the results.'
INVALID_WATCH_PERIOD = '🔢 Invalid watch period. I will use the default one.'
PARSING_ERROR = '🚨 A parsing error has occurred!'
UNWATCH_PREFIX = '⏹ Stop watching command: '
WATCH_ERROR = '👀 No commands to watch, run one first.'
WATCH_PREFIX = '▶ Watching command: '
