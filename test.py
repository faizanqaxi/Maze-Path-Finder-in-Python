with open('test.txt') as f:
    contents = f.read()
    contents = contents.splitlines()

print((max(len(line) for line in contents)))
