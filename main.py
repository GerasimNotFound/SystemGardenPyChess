import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 40
WINDOW_SIZE = (800, 800)
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTBLUE = (132,196,192)
BLUE = (0,86,143)
BACKGROUND = (230,96,114)
CELL_QTY = 8
CELL_SIZE = 80
COLLORS = [BLUE, LIGHTBLUE]
FNT18 = pg.font.Font(pg.font.get_default_font(), 16)
LTRS = 'АБВГДЕЖЗИЙКЛМНОПРСТ'
WIN = pg.display.set_mode(WINDOW_SIZE)

WIN.fill(BACKGROUND)

n_lines = pg.Surface((CELL_SIZE * CELL_SIZE, CELL_SIZE // 2))
n_rows = pg.Surface((CELL_SIZE // 2, CELL_QTY * CELL_SIZE))
fields = pg.Surface((CELL_QTY * CELL_SIZE, CELL_QTY * CELL_SIZE))
board = pg.Surface((
    2*n_rows.get_width() + fields.get_width(),
    2*n_lines.get_height() + fields.get_height()
))
is_even_qty = (CELL_QTY % 2 == 0)
cell_color_index = 1 if (is_even_qty) else 0
for y in range(CELL_QTY):
    for x in range(CELL_QTY):
        cell = pg.Surface((CELL_SIZE, CELL_SIZE))
        cell.fill(COLLORS[cell_color_index])
        fields.blit(cell, (x * CELL_SIZE, y * CELL_SIZE))
        cell_color_index ^= True
    cell_color_index = cell_color_index^True if (is_even_qty) else cell_color_index
for i in range(0, CELL_QTY):
    letter = FNT18.render(LTRS[i],1,WHITE)
    number = FNT18.render(str(CELL_QTY - i),1, WHITE)
    n_lines.blit(letter, (
        i * CELL_SIZE + (CELL_SIZE - letter.get_rect().width) // 2,
        (n_lines.get_height() - letter.get_rect().height) // 2
    ))
    n_rows.blit(number, (
        (n_rows.get_width() - letter.get_rect().width) // 2,
        i * CELL_SIZE + (CELL_SIZE - number.get_rect().height) // 2
    ))
board.blit(n_rows, (0, n_lines.get_height()))
board.blit(n_rows, (n_rows.get_width() + fields.get_width(), n_lines.get_height()))
board.blit(n_lines, (n_rows.get_width(), 0))
board.blit(n_lines, (n_rows.get_width(), n_rows.get_width() + fields.get_width()))
board.blit(fields, (n_rows.get_width(), n_lines.get_height()))
WIN.blit(board, (
    (WINDOW_SIZE[0] - board.get_width()) // 2,
    (WINDOW_SIZE[1] - board.get_height()) // 2
    )
)
pg.display.update()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    clock.tick(FPS)
