import time

def _print(text):
    print(time.strftime('%H:%M:%S', time.localtime()), text)

class Printer:
    level: int = 1

    def critical(self, text):
        print(text)

    def error(self, text):
        if self.level < 5: _print(text)

    def warning(self, text):
        if self.level < 4: _print(text)

    def info(self, text):
        if self.level < 3: _print(text)

    def debug(self, text):
        if self.level < 2: _print(text)