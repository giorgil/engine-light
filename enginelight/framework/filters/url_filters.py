from google.appengine.ext.webapp import template
from routes import util
 
register = template.create_template_register()
  
class UrlNode(template.Node):
  def __init__(self, arg):
    self.arg = arg
  
  def render(self):
    """docstring for render"""
    return "/ab/c/ac"
      
def url_for(parser, token):
  bits = list(token.split_contents())
  return UrlNode(bits[1])
 
register.tag(url_for)