# Fog Network Distributed Encryption and Decryption

## Project Overview

The Fog Network Encryption and Decryption project is a simulated network of fog devices, establishing a distributed system for secure data transformation. Within this architecture, a client communicates with a server, where the server tasks two fog nodes with the encryption of user-supplied messages. Subsequently, the server conveys the encrypted content back to the client for decryption.

## System Architecture

This project encompasses the following core elements:

- **Client**: This component initiates the process by generating its unique public and private keys via the RSA algorithm. The user is prompted to input the message for encryption.

- **Server**: Comprising two fog nodes, the server deploys Python scripts named "encryption.py." Each of these nodes establishes a connection with the client, receiving half of the message for encryption, along with the client's public key. Both nodes independently perform encryption and subsequently transmit the encrypted content to the client.
 <div align="center">
  <img src="https://github.com/bensalahmohameed/devops-fog/assets/100475606/43638fff-522b-4e71-9662-ce3c9a9d9da6" alt="Architecture FOG textEncryption (1)">
</div>


## Solution Strategy

The client-server communication is facilitated using Python sockets, ensuring the seamless exchange of data. Here is the step-by-step workflow:

1. The client executes "rsa.py" to create its public and private keys using the RSA algorithm. Simultaneously, it collects user input for the message requiring encryption.

2. The server, represented by two fog nodes, employs "encryption.py." Each node connects to the client, accepting a portion of the message and the client's public key. The message is encrypted, and the resulting encrypted segments are returned to the client.

3. On the client-side, running "decrypt.py" enables the reception of the encrypted segments. It assembles these segments, utilizing its private key to decrypt the content, ultimately reconstructing the original message.

## Usage Instructions

To execute the project, follow these instructions:

1. Begin by cloning the project repository onto your client machine using the following command:

   ```bash
   git clone https://github.com/bensalahmohameed/devops-fog.git
2. Distribute "encrypt1.py" to the first fog node and "encrypt2.py" to the second fog node.
3. On the client machine, ensure that "rsa.py" and "decrypt.py" are available.
4. Execute the following commands in the specified sequence:

   - On the client machine, open a terminal and run the following commands:

     ```bash
     python3 rsa.py
     python3 decrypt.py
     ```

   - On the first fog node:
   ```bash
   python3 encrypt1.py
   ```

   - On the second fog node:

   ```bash
   python3 encrypt2.py
   ```

4. On the client machine, input the message to be processed as directed.

## Additional Information

Throughout the process, each machine autonomously creates files to preserve outputs and document the workflow.

Please ensure to change the ip adress of the socket to the actual client ip in all files












