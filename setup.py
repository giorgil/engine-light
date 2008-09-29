from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='enginelight',
      version=version,
      description="a lightweight controller class for google app engine",
      long_description="""\
""",
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet",
      ],
      keywords='google appengine',
      author='Trek Glowacki',
      author_email='trek.glowacki@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      data_files=[('enginelight/templates/application', ['enginelight/templates/application/index.yaml_tmpl']),
                  ('enginelight/templates/application', ['enginelight/templates/application/app.yaml_tmpl']),
                  ('enginelight/templates', ['enginelight/templates/controller.py_tmpl']),
                  ('enginelight/templates', ['enginelight/templates/model.py_tmpl']),
                  ('enginelight/templates/application/+package+.egg-info', ['enginelight/templates/application/+package+.egg-info/paster_plugins.txt'])
                  ],
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.paster_command]
      controller = enginelight.commands:ControllerCommand
      model = enginelight.commands:ModelCommand
      resource = enginelight.commands:ResourceCommand
      
      [paste.global_paster_command]
      
        
      [paste.paster_create_template]
      enginelight = enginelight.template:FrameworkTemplate
      """
      )
