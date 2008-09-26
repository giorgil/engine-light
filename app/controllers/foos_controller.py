from application_controller import ApplicationController
from app.models.greeting import Greeting
class FoosController(ApplicationController):
  def index(self):
    """docstring for index"""
    self.context['greetings'] = Greeting.all().fetch(10)
    self.render_view('foos/index.html')
  
  def show(self):
    """docstring for show"""
    Greeting.get_by_id(2)
    self.context['greeting'] = Greeting.get_by_id(2)
    self.context['x'] = self.request.arguments()
    self.render_view('foos/show.html')
  