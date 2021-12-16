from typing import Optional

import blueprints
import consts


def print_level(level: blueprints.Level) -> None:
    print_buf = []
    for y in range(level.height):
        row_buf = ["  "] * level.width
        print_buf.append(row_buf)

    for wall in level.field.walls:
        print_buf[wall.y][wall.x] = "x "
            
    for orb in level.field.orbs:
        print_buf[orb.y][orb.x] = "@ "

    p_loc = level.player.location
    p_dir = level.player.direction
    p_char = " "
    if p_dir == consts.Direction.LEFT:
        p_char = "<"
    if p_dir == consts.Direction.RIGHT:
        p_char = ">"
    if p_dir == consts.Direction.UP:
        p_char = "^"
    if p_dir == consts.Direction.DOWN:
        p_char = "v"
    print_buf[p_loc.y][p_loc.x] = p_char + " "

    print("=" * (level.width - len(level.name) // 2), end=" ")
    print(level.name, end=" ")
    print("=" * (level.width - (len(level.name) - 1) // 2))
    
    print(f"Tick: {level.tick} / {level.tick_limit}")
    print(f"Points: {level.player.points} / {len(level.field.orbs) + level.player.points}")
    print(f"Stack limit: {level.stack_limit}")
    print(f"Script operation limit: {level.script_iteration_limit}")
    
    print(f"+ {'- ' * level.width}+")
    for line in print_buf:
        print("| " + "".join(line) + "|")
    print(f"+ {'- ' * level.width}+")
    print(f"Stack: {level.player.stack}")

def print_start() -> None:
    print("====== Turtle tank alpha =====")
    print("Write a script to control a tank!")
    print("The script is run at every game step." + 
          "The memory for the script is organised " +
          "as a stack. The stack is kept across each " +
          "step.")
    print("")

    print("Rules:")
    print("- Tank will move forward one space every step after the script is processed.")
    print("- Tank will wrap around in both X and Y.")
    print("- Collect all the points '@'.")
    print("- Avoid hitting all the walls 'x'.")

    print("")
    print("Commands:")
    print("- help: prints this help message")
    print("- checkpoint key: skips to the checkpoint level")
    print("- play: start the current level")
    print("- quit: quits the game")
    
    print("")

    print("Script instructions:")
    print("- LOAD, value: push(value)")
    print("- TICK: push(game step)")
    print("- COPY, index: push(peek(index)) where positive index is from the start of the stack and negative index is from the current stack position. e.g. `COPY, -1` will push the last value pushed again, `COPY, 0` will push the earliest value pushed on to the stack.")
    print("- DEL, n: will delete a value off the stack at index n. Indexing follows that of COPY.")
    print("- RIGHT: Turns the tank to the right")
    print("- LEFT: Turns the tank to the left")
    print("- IF: Skips the next instruction if pop() == 0")
    print("- SKP, n: Skip the next n instruction")
    print("- ADD: push(pop() + pop())")
    print("- SUB: push(pop() - pop())")
    print("- MOD: push(pop() % pop())")

    print("")
    print("Scripts are comma seperated list of either instructions, and int. If the program counter points to an int it will be treated as a NOP.")

    print("")
