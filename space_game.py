import pygame.display, controls
import sqlite3
from game_over import Game_over
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from menu import Menu
from input_name import Input_name


def run():
    "Основной файл, в котором запускается игра"
    con = sqlite3.connect("D:\\Python\\python_game\\venv\\test.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS player( player text, score int)")
    res = cur.execute("SELECT name FROM sqlite_master")
    res.fetchone()
    con.commit()
    pygame.init()
    pygame.mixer.music.load("sounds/space.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption(("Game"))
    bg_color = (0, 0, 0)
    game_over = Game_over(screen)
    menu = Menu(screen)
    menu.output()
    pygame.display.flip()
    while True:
        if controls.events_menu(menu):
            break
    if menu.click:
        input_name = Input_name(screen)
        while True:
            if input_name.done:
                break
        if input_name.name_input:
            gun = Gun(screen)
            bullets = Group()
            inos = Group()
            controls.create_army(screen, inos)
            stats = Stats()
            sc = Scores(screen, stats, input_name, cur)
            while True:
                controls.events(screen, gun, bullets)
                if stats.run_game:
                    gun.update_gun()
                    controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
                    controls.update_bullets(screen, stats, sc, inos, bullets)
                    controls.update_inos(stats, screen, sc, bullets, gun, inos, game_over, input_name, cur, con)


if __name__ == '__main__':
    run()
