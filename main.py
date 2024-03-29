from turtle import Turtle


class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
        self.points = 0
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_left(self):
        new_x = self.xcor() - self.step
        if -s_width / 2 < new_x < s_width / 2:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + self.step
        if -s_width / 2 < new_x < s_width / 2:
            self.goto(new_x, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

s_width = 200
s_height = 180

player = Sprite(0, -100, 10, 'circle', 'orange')
enemy1 = Sprite(-s_width, 0, 15, 'square', 'red')
enemy1.set_move(-s_width, 0, s_width, 0)
enemy2 = Sprite(s_width, 70, 15, 'square', 'red')
enemy2.set_move(s_width, 70, -s_width, 70)
goal = Sprite(0, 120, 20, 'triangle', 'green')

scr = player.getscreen()
scr.listen()


scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

total_goals = 0
while total_goals < 3:
    enemy1.make_step()
    enemy2.make_step()

    if player.is_collide(goal):
        player.goto(0, -100)
        total_goals += 1

    if player.is_collide(enemy1) or player.is_collide(enemy2):
        goal.hideturtle()
        break

if total_goals == 3:
    enemy1.hideturtle()
    enemy2.hideturtle()
