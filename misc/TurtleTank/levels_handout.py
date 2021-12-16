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

    return level

def get_level(check_point: str) -> Optional[blueprints.Level]:
    level_gen_list = [
            ("fake_checkpoint_0", generate_level_0),
            ("fake_checkpoint_1", generate_level_1),
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
        print("You have completed the game and captured the flag: idek{FAKE_FLAG}")
        return None

    return level

