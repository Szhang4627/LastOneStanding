from gamelib import *

def hideAll():
    Idle.visible=False
    Shoot.visible=False
    Rocket.visible=False
    Slash.visible=False
    Pain.visible=False
    #Bullet.visible=False
    #RocketAmmo.visible=False
    #Boom.visible=False
    #Nuke.visible=False

##########################################################   
game=Game (900,800,"Last one standing")

bk=Image("images\\Forest.png",game)
game.setBackground(bk)
bk.resizeTo(game.width,game.height)

Jeep=Image("images\\jeep.png",game)
Idle=Animation("images\\Idle.gif",8,game,786/8,135,frate=5)
Shoot=Animation("images\\Shoot.gif",8,game,809/8,133,frate=3)
Rocket=Animation("images\\Rocket.gif",13,game,794/6,367/3,frate=5)
Slash=Animation("images\\Slash.png",7,game,960/5,384/2,frate=5)
Pain=Animation("images\\Pain.gif" ,5,game,465/5,126,frate=5)
Aim=Image("images\\Aim.png",game)
Boom=Animation("images\\Boom.png",20,game,785/5,916/4,frate=3)
Bullet=Image("images\\bullet.jpg",game)
RocketAmmo=Image("images\\RocketAmmo.png",game)
Nuke=Image("images\\Nuke.gif",game)

gun=Sound("sound\\GunSound.wav",1)
rocket=Sound("sound\\Arcade Explo A.wav",2)
background=Sound("sound\\Left 4 Dead - Witch.wav",3)
############################################################
Zombies=[]

for times in range(100):
    Zombies.append(Image("images\\Alive.png",game))
    
for z in Zombies:
    x = randint(950,10000)
    y = randint(600,750)
    z.moveTo(x,y)
    
    z.setSpeed(2,90)
#######################################################
"""
Nukes=[]
for times in range(50):
    Nukes=Image("images\\Nuke.gif",game)

for n in Nukes:
    x = randint(100,700)
    y = -randint(100,5000)
    s = randint(1,3)
    n.moveTo(x,y)
    n.setSpeed(s,180)"""
################################################
Idle.resizeBy(30)
Idle.setSpeed(6,60)
Idle.moveTo(75,640)

Jeep.resizeBy(20)
Jeep.moveTo(-3.5,720)

Shoot.resizeBy(30)
Shoot.moveTo(75,640)

Rocket.resizeBy(30)
Rocket.moveTo(75,640)
                                     
Pain.resizeBy(30)
Pain.moveTo(75,640)

Slash.moveTo(75,640)

z.resizeBy(10)
Aim.resizeBy(-80)
Boom.moveTo(z.x,z.y)

Bullet.resizeBy(-92.5)
RocketAmmo.resizeBy(-75)

"""Nuke.resizeBy(-90)"""

#######################################################
print("Startup Screen")
game.scrollBackground("right",3)
game.drawText("Last One Standing",game.width/4 ,game.height/4,Font(black,90,red))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(green,40,black))
background.play()
game.update()
game.wait(K_SPACE)

status = "Idle"
print("Game Begins")
Bullet.setSpeed(10,-90)
Bullet.visible= False

RocketAmmo.setSpeed(10,-90)
RocketAmmo.visible= False

kills = 0
Idle.health=100
Shoot.health=200
######################################################
while not game.over:
    game.processInput()
    game.scrollBackground("right",3)
    hideAll()
    Jeep.draw()
    Aim.draw()
    Boom.draw(False)
    Bullet.moveTowards(mouse,10)
    RocketAmmo.moveTowards(mouse,10)
    """for n in Nukes:
        n.move()"""
    print("In Game")
    background.play()
######################################################   
    for z in Zombies:
        z.move()
        if z.collidedWith(RocketAmmo, "rectangle"):
            Boom.moveTo(z.x,z.y)
            Boom.visible=True
            Boom.f=0
            z.visible= False
            RocketAmmo.visible=False
            kills += 1
        if z.collidedWith(Idle,"rectangle"):
            z.visible= False          
            Slash.visible=True
            status = "Pain"
            Idle.health-=3
        if z.collidedWith(Jeep,"rectangle"):
            z.visible= False         
            Slash.visible=True
            status = "Pain"
            Idle.health-=3
        if z.collidedWith(Shoot,"rectangle"):
            z.visible= False
            Slash.visible=True
            status = "Pain"
            Idle.health-=3
        if z.collidedWith(Rocket,"rectangle"):
            z.visible= False
            Slash.visible=True
            status = "Pain"
            Idle.health-=3
        if z.collidedWith(Bullet, "rectangle"):
            z.visible= False
            Bullet.visible=False
            kills += 1
        if z.collidedWith(Boom, "rectangle"):
            z.visible=False
            kills +=1
#############################################################                 
    Aim.moveTo (mouse.x, mouse.y)
    if mouse.LeftButton and Shoot.health >0:
        Shoot.moveTo(Idle.x,Idle.y)
        Shoot.visible=True
        Shoot.draw()
        Shoot.health-=0.5
        Bullet.visible=True
        Bullet.moveTo(Idle.x, Idle.y)
        gun.play()
    elif mouse.RightButton and Shoot.health >0:
        Rocket.moveTo(Idle.x,Idle.y)
        Rocket.visible=True
        Rocket.draw()
        Shoot.health-=1
        RocketAmmo.visible=True
        RocketAmmo.moveTo(Idle.x, Idle.y)
        rocket.play()
    else:       
        if status == "Pain":
            Pain.moveTo(Idle.x,Idle.y)
            Pain.visible=True
            Pain.draw(False)
            if Pain.visible == False:
                status = "Idle"
        else:
            Idle.visible=True
            Idle.draw()
            
    """if keys.Pressed[K_q]:
        n.visible=True
        n.moveTo(z.x,z.y)"""
        
################################################################
    if Idle.health <0 or Shoot.health <0 :
        game.over=True
################################################################   
    Slash.draw()
    game.drawText("Health:" + str(Idle.health),5,10)
    game.drawText("Ammo:" + str(Shoot.health),112,10)
    game.drawText("Kills:" + str (kills),210,10)
    game.update(70)
###############################################################
    game.drawText("Game Over",game.width/4 ,game.height/4,Font(black,90,red))
    game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(green,40,black))
game.update()
game.wait(K_ESCAPE)
   
game.quit()
