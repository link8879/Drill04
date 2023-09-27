from pico2d import*

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
x = 400
y = 400
dir_x = 0
dir_y = 0

def handle_events():
    global running, dir_x, dir_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1




def draw():
    global frame, x, y

    if dir_x == 1 and dir_y == 0:
        character.clip_draw(frame * 80, 0, 80, 80, x, y)
        frame = (frame + 1) % 10
        x += dir_x * 10
    elif dir_x == -1 and dir_y == 0:
        character.clip_draw(frame * 80, 180, 80, 80, x, y)
        frame = (frame + 1) % 10
        x += dir_x * 10
    elif dir_x == 0 and dir_y == 0:
        character.clip_draw(frame * 80, 0, 80, 80, x, y)
        frame = (frame + 1) % 3
    
while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    draw()

    update_canvas()
    handle_events()

    if not running:
        break

    delay(0.15)