x='Test.bat'
with open(x, 'r') as file:
    commands=[]
    for line in file:
        if line[-1:]=='\n':
            commands.append(line[:-1])
        else:
            commands.append(line)
    print(commands)
