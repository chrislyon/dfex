## ----------------
## CLASS PARTNER
## ----------------

import ipaddress

class Partner(object):
	def __init__(self):
		self.name 				= 'partner'
		self.address 			= ipaddress.ip_address('127.0.0.1')
		self.port				= 12000
		self.my_name			= None
		self.partner_name		= None

	def __str__(self):
		return '<Partner:%s>' % self.name

def test():
	p = Partner()
	print(p)

if __name__ == '__main__':
	test()
