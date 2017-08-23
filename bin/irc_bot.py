#! /usr/bin/env python3

import itertools
import irc.bot
import irc.strings
import sys
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
import threading


class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname,
                                            nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)
        thread = threading.Thread(target=self.main_loop, args=(c, ))
        thread.start()

    def on_pubmsg(self, c, e):
        print(e.arguments[0])

    def get_lines(self):
        while True:
            yield sys.stdin.readline().strip()

    def main_loop(self, connection):
        for line in itertools.takewhile(bool, self.get_lines()):
            connection.privmsg(self.channel, line)


def main():
    import sys
    server = "chat.freenode.net"
    port = 6667
    channel = "#xyj"
    nickname = sys.argv[1]

    bot = TestBot(channel, nickname, server, port)
    bot.start()


if __name__ == "__main__":
    main()
