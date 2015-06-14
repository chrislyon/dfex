from multiprocessing.connection import Client
from array import array

address = ('localhost', 12000)

with Client(address, authkey=b'secret password') as conn:
    #print(conn.recv())                  # => [2.25, None, 'junk', float]
    #print(conn.recv_bytes())            # => 'hello'
    #arr = array('i', [0, 0, 0, 0, 0])
    #print(conn.recv_bytes_into(arr))    # => 8
    #print(arr)                          # => array('i', [42, 1729, 0, 0, 0])

	AUTH = conn.recv()
	if AUTH == 'READY TO AUTH':
		conn.send('OK')
	Q = conn.recv()
	if Q == 'NAME':
		conn.send('CLIENT1')
