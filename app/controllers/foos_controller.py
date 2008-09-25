from application_controller import ApplicationController
from app.models.greeting import Greeting
class FoosController(ApplicationController):
  def index(self):
    """docstring for index"""
  
  def show(self):
    """docstring for show"""
    g = Greeting()
    g.content = "well hello there!"
    self.context['greeting'] = g
    self.render_view('foos/show.html')
  