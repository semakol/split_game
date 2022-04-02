from defs import message

def level_scripts(level_number, player, screen, level, scripts, k_space, tp_script):
    if level_number == 1:
        if not scripts[0]:
            message(screen, 'Ходить: W, A, S, D')
            player.stuck = True
            player.tp_on = False
            tp_script[0] = False
            if k_space[0]:
                player.stuck = False
                scripts[0] = 1
                k_space[0] = 0
                scripts.append(0)
        elif not scripts[1]:
            player.stuck = True
            player.tp_on = False
            message(screen, 'Диктор: Встаньте на зелёный квадрат')
            if k_space[0]:
                player.stuck = False
                scripts[1] = 1
                k_space[0] = 0
                scripts.append(0)
        elif not scripts[2]:
            if player.p_pos == (3, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Здраствуйте, испытуемый №42069')
                if k_space[0]:
                    player.stuck = False
                    scripts[2] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[3]:
            if player.p_pos == (3, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Вы будете проходить испытание с пространственой аномалией')
                if k_space[0]:
                    player.stuck = False
                    scripts[3] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[4]:
            if player.p_pos == (3, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Пройдите в следущую комнату')
                if k_space[0]:
                    for door in level[5]:
                        if door.pos == (6, 6) or door.pos == (9, 6):
                            door.on = True
                    player.stuck = False
                    scripts[4] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[5]:
            if player.p_pos == (10, 6):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Перед вами куб и кнопка')
                if k_space[0]:
                    player.stuck = False
                    scripts[5] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[6]:
            if player.p_pos == (10, 6):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Диктор: Я думаю вы разберётесь что делать')
                if k_space[0]:
                    player.stuck = False
                    scripts[6] = 1
                    k_space[0] = 0
                    scripts.append(0)
        elif not scripts[7]:
            if player.p_pos == (12, 2):
                player.stuck = True
                player.tp_on = False
                message(screen, 'Поднять, опустить Куб "R"')
                if k_space[0]:
                    player.stuck = False
                    scripts[7] = 1
                    k_space[0] = 0
                    scripts.append(0)
    elif level_number == 2:
        if not scripts[0]:
            if player.p_pos == (5, 5):
                message(screen, 'Открывать дверь на "E"')
                player.stuck = True
                player.tp_on = False
                tp_script[0] = False
                if k_space[0]:
                    player.stuck = False
                    scripts[0] = 1
                    k_space[0] = 0
                    scripts.append(0)
    elif level_number == 3:
        pass
    elif level_number == 4:
        pass
    elif level_number == 5:
        pass
    elif level_number == 6:
        pass