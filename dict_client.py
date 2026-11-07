# Abel's Dictionary Client - v2 with ADD
import socket
import json

action = input("Do you want to QUERY or ADD a word? ").upper()

if action == "ADD":
    word = input("What word to add? ")
    meaning = input(f"What does '{word}' mean? ")
    request = {"command": "ADD", "word": word, "meaning": meaning}
else:
    word = input("What word do you want to look up? ")
    request = {"command": "QUERY", "word": word}

client = socket.socket()
client.connect(("localhost", 5000))
client.send(json.dumps(request).encode())

data = client.recv(1024).decode()
response = json.loads(data)
print(f"\n{response['meaning']}")
client.close()