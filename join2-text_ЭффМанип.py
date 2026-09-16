from timeit import timeit
наб = ['1']*10_000
def наи():
  отв = ''
  for сим in наб:
    отв += сим+'-'
  return отв[:-1]
def эфф():
  return '-'.join(наб)
print(наи()==эфф()) # True
вр_наи = timeit('наи()', globals=globals(), number=1000)
вр_эфф = timeit('эфф()', globals=globals(), number=1000)
print(вр_наи // вр_эфф)

