
# implementation of card game - Memory

import simplegui
import random

deck = range(8) + range(8)
grid = 16
WIDTH = 800
HEIGHT = 100
exposed = []
for i in range(16):
    exposed.append(False)

# helper function to initialize globals
def new_game():
    global deck, state, exposed, turns
    random.shuffle(deck)
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    for val in range(len(exposed)):
        exposed[val] = False
     
    # define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, clicked1, clicked2, turns
    
    clicked = pos[0] / (WIDTH / grid) 
    if exposed[clicked] == False:
        exposed[clicked] = True
    
        if state == 0:
            state = 1
            clicked1 = clicked
        elif state == 1:
            state = 2
            clicked2 = clicked
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            state = 1
            if deck[clicked1] != deck[clicked2]:
                exposed[clicked1] = False
                exposed[clicked2] = False
            clicked1 = clicked
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    
    # draw cards even width apart
    place = 0
    for card in deck:
        canvas.draw_text(str(card), ((place * WIDTH / grid) + 18, 60), 30, 'Green')
        place += 1

    # draw green rectangles where exposed is False
    place = 0
    for check in exposed:
        if check:
            place += 1
        else:
            canvas.draw_polygon([(place * WIDTH / grid, 0), ((place + 1)* WIDTH / grid, 0), ((place + 1)* WIDTH / grid, HEIGHT), (place * WIDTH / grid, HEIGHT)], 1, 'black', 'Green')
            place += 1
    
    # draw card outline so it still shows when exposed is True
    for place in range(grid):
        canvas.draw_polygon([(place * WIDTH / grid, 0), ((place + 1)* WIDTH / grid, 0), ((place + 1)* WIDTH / grid, HEIGHT), (place * WIDTH / grid, HEIGHT)], 1, 'black',)
             
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.set_canvas_background('white')
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
