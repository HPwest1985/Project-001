import socket, threading

host = input("Enter an address to scan: ")
ip = socket.gethostbyname(host)
threads = []
open_ports = {}
import parser

def load_suite(source_string):
    st = parser.suite(source_string)
    return st, st.compile()

def load_expression(source_string):
    st = parser.expr(source_string)
    return st, st.compile()

def try_port(ip, port, delay, open_ports):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(delay)
    result = sock.connect_ex((ip, port))

    if result == 0:
        open_ports[port] = 'open'
        return True
    else:
        open_ports[port] = 'false'
        return None 

def scan_ports(ip, delay): 

    for port in range(0, 1023): 
        thread = threading.Thread(target=try_port, args=(ip, port, delay, open_ports))
        threads.append(thread)

    for i in range(0, 1023): 
        threads[i].start()

    for i in range(0, 1023):
        threads[i].join()

    for i in range(0, 1023):
        if open_ports[i] =='open':
            print  is open
        if i == 1022:
            print is 'finish'

if '_name_' == "_main_":
    scan_ports(ip, 3) #3 is the delay 