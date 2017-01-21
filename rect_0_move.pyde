def setup():
    size(400,200)
    rectMode(CENTER)
    
def draw():
    background(255)
    fill(192)
    noStroke()
    rect(40,40,40,40)
    
    with pushMatrix():
        translate(mouseX, mouseY)
        rotate(radians(mouseX))
        fill(0)
        rect(0,0,40,40)