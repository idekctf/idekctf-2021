import blueprints
import consts


def process_script(level: blueprints.Level) -> None:
    skip_next = False
    prg = level.player.script
    stack = level.player.stack
    prg_ptr = 0
    iter_cnt = 0
    while prg_ptr < len(prg):
        iter_cnt += 1
        if iter_cnt > level.script_iteration_limit:
            level.error.append("Script iteration limit reached.")
            return
        op = prg[prg_ptr]
        if len(stack) > level.stack_limit:
            level.error.append("Stack limit exceeded.")
            return
        if not isinstance(op, consts.OpCode):
            prg_ptr += 1
            continue

        # Instruction that load data onto stack.
        if op == consts.OpCode.TICK:
            stack.append(level.tick)
        if op == consts.OpCode.LOAD:
            if len(prg) < prg_ptr + 1:
                level.error.append(f"{prg_ptr} LOAD: missing value.")
            val = prg[prg_ptr + 1]
            if not isinstance(val, int):
                level.error.append(f"{prg_ptr} LOAD: invalid value.")
                return
            stack.append(val)
            prg_ptr += 1
        if op == consts.OpCode.COPY:
            if len(prg) < prg_ptr + 1:
                level.error.append(f"{prg_ptr} COPY: missing value.")
            val = prg[prg_ptr + 1]
            if not isinstance(val, int):
                level.error.append(f"{prg_ptr} COPY: invalid value.")
                return
            if len(stack) < abs(val):
                level.error.append(f"{prg_ptr} COPY: empty stack.") 
                return
            stack.append(stack[val])
            prg_ptr += 1
        if op == consts.OpCode.DEL:
            if len(prg) < prg_ptr + 1:
                level.error.append(f"{prg_ptr} DEL: missing value.")
            val = prg[prg_ptr + 1]
            if not isinstance(val, int):
                level.error.append(f"{prg_ptr} DEL: invalid value.")
                return
            if len(stack) < abs(val):
                level.error.append(f"{prg_ptr} DEL: empty stack.") 
                return
            stack.pop(val)

        # Tank controls.
        if op == consts.OpCode.LEFT:
            level.player.turn_left()
        if op == consts.OpCode.RIGHT:
            level.player.turn_right()

        # Flow control.
        if op == consts.OpCode.IF:
            if not stack:
                level.error.append(f"{prg_ptr} IF: empty stack.") 
                return
            if stack.pop(-1) != 0:
                prg_ptr += 1
        if op == consts.OpCode.SKP:
            if len(prg) < prg_ptr + 1:
                level.error.append(f"{prg_ptr} SKP: missing value.")
            val = prg[prg_ptr + 1]
            if not isinstance(val, int):
                level.error.append(f"{prg_ptr} SKP: invalid value.")
                return
            prg_ptr += val + 2
            continue

        # Math.
        if op == consts.OpCode.ADD:
            if len(stack) < 2:
                level.error.append(f"{prg_ptr} ADD: empty stack.") 
                return
            stack.append(stack.pop(-1) + stack.pop(-1))
        if op == consts.OpCode.SUB:
            if len(stack) < 2:
                level.error.append(f"{prg_ptr} SUB: empty stack.") 
                return
            stack.append(stack.pop(-1) - stack.pop(-1))
        if op == consts.OpCode.MOD:
            if len(stack) < 2:
                level.error.append(f"{prg_ptr} MOD: empty stack.") 
                return
            try:
                stack.append(stack.pop(-1) % stack.pop(-1))
            except ZeroDivisionError:
                level.error.append(f"{prg_ptr} MOD: divide by zero.")
        prg_ptr += 1
