def add(a, b):
  return a + b

def sub(a, b):
  return a - b

if(__name__ == "__main__"):
  print(
    "이 프로그램은 자체적으로 실행되고 있습니다."
  )
print(__name__)
print(add(1, 4))
print(sub(4, 2))