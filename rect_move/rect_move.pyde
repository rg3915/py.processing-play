c, r = 0, 180
x, y, d = 50, 40, 60
start_translate = 110

def setup():
    size(600, 200)
    frameRate(12)
    stroke(0)
    fill(255, 255, 255)
    myFont = createFont("Georgia", 24);
    textFont(myFont);
    textAlign(CENTER, CENTER);

def draw():    
    global c, x, y, d, r, start_translate # pra poder alterar os valores
    background(255) # fundo preto (e limpa o frame da animação)
    
    fill(255, 255, 255)

    # text
    fill(0, 0, 0)
    text(x, width * 0.9, height * 0.9) # frame
    text(r, width * 0.9, height * 0.1) # angle
    text('o', width * 0.95, height * 0.07)
    text(c, width * 0.1, height * 0.9)
    
    # draw lines
    stroke(0,0,255)
    line(45, 100, 535, 100)
    line(50,80,50,120)
    line(530,80,530,120)
    for i in range(50,531,60):
        line(i,90,i,110)
        
    # draw square
    with pushMatrix():
        translate(start_translate,100)
        rotate(radians(r))
        rect(0, 0, d, d)

    # animate square
    x += 100
    if x > 500:
        x = 50
    # reset c counter for start_translate
    c += 1
    if c % 6 == 0:
        start_translate += 60
    if c > 42:
        c = 1
        start_translate = 110
    r += 15
    if r > 256:
        r = 180
    
    # noLoop()
    
    # if frameCount % 10 == 0:        # a cada 10 frames
        # saveFrame("anima-###.png")  # salva um PNG
    # if frameCount == 900:   # para no 900
        # noLoop()