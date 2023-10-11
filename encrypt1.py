file_path = "/home/saliih/Desktop/test/workspace/multibranch_main_2/public_key"
with open(file_path, "r") as file:
		public_key=file.readline()
		public_key=public_key.strip()
public_key=int(public_key)

file_path = "/home/saliih/Desktop/test/workspace/multibranch_main_2/n"
with open(file_path, "r") as file:
		n=file.readline()
		n=n.strip()
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
	file_path = "/home/saliih/Desktop/test/workspace/multibranch_main_2/msg"
	with open(file_path, "r") as file:
		msg=file.readline()
		msg=msg.strip()
		
	print("\n\nThe encoded message(encrypted by public key)\n")
	print(''.join(str(p) for p in msg[:len(msg)//2]))
	print(''.join(str(p) for p in encoder(msg[:len(msg)//2])))
	encodedmsg=''.join(str(p) for p in encoder(msg[:len(msg)//2]))
	file_path_to_encoded1 = "/home/saliih/Desktop/test/workspace/multibranch_main_2/endcoded1"
	with open(file_path_to_encoded1, "w") as file:
		file.write(encodedmsg+"\n")
		
    

