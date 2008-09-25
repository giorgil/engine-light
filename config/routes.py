def routing(m):
  m.resource('foo', 'foos')
  m.connect(':controller/:action/:id')
  return m