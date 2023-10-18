import socket

def send_file(server_socket, file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                server_socket.send(data)
                data = file.read(1024)
            print("File sent successfully")
    except Exception as e:
        print(f"Error sending file: {str(e)}")




server_ip = '192.168.50.130'  # Replace with the server's IP address
server_port = 12344
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

#file_names = ['/home/saliih/Desktop/test/msg', '/home/saliih/Desktop/test/n', '/home/saliih/Desktop/test/public_key']

#with open('/home/saliih/Desktop/test/all', 'wb') as file:
#	data = client_socket.recv(1024)
#	file.write(data)

#output_file_path = ['/home/saliih/Desktop/test/msg', '/home/saliih/Desktop/test/n', '/home/saliih/Desktop/test/public_key']	

#with open('/home/saliih/Desktop/test/all', 'r') as file:
#	for j in range(3):
#		line = file.readline()
#		with open(output_file_path[j], 'w') as output_file:
#			output_file.write(line)

        
msg = client_socket.recv(1024)   
msg = msg.decode('utf-8')    
#file_path = "/home/saliih/Desktop/test/public_key"
#with open(file_path, "r") as file:
#		public_key=file.readline()
#		public_key=public_key.strip()
public_key = client_socket.recv(1024)
public_key = public_key.decode('utf-8')
public_key = int(public_key)
#public_key=int(public_key)


#file_path = "/home/saliih/Desktop/test/n"
#with open(file_path, "r") as file:
#		n=file.readline()
#		n=n.strip()
n=client_socket.recv(1024)
n=n.decode('utf-8')
n=int(n)

# To encrypt the given number
def encrypt(message):
	global public_key, n
	e = public_key
	encrypted_text = 1
	while e > 0:
		encrypted_text *= message
		encrypted_text %= n
		e -= 1
	return hex(encrypted_text)


# First converting each character to its ASCII value and
# then encoding it then decoding the number to get the
# ASCII and converting it to character
def encoder(message):
	encoded = []
	# Calling the encrypting function in encoding function
	for letter in message:
		encoded.append(encrypt(ord(letter)))
	return encoded




if __name__ == '__main__':
	# Define the path to where you want to save the received file from the server
	
	#file_path = "/home/saliih/Desktop/test/msg"
	#with open(file_path, "r") as file:
	#	msg=file.readline()
	#	msg=msg.strip()
	print ("msg: "+msg)
	print ("publickey: "+str(public_key))
	print("n: "+str(n))

	print("\n\nThe encoded message(encrypted by public key)\n")
	print(''.join(str(p) for p in msg[len(msg)//2:]))
	print(''.join(str(p) for p in encoder(msg[len(msg)//2:])))
	encodedmsg=''.join(str(p) for p in encoder(msg[len(msg)//2:]))
	file_path_to_encoded1 = "/home/edge2/Desktop/node/endcoded2"
	with open(file_path_to_encoded1, "w") as file:
		file.write(encodedmsg+"\n")
	
	# Specify the path to the file you want to send from the client
	#send_file(client_socket, 'endcoded1')
	#client_socket.send(encodedmsg)
	client_socket.close()
	server_ip = '192.168.50.130'  # Replace with the server's IP address
	server_port = 12346
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((server_ip, server_port))
	encodedmsg=str(encodedmsg)
	encodedmsg=encodedmsg.encode('utf-8')
	client_socket.send(encodedmsg)
	client_socket.close()
	
	
	
	

