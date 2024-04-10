from process import r_file, solo_mode, loop_playing, create_game, create_menu, close
from var import menu_start, menu_load
import os


def main():
    # Create game
    screen = create_game('ChickenInvader')
    select_start = create_menu(screen, menu_start())

    while True:
        if select_start == 1:
            if os.path.exists('C:/workspace/ChickenInvaders/Data/save/save.txt'):
                select_load = create_menu(screen, menu_load())
                if select_load == 1:
                    load_inf = r_file()
                    loop_playing(screen, load_inf)
                elif select_load == 2:
                    os.remove('C:/workspace/ChickenInvaders/Data/save/save.txt')
                    loop_playing(screen)
            else:
                loop_playing(screen)
            select_start = create_menu(screen, menu_start())
        elif select_start == 2:
            create_menu(screen, solo_mode(screen))
            select_start = create_menu(screen, menu_start())
        elif select_start == 3:
            close()
            break

if __name__ == "__main__":
    main()
