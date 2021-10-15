import turtle

def funk1():
    tosh.pencolor(ranglar[rang])
    tosh.forward(50)

def funk2():
    tosh.left(45)

def funk3():
    tosh.right(45)

def funk4():
    wn.bye()

def funk5():
    global pensz
    pensz += 1
    tosh.pensize(pensz)
    
        
def funk6():
    global pensz
    pensz = pensz - 1
    if pensz > 0:
        tosh.pensize(pensz)
    else:
        pensz = 1
        tosh.pensize(pensz)

def funk7():
    global ruchka
    if ruchka == 1:
        tosh.penup()
        ruchka = 0
    else:
        tosh.pendown()
        ruchka = 1 
def funk8():
    tosh.pencolor("green")
    tosh.back(50)

def funk9():
    global rang
    if rang >5:
        rang = 0
    else:
        ranglar = ["yellow","orange","white","red","brown","purple"]
        tosh.pencolor(ranglar[rang])
        rang += 1
def funk10(tekst, x, y):
    tanish = turtle.Turtle()
    tanish.penup()
    tanish.goto(x,y)
    tanish.write(tekst, font=10)
    tanish.hideturtle()
def funk11():
    global kattalik
    kattalik += 1
    tosh.turtlesize(kattalik)
def funk12():
    global kattalik
    kattalik = kattalik - 1
    if kattalik > 0:
        tosh.turtlesize(kattalik)
    else:
        kattalik = 1
        tosh.turtlesize(kattalik)
    
    
    
def main():
    global tosh
    global wn
    global pensz
    global ruchka
    global rang
    global ranglar
    global kattalik
    kattalik = 1
    rang = 0
    ruchka = 1
    wn = turtle.Screen()
    wn.setup(700, 500)
    wn.bgcolor("green")
    wn.title("toshbaqa dasturi")
    tosh = turtle.Turtle()
    pensz = 1
    ranglar = ["black","yellow","orange","white","red","brown","purple"]
    turtle.pensize(pensz)
    funk10("'↑' - Oldinga yurish ", 700 , 375)
    funk10("'→' - O'ngga  yurish ", 700 , 350)
    funk10("'←' - Chapga yurish ", 700 , 325)
    funk10("'d' - Rangdi o'zgartirish ", 700 , 300)
    funk10("'space' - Ruchkani ko'tarish ", 700 , 275)
    funk10("'↓' - O'chirish ", 700 , 250)
    funk10("'a' - Shriftni kattalashtirish ", 700 , 225)
    funk10("'s' - Shriftni kichiklashtirish ", 700 , 200)
    funk10("'w' - Toshbaqani kattalashtirish ", 700 , 175)
    funk10("'e' - Toshbaqani kichiklashtirish ", 700 , 150)
    funk10("q' - Dasturdan chiqish ", 700 , 125)
    funk10(" created by bekzodjon_python_master ", 650 , 100)
            

    wn.onkey(funk1,"Up")
    wn.onkey(funk2,"Left")
    wn.onkey(funk3,"Right")
    wn.onkey(funk4,"q")
    wn.onkey(funk5,"a")
    wn.onkey(funk6,"s")
    wn.onkey(funk7,"space")
    wn.onkey(funk8,"Down")
    wn.onkey(funk9,"d")
    wn.onkey(funk11,"w")
    wn.onkey(funk12,"e")
    
    
    wn.listen()
    wn.mainloop()
main()


