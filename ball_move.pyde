c = 1
x, y, vx = 50, 100, 25

def setup():
    size(400,200)
    frameRate(5)
    
def draw():
    global c, x, y, vx
    background(255)
    
    fill(255,0,255)
    ellipse(x, y, 50, 50)
    
    x += vx
    if not (0 + 25 < x < width - 25):
        vx = -vx
    