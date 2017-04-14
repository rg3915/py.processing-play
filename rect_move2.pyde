padding = 10
c, r = 0, 180
x, y, d = 50, 40, 60
stx = padding # start_translate_x
sty = padding # start_translate_y

def setup():
    size(450, 450)
    frameRate(12)
    stroke(0)
    fill(255, 255, 255)
    myFont = createFont("Georgia", 24);
    textFont(myFont);
    textAlign(CENTER, CENTER);

def draw():    
    global c, x, y, d, r, stx, sty # pra poder alterar os valores
    background(255) # fundo preto (e limpa o frame da animação)
    
    fill(255, 255, 255)

    # text
    fill(0, 0, 0)
    text(c, width * 0.1, height * 0.9) # counter
    text(x, width * 0.9, height * 0.9) # frame
    text(r, width * 0.9, height * 0.1) # angle
    text('o', width * 0.97, height * 0.07)

    
    # draw lines
    stroke(0,0,255)
        
    line(0 + padding, 0 + padding, width - padding, 0 + padding)
    line(width - padding, 0 + padding, height - padding, width - padding)
    line(0 + padding, height - padding, width - padding, height - padding)
    line(0 + padding, 0 + padding, 0 + padding, height - padding)
        
    # draw square
    with pushMatrix():
        translate(stx,sty)
        # rotate(radians(r))
        rect(0, 0, d, d)

    # animate square
    x += 100
    if x > 500:
        x = 50
    # reset c counter for start_translate
    c += 1
    # if c % 6 == 0:
        # start_translate += 60
    if c > 42:
        c = 1
        # start_translate = 110
    r += 15
    if r > 256:
        r = 180
    
    # noLoop()
    
    # if frameCount % 10 == 0:        # a cada 10 frames
        # saveFrame("anima-###.png")  # salva um PNG
    # if frameCount == 900:   # para no 900
        # noLoop()