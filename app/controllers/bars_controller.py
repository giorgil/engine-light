from application_controller import ApplicationController

class BarsController(ApplicationController):
  def index(self):
    """docstring for index"""
  
  def show(self):
    """docstring for show"""
    self.render_view('bars/show.html')
