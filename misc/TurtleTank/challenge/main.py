#!/usr/bin/env python3

import sys
import draw
import time
import game

def main() -> int:
    draw.print_start()

    check_point = ""

    while True:
        print("Command > ", end="")
        cmd_arg = input().split(" ")
        cmd = cmd_arg[0]
        if cmd == "quit":
            break
        if cmd == "help":
            draw.print_start()
        if cmd == "play":
            check_point = game.game_loop(check_point)
        if cmd == "checkpoint":
            if len(cmd_arg) > 2:
                print("Too many arguments")
                continue
            if len(cmd_arg) == 2:
                check_point = cmd_arg[1]
            else:
                check_point = ""
    print("Terminated.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
