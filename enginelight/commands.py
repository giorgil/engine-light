import os
from paste.script import command
from Cheetah.Template import Template

class ModelCommand(command.Command):
  min_args = 1
  max_args = 1
  group_name = 'enginelight'
  summary = 'Creates a model'
  parser = command.Command.standard_parser(verbose=True)
  
  def command(self):
    template = Template(file=(os.path.dirname(__file__) + '/templates/model.py_tmpl'), searchList={'name': self.args[0]})
    self.ensure_dir('app/models', svn_add=False)
    self.ensure_file(('app/models/' + self.args[0].lower() + '.py'), template.__str__(), svn_add=False)


class ControllerCommand(command.Command):
  min_args = 1
  max_args = 1
  group_name = 'enginelight'
  summary = 'Creates a controller'
  parser = command.Command.standard_parser(verbose=True)
  
  
  def command(self):
    template = Template(file=(os.path.dirname(__file__) + '/templates/controller.py_tmpl'), searchList={'name': self.args[0]})
    self.ensure_dir('app/controllers', svn_add=False)
    self.ensure_file(('app/controllers/' + self.args[0].lower() + '_controller.py'), template.__str__(), svn_add=False)
  
class ResourceCommand(command.Command):
  min_args = 1
  max_args = 1
  group_name = 'enginelight'
  
