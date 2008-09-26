from application_controller import ApplicationController
from app.models.greeting import Greeting
class FoosController(ApplicationController):
  def index(self):
    """docstring for index"""
    self.view['greetings'] = Greeting.all().fetch(10)
    self.render_view('foos/index.html')
  
  def show(self):
    """docstring for show"""
    self.view['greeting'] = Greeting.get_by_id(int(self.request.params['id']))
    self.view['x'] = self.request.arguments()
    self.render_view('foos/show.html')
  