import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except: 
        return False

for x in range(1, 1023):
    if pscan(x):
        print('Port',x, 'is open !!!!!')
    else:
        print('Port',x, 'is closed')