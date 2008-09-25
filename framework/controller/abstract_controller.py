import os
from framework.root import APP_ROOT
from google.appengine.ext.webapp import template
class AbstractController():
  def __init__(self, request, response):
    """docstring for __init"""
    self.request = request
    self.response = response
    self.context =  {}
  
  def render_view(self, file_name):
    """docstring for render"""
    path = os.path.join(APP_ROOT, ('app/views/' + file_name) )
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(template.render(path, self.context))
    
  def render_text(self, text):
    """docstring for render_text"""
    self.response.headers['Content-Type'] = 'text/text'
    self.response.out.write(text)
    
  def render_xml(self, xml):
    """docstring for render_xml"""
    self.response.headers['Content-Type'] = 'text/xml'

    
    
    