# with open('factorial/newFile.txt', 'w') as file:
#     file.write('written again')

with open('factorial/newFile.txt', 'a+') as file:
    file.write('will be appended')
    file.seek(0)
    print(file.read())
