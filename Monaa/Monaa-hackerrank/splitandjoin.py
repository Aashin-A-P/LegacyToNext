line="this is a string"

def split_and_join(line):
          a=line.split(" ")
          return"-".join(a)
result = split_and_join(line)
print(result)