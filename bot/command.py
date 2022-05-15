from typing import Callable, Iterable


class command:
    def __init__(self, name: str, callback: Callable, flags: Iterable[str], help: str):
        self.name = name
        self.callback = callback
        self.flags = flags
        self.help = help
