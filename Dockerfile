FROM alpine:latest

# Install SSH server and generate host keys
RUN apk add openssh

# Set a password for the root user (change 'your-password' to your desired password)
RUN echo 'root:your-password' | chpasswd

# Expose SSH port
EXPOSE 22

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]

