from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os, glob, sys

# set a gloabl APP_ROOT
from framework.root import APP_ROOT

# add the framework, congiuration, and application folders as places to look for modules
sys.path.append(APP_ROOT + '/framework')
sys.path.append(APP_ROOT + '/config')
sys.path.append(APP_ROOT + '/app/models')
sys.path.append(APP_ROOT + '/app/controllers')

import framework
import routes
import config.routes
import app.controllers 

# Create a new routing mapper and give it the contents of config/routes.py
m = routes.Mapper()
m = config.routes.routing(m)

# Routes needs to know all the controllers to generate the 
# regular expressions.
controllers = []
for file in glob.glob(os.path.join((globals()['APP_ROOT'] + '/app/controllers'), '*_controller.py')):
  controllers.append(os.path.basename(file).replace('_controller.py',''))
m.create_regs(controllers)

class Router(webapp.RequestHandler):  
  def get(self):
    m.environ = {'REQUEST_METHOD':'GET'}
    controller = m.match(self.request.path)
    __import__('app.controllers.' + controller['controller'] + '_controller')
    eval("app.controllers." + controller['controller'] +"_controller." + controller['controller'].capitalize() + "Controller(self.request, self.response)." + controller['action'] + '()')

# send all requests to the better Router
application = webapp.WSGIApplication([('.*', Router)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()