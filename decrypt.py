import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.50.130'  # Use the server's actual IP address
server_port = 12346

server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

client_socket2, client_address2 = server_socket.accept()
print(f"Accepted connection from {client_address2}")


file_path = "/home/saliih/Desktop/projet-fog/private_key"
with open(file_path, "r") as file:
		private_key=file.readline()
		private_key=private_key.strip()
private_key=int(private_key)

# file_path = "/home/saliih/Desktop/projet-fog/endcoded1"
# with open(file_path, "r") as file:
# 		encodedmsg1=file.readline()
# 		encodedmsg1=encodedmsg1.strip()
encodedmsg1=client_socket.recv(1024)	
encodedmsg1=encodedmsg1.decode('utf-8')
encodedmsg1=encodedmsg1.split("0x")[1:]

encodedmsg11=[]
for c in encodedmsg1:
	encodedmsg11.append(int(c,16))



#encodedmsg1=int(encodedmsg1)

# file_path = "/home/saliih/Desktop/projet-fog/endcoded2"
# with open(file_path, "r") as file:
# 		encodedmsg2=file.readline()
# 		encodedmsg2=encodedmsg2.strip()
encodedmsg2=client_socket2.recv(1024)
encodedmsg2=encodedmsg2.decode('utf-8')
encodedmsg2=encodedmsg2.split("0x")[1:]
encodedmsg22=[]
for c in encodedmsg2:
	encodedmsg22.append(int(c,16))
#encodedmsg2=int(encodedmsg2)


file_path = "/home/saliih/Desktop/projet-fog/n"
with open(file_path, "r") as file:
		n=file.readline()
		n=n.strip()
n=int(n)


# To decrypt the given number
def decrypt(encrypted_text):
	global private_key, n
	d = private_key
	decrypted = 1
	while d > 0:
		decrypted *= encrypted_text
		decrypted %= n
		d -= 1
	return decrypted


def decoder(encoded):
	s = ''
	# Calling the decrypting function decoding function
	for num in encoded:
		s += chr(decrypt(num))
	return s


if __name__ == '__main__':
	print("\n\nThe decoded message(decrypted by private key)\n")
	print(''.join(str(p) for p in decoder(encodedmsg11)),''.join(str(p) for p in decoder(encodedmsg22)))
	

client_socket.close()
client_socket2.close()
server_socket.close()
