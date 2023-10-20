# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
import math
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.50.130'  # Use the server's actual IP address
server_port = 12344

server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

client_socket2, client_address2 = server_socket.accept()
print(f"Accepted connection from {client_address2}")

# A set will be the collection of prime numbers,
# where we can select random primes p and q
prime = set()

public_key = None
private_key = None
n = None

# We will run the function only once to fill the set of
# prime numbers
def primefiller():
	# Method used to fill the primes set is Sieve of
	# Eratosthenes (a method to collect prime numbers)
	seive = [True] * 250
	seive[0] = False
	seive[1] = False
	for i in range(2, 250):
		for j in range(i * 2, 250, i):
			seive[j] = False

	# Filling the prime numbers
	for i in range(len(seive)):
		if seive[i]:
			prime.add(i)


# Picking a random prime number and erasing that prime
# number from list because p!=q
def pickrandomprime():
	global prime
	k = random.randint(0, len(prime) - 1)
	it = iter(prime)
	for _ in range(k):
		next(it)

	ret = next(it)
	prime.remove(ret)
	return ret


def setkeys():
	global public_key, private_key, n
	prime1 = pickrandomprime() # First prime number
	prime2 = pickrandomprime() # Second prime number

	n = prime1 * prime2
	fi = (prime1 - 1) * (prime2 - 1)

	e = 2
	while True:
		if math.gcd(e, fi) == 1:
			break
		e += 1

	public_key = e

	d = 2
	while True:
		if (d * e) % fi == 1:
			break
		d += 1
    
	private_key = d
	
	msg=input("what msg you want to encode ? ")
	
	file_path_to_privateKey = "/home/saliih/Desktop/projet-fog/private_key"
	file_path_to_publicKey = "/home/saliih/Desktop/projet-fog/public_key"
	file_path_to_n = "/home/saliih/Desktop/projet-fog/n"
	file_path_to_msg="/home/saliih/Desktop/projet-fog/msg"
	
	msge=msg.encode('utf-8')
	client_socket.send(msge)
	client_socket2.send(msge)
	with open(file_path_to_msg, "w") as file:
		file.write(msg+"\n")
	
	with open(file_path_to_privateKey, "w") as file:
		file.write(str(private_key)+"\n")
	
	public_keye=str(public_key)
	public_keye=public_keye.encode('utf-8')
	client_socket.send(public_keye)
	client_socket2.send(public_keye)
	with open(file_path_to_publicKey, "w") as file:
		file.write(str(public_key)+"\n")
	
	ne=str(n)
	ne=ne.encode('utf-8')
	client_socket.send(ne)
	client_socket2.send(ne)
	with open(file_path_to_n, "w") as file:
		file.write(str(n)+"\n")
	
#------------------------------------------------------------------------------------	
#MAIN
primefiller()
setkeys()

client_socket.close()
client_socket2.close()
server_socket.close()

