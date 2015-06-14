from multiprocessing.connection import Listener
from array import array

address = ('localhost', 12000)     # family is deduced to be 'AF_INET'
auth_key = b'secret password'

with Listener(address, authkey=auth_key) as listener:
	with listener.accept() as conn:
		print('connection accepted from', listener.last_accepted)

		#conn.send([2.25, None, 'junk', float])
		#conn.send_bytes(b'hello')
		#conn.send_bytes(array('i', [42, 1729]))

		conn.send('READY TO AUTH')
		R = conn.recv()
		if R == 'OK':
			conn.send('NAME')
			N = conn.recv()
			if N:
				print('NAME = %s ' % N)
				conn.close()
		else:
			print("Client not ready to AUTH")
			conn.close()
			
