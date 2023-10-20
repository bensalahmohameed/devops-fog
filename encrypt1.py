import socket

server_ip = '192.168.50.130'  # Replace with the server's IP address
server_port = 12344
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
        
msg = client_socket.recv(1024)   
msg = msg.decode('utf-8')    

public_key = client_socket.recv(1024)
public_key = public_key.decode('utf-8')
public_key = int(public_key)

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
	
	print ("msg: "+msg)
	print ("publickey: "+str(public_key))
	print("\n\nThe encoded message(encrypted by public key)\n")
	print(''.join(str(p) for p in msg[:len(msg)//2]))
	print(''.join(str(p) for p in encoder(msg[:len(msg)//2])))
	encodedmsg=''.join(str(p) for p in encoder(msg[:len(msg)//2]))
	file_path_to_encoded1 = "/home/saliih/Desktop/test/endcoded1"
	with open(file_path_to_encoded1, "w") as file:
		file.write(encodedmsg+"\n")
	client_socket.close()


	#Connecting to the server to send encrypted data to be decrypted
	server_ip = '192.168.50.130'  # Replace with the server's IP address
	server_port = 12346
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((server_ip, server_port))
	encodedmsg=str(encodedmsg)
	encodedmsg=encodedmsg.encode('utf-8')
	client_socket.send(encodedmsg)
	client_socket.close()


	
	
	

	
	
	
	
	
	

