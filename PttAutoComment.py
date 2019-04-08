from PttAuto import Ptt
from getpass import getpass
import time

class PttComment(Ptt):
    def enter_board(self, board):
        self._telnet.write(b's')
        self._telnet.write(board.encode('big5') + b'\r\n')
        time.sleep(1)
        self._telnet.write(b'\r\n')
        time.sleep(2)
        self._content = self._telnet.read_very_eager().decode('big5', 'ignore')


def main():
    host = 'ptt.cc'
    account = getpass("Please input your PttID:")
    password = getpass("Please input your password:")
    app = PttComment(host, account, password)
    time.sleep(1)
    if app.is_connect():
        if app.login():
            app.enter_board("Gossiping")
            print (app._content)
    app.logout()
    
if __name__ == "__main__":
    main()
