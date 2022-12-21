import sys, pygame
import time
from bullet import Bullet
from ino import Ino

FPS = 30
clock = pygame.time.Clock()


def events(screen, gun, bullets):
    "Обрабатывает нажатие клавиш и создает звук выстрела"
    s = pygame.mixer.Sound("sounds/laser.wav")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            if event.key == pygame.K_a:
                gun.mleft = True
            if event.key == pygame.K_SPACE:
                s.play()
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
            if event.key == pygame.K_s:
                vol = 0
                pygame.mixer.music.set_volume(vol)
            if event.key == pygame.K_w:
                vol = 1
                pygame.mixer.music.set_volume(vol)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            if event.key == pygame.K_a:
                gun.mleft = False
        clock.tick(FPS)


def events_menu(menu):
    "Проверяет нажатие кнопки мыши на Start и Exit"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if event.pos[0] > 118 and event.pos[0] < 582 and  event.pos[1] > 279 and event.pos[1] < 421:
            if menu.rect.collidepoint(event.pos):
                menu.click = True
                return True
            # if event.pos[0] > 118 and event.pos[0] < 582 and  event.pos[1] > 479 and event.pos[1] < 621:
            if menu.rect1.collidepoint(event.pos):
                sys.exit()


def update(bg_color, screen, stats, sc, gun, inos, bullets):
    "Рисует счет и пули"
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    "Обрабатывает попадение, создает ещё инопланетян"
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        if stats.score % 200 == 0 and stats.score > 0:
            create_army_line(screen, inos)
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)



def update_inos(stats, screen, sc, bullets, gun, inos, game_over, input_name, cur, con):
    "Перемещение инопланетян"
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets, game_over, input_name, cur, con)
    inos_check(stats, screen, sc, gun, inos, bullets, game_over, input_name, cur, con)


def gun_kill(stats, screen, sc, gun, inos, bullets, game_over, input_name, cur, con):
    "Контролирует оставшиеся жизни"
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        database(input_name, stats, cur, con)
        game_over.output()
        pygame.display.flip()
        time.sleep(5)
        sys.exit()


def create_army(screen, inos):
    "Создается армия инопланетян"
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((700 - 100 - 2 * ino_height) / ino_height)
    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)


def create_army_line(screen, inos):
    "Создается линия инопланетян"
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    for ino_number in range(number_ino_x):
        ino = Ino(screen)
        ino.x = ino_width + (ino_width * ino_number)
        ino.rect.x = ino.x
        inos.add(ino)


def inos_check(stats, screen, sc, gun, inos, bullets, game_over, input_name, cur, con):
    "Проверяет, чтобы инопланетяни не перешли за нижнюю полосу"
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc,  gun, inos, bullets, game_over, input_name, cur, con)
            break


def database(input_name, stats, cur, con):
    "Добавляет в базу данных результат игры"
    dis = (input_name.text, stats.score)
    cur.execute("INSERT INTO player( player, score) VALUES(?, ?)", dis)
    con.commit()

def score_database(cur):
    "Находит лучший результат в базе данных"
    sqlite_select_query = """SELECT * FROM player order by score desc limit 1;"""
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    dis = []
    for row in records:
        dis = [str(row[0]), str(row[1])]
    temp_str = " ".join(dis)
    return temp_str