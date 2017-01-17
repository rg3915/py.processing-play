c = 1
x, y, d = 50, 100, 90

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
    # draw circles
    ellipse(x, y, d, d)

    # text
    fill(0, 0, 0)
    text(c, x, 30)
    text(x, width * 0.9, height * 0.9);

    # draw lines
    line(45, 100, 555, 100)
    for i in range(50,551,250):
        line(i,80,i,120)
    for i in range(50,610,50):
        line(i,90,i,110)
        
    # animate circle
    x += 100
    if x > 550:
        x = 50
    # reset c
    c += 1
    if c > 6:
        c = 1
    
    loop()
    
    # if frameCount % 10 == 0:        # a cada 10 frames
        # saveFrame("anima-###.png")  # salva um PNG
    # if frameCount == 900:   # para no 900
        # noLoop()

# http://www.3dtotal.com/tutorial/2323-principles-animation-maya-by-jahirul-amin-beginners-guide-to-character-creation-in-free-chapter