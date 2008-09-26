def routing(m):
  m.resource('foo', 'foos')
  m.resource('bar', 'bars')
  m.connect(':controller/:action/:id')
  return m