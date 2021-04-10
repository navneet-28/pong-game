from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    points=NumericProperty(0)
    def bounce(self,ball):
        if self.collide_widget(ball):
            ball.velocity_x*=-1
class PongBall(Widget):
    velocity_x=NumericProperty(0)
    velocity_y=NumericProperty(0)
    velocity=ReferenceListProperty(velocity_x,velocity_y)
    def move(self):
        self.pos= Vector(*self.velocity) +self.pos

class PongGame(Widget):
    ball=ObjectProperty(None)
    firstPlayer=ObjectProperty(None)
    secondPlayer=ObjectProperty(None)
    def serve_ball(self):
        self.ball.velocity = Vector(7,0).rotate(randint(0,360))
    def update(self,dt):
        self.ball.move()
        if (self.ball.y<0) or (self.ball.y+50>self.height):
            self.ball.velocity_y*= -1
        if self.ball.x<0:
            self.ball.velocity_x*= -1
            self.secondPlayer.points +=1
        if self.ball.x+50>self.width:
            self.ball.velocity_x*= -1
            self.firstPlayer.points +=1
        self.firstPlayer.bounce(self.ball)
        self.secondPlayer.bounce(self.ball)
    def on_touch_move(self, touch):
        if touch.x<self.width / 1/4:
            self.firstPlayer.center_y=touch.y
        if touch.x>self.width * 3/4:
            self.secondPlayer.center_y=touch.y

class PongApp(App):
    def build(self):
        game=PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
    
PongApp().run()