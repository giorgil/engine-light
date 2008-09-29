from paste.script import templates

class FrameworkTemplate(templates.Template):
    egg_plugins = []
    summary = 'Template for creating a basic EngineLight application'
    _template_dir = 'templates/application'
    use_cheetah = True
