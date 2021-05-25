import socket

def connectToServer(HOST, PORT):
	"""Create a socket connection with the Server and connect to it.

	Parameters
	----------
	HOST : str
		IP address of Host or Server, the Client needs to connect to
	PORT : int
		Port address of Host or Server, the Client needs to connect to

	Returns
	-------
	socket
		Object of socket class for connecting and communication to Server
	"""

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.connect((HOST, PORT))

	return server_socket


def formatRecvdData(data_recvd):
	"""Format the data received from the Server as required for better representation.

	Parameters
	----------
	data_recvd : str
		Data received from the Server about scheduling of Vaccination Appointment
	"""

	##############	ADD YOUR CODE HERE	##############
	
	print(data_recvd)	

	##################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""

	HOST = '127.0.0.1'
	PORT = 24680

	# Start the connection to the Server
	server_socket = None
	try:
		server_socket = connectToServer(HOST, PORT)
	except ConnectionRefusedError:
		print("*** Start the server first! ***")

	# Receive the data sent by the Server and provide inputs when asked for.
	if server_socket != None:
		while True:
			data_recvd = server_socket.recv(1024).decode('utf-8')
			formatRecvdData(data_recvd)
			if '>>>' in data_recvd:
				print()				
				data_to_send = input()			
				server_socket.sendall(data_to_send.encode('utf-8'))

			elif '<<<' in data_recvd:
				print()

			elif not data_recvd:
				server_socket.close()
				break
		
		server_socket.close()
