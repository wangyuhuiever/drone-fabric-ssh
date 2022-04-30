# -*- coding: utf-8 -*-
import client
import time

if __name__ == '__main__':
    tz = time.strftime('%Z', time.localtime())
    print(tz)
    client.run()
