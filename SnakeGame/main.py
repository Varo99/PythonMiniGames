import turtle, time, random

pausa = False
score = 0
with open("highscore.txt","r") as file:
    highscore = int(file.read())
print(highscore)

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Snake the game")
ventana.bgcolor("black")
ventana.setup(width=900, height= 900)
ventana.tracer(0)

# Cabeza de la snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("orange")
head.penup()
head.goto(0,0)
head.direction = ""

# Cuerpo de la snake
body = []

# comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
comidax = random.randint(-430,430)
comiday = random.randint(-430,430)
food.goto(comidax, comiday)

# Texto Score
texto = turtle.Turtle()
texto.speed(0)
texto.color("red")
texto.penup()
texto.hideturtle()
texto.goto(0,420)
texto.write(f"Score: {score}           High Score: {highscore}", align="center", font=("Times New Roman", 22, "normal"))

# Texto de pausa
pausetext = turtle.Turtle()
pausetext.speed(0)
pausetext.color("white")
pausetext.penup()
pausetext.hideturtle()
pausetext.goto(0, 0)
pausetext2 = turtle.Turtle()
pausetext2.speed(0)
pausetext2.color("white")
pausetext2.penup()
pausetext2.hideturtle()
pausetext2.goto(0, -20)

# Texto de Game Over
gameover = turtle.Turtle()
gameover.speed(0)
gameover.color("white")
gameover.penup()
gameover.hideturtle()
gameover.goto(0, -20)

# funciones
def pausa():
    global pausa
    if pausa == False:
        pausa = True
    else:
        pausa = False
def arriba():
    head.direction = "up"
def abajo():
    head.direction = "down"
def derecha():
    head.direction = "right"
def izquierda():
    head.direction = "left"
def movimiento():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Escuchar teclado
ventana.listen()
ventana.onkeypress(arriba, "w")
ventana.onkeypress(abajo, "s")
ventana.onkeypress(derecha, "d")
ventana.onkeypress(izquierda, "a")
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(pausa, " ")

# Bucle de ejecución
while True:
    ventana.update()
    # Check colisiones
    # Bordes
    if head.xcor() > 430 or head.xcor() < -430 or head.ycor() > 430 or head.ycor() < -430:
        time.sleep(1)
        # Save score
        if score > highscore:
            highscore = score
            with open("highscore.txt", "w") as file:
                file.write(str(highscore))
        score = 0
        texto.clear()
        texto.write(f"Score: {score}           High Score: {highscore}", align="center",
                    font=("Times New Roman", 21, "normal"))
        # Remove body
        for segment in body:
            segment.goto(5000, 5000)
        body = []
        # Restart
        head.goto(0, 0)
        head.direction = ""
    # Body
    for segment in body:
        if head.distance(segment) < 20:

            time.sleep(1)
            # Save score
            if score > highscore:
                highscore = score
                with open("highscore.txt","w") as file:
                    file.write(str(highscore))
            score = 0
            texto.clear()
            texto.write(f"Score: {score}           High Score: {highscore}", align="center",
                        font=("Times New Roman", 21, "normal"))
            # Remove body
            for segment in body:
                segment.goto(5000, 5000)
            body = []
            # Restart
            head.goto(0, 0)
            head.direction = ""
    # comida
    if head.distance(food) < 20:
        comidax = random.randint(-430, 430)
        comiday = random.randint(-430, 430)
        food.goto(comidax, comiday)
        # Body
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("yellow")
        segment.penup()
        segment.goto(0, 0)
        body.append(segment)
        # Update score
        score += 1
        texto.clear()
        texto.write(f"Score: {score}           High Score: {highscore}", align="center",
                    font=("Times New Roman", 21, "normal"))
    # Movimiento si el juego no esta pausado
    if pausa is not True:
        pausetext.clear()
        pausetext2.clear()
        # mover cuerpo de la sierrrrpe
        for index in range(len(body) - 1, 0, -1):
            x = body[index - 1].xcor()
            y = body[index - 1].ycor()
            body[index].goto(x, y)
        if len(body) > 0:
            x = head.xcor()
            y = head.ycor()
            body[0].goto(x, y)
        movimiento()
        time.sleep(0.1)

    # Pausa
    else:
        pausetext.write(f"PAUSED", align="center",
                    font=("Times New Roman", 22, "normal"))
        pausetext2.write(f"press 'space' to continue", align="center",
                        font=("Times New Roman", 14, "normal"))
