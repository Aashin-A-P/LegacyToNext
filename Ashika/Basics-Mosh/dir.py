from pathlib import Path

path1=Path("packages1.py")
print(path1.exists())
path2=Path("dir1")
print(path2.mkdir())
print(path2.rmdir())
print(path1.glob('*'))

for i in path1.glob('*.py'):
    print(i)

