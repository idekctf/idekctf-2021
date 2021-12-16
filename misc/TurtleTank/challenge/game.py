import blueprints
import consts
import draw
import engine
import levels
import time


def process_level(level: blueprints.Level) -> consts.GameState:
    engine.process_script(level)
    if level.error:
        return consts.GameState.FAILED
    level.move_player_forward()
    if level.player.location in level.field.walls:
        return consts.GameState.FAILED
    if level.player.location in level.field.orbs:
        level.player.points += 1
        level.field.orbs.remove(level.player.location)
    if len(level.field.orbs) == 0:
        return consts.GameState.WIN
    level.tick += 1
    return consts.GameState.PLAYING

def game_loop(check_point: str) -> bool:

    level = levels.get_level(check_point)
    if not level:
        return check_point

    draw.print_level(level)
    print("Enter script: ", end="")
    script_text = input()
    for op in script_text.split(","):
        if not op:
            continue
        op_val = op.strip().upper()
        if op_val in consts.OpCode.__members__:
            level.player.script.append(consts.OpCode[op_val])
        else:
            try:
                int_val = int(op_val)
            except ValueError:
                print(f"Error: invalid script, '{op}' unkonwn.")
                return check_point
            level.player.script.append(int_val)
    
    for i in range(level.tick_limit):
        game_state = process_level(level)
        draw.print_level(level)
        if game_state != consts.GameState.PLAYING:
            break
        time.sleep(0.001)
    if game_state == consts.GameState.WIN:
        print (f"Level checkpoint: {level.skip_code}")
        print ("SUCCESS!")
        return level.skip_code
    else:
        if not level.error:
            print ("FAILED")
        else:
            print ("ERROR")
            for msg in level.error:
                print(msg)

    return check_point

