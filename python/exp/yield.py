def output():
  for i in range(1,10):
    yield i

print(next(output()))
print(next(output()))
