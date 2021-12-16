import copy
import random
from typing import Optional

import blueprints
import consts
import game

def generate_level_0(skip_code: str) -> blueprints.Level:
    level = blueprints.Level(
            name="There's an obstacle",
            width=20,
            height=20,
            field=blueprints.Playground([],[]),
            player=blueprints.Player(
                location=blueprints.Point(10,10),
                direction=consts.Direction.LEFT,
                points=0,
                stack=[],
                script=[]),
            tick=0,
            script_iteration_limit=32,
            stack_limit=8,
            tick_limit=20,
            error=[],
            skip_code=skip_code)

    level.field.walls.append(blueprints.Point(5,10))
    level.field.orbs.append(blueprints.Point(2,10))
    level.field.orbs.append(blueprints.Point(6,10))
    # TICK, LOAD, 4, SUB, IF, SKP, 1, SKP, 2, RIGHT, RIGHT
    return level

def generate_level_1(skip_code: str) -> blueprints.Level:
    level = blueprints.Level(
            name="Sand box",
            width=20,
            height=20,
            field=blueprints.Playground([],[]),
            player=blueprints.Player(
                location=blueprints.Point(4,4),
                direction=consts.Direction.LEFT,
                points=0,
                stack=[],
                script=[]),
            tick=0,
            script_iteration_limit=32,
            stack_limit=2,
            tick_limit=40,
            error=[],
            skip_code=skip_code)

    for i in range(1,10):
        level.field.orbs.append(blueprints.Point(4, 4 + i))
        level.field.orbs.append(blueprints.Point(14, 4 + i))
        level.field.orbs.append(blueprints.Point(4 + i, 4))
        level.field.orbs.append(blueprints.Point(4 + i, 14))

    # LOAD, 10, TICK, MOD, IF, LEFT
    return level

def generate_level_2(skip_code: str) -> blueprints.Level:
    level = blueprints.Level(
            name="All the orbs",
            width=20,
            height=20,
            field=blueprints.Playground([],[]),
            player=blueprints.Player(
                location=blueprints.Point(0,0),
                direction=consts.Direction.LEFT,
                points=0,
                stack=[],
                script=[]),
            tick=0,
            script_iteration_limit=16,
            stack_limit=4,
            tick_limit=400,
            error=[],
            skip_code=skip_code)

    for x in range(20):
        for y in range(20):
            if x == 0 and y == 0:
                continue
            level.field.orbs.append(blueprints.Point(x,y))
    # LOAD, 20, TICK, MOD, COPY, -1, LOAD, 19, SUB, IF, RIGHT, IF, LEFT
    return level

def generate_level_3(skip_code: str) -> blueprints.Level:
    level = blueprints.Level(
            name="Spiralling out of control.",
            width=31,
            height=31,
            field=blueprints.Playground([],[]),
            player=blueprints.Player(
                location=blueprints.Point(15,15),
                direction=consts.Direction.LEFT,
                points=0,
                stack=[],
                script=[]),
            tick=0,
            script_iteration_limit=21,
            stack_limit=6,
            tick_limit=2600,
            error=[],
            skip_code=skip_code)
    for x in range(31):
        for y in range(31):
            if random.randrange(0,10) > 2:
                continue
            level.field.walls.append(blueprints.Point(x,y))
    # Simulate the expeted path.
    seq = [1,1]
    for i in range(15):
        seq.append(seq[-1] + seq[-2])
    for i in seq:
        for j in range(i):
            try:
                level.field.walls.remove(level.player.location)
            except:
                pass
            level.move_player_forward()
        level.player.turn_right()
        level.field.orbs.append(copy.deepcopy(level.player.location))
    level.player.location = blueprints.Point(15,15)
    level.player.direction = consts.Direction.LEFT

     # TICK, IF, SKP, 1, SKP, 6,  LOAD, 1, LOAD, 1, LOAD, 1, COPY, -1, TICK, SUB, IF, SKP, 1, SKP, 15,  RIGHT, DEL, -1, COPY, -2, COPY, -2, ADD, COPY, -2, TICK, ADD, DEL, 0
    return level

def get_level(check_point: str) -> Optional[blueprints.Level]:
    level_gen_list = [
            ("there_and_back_again", generate_level_0),
            ("consume_the_box", generate_level_1),
            ("there_was_a_spare_tick", generate_level_2),
            ("golden_ratios_are_everywhere", generate_level_3),
            ]

    if not check_point:
        return level_gen_list[0][1](level_gen_list[0][0])

    found = False
    level = None
    for skip_code, gen_func  in level_gen_list:
        if found:
            level = gen_func(skip_code)
            break
        if check_point == skip_code:
            found = True

    if not found:
        print("Invalid checkpoint")
        return None

    if found and level is None:
        print("You have completed the game and captured the flag: idek{360_no_script}")
        return None

    return level

