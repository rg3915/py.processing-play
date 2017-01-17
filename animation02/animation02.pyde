c = 1
x, y, d = 50, 40, 60

def setup():
    size(600, 200)
    frameRate(2)
    stroke(0)
    fill(255, 255, 255)
    myFont = createFont("Georgia", 24);
    textFont(myFont);
    textAlign(CENTER, CENTER);

def draw():    
    global c, x, y, d # pra poder alterar a posição e diâmetro do círculo
    background(255) # fundo preto (e limpa o frame da animação)
    
    fill(255, 255, 255)

    # text
    fill(0, 0, 0)
    text(x, width * 0.9, height * 0.9);

    # draw lines
    line(45, 100, 555, 100)
    line(50,80,50,120)
    line(550,80,550,120)
    for i in range(50,610,100):
        line(i,90,i,110)
        
    # draw square
    rotate(radians(x))
    rect(0, 0, d, d)

    # animate square
    x += 100
    if x > 500:
        x = 50
    # reset c
    c += 1
    if c > 6:
        c = 1
    
    # noLoop()
    
    # if frameCount % 10 == 0:        # a cada 10 frames
        # saveFrame("anima-###.png")  # salva um PNG
    # if frameCount == 900:   # para no 900
        # noLoop()