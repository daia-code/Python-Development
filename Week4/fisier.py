# file = open('data.txt', 'r+')
# file.write("Hello")
# file.close()

# file=open('data3.txt','w')
# try:
#     file.write('hello')
# finally:
#     file.close()

# with open('data.txt', 'w') as file:
#     file.write('course python1\n course python2')

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line, 'line')

# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)

with open('data.txt', 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break
        print(line)
