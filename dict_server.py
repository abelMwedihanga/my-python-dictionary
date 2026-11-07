# Abel's Dictionary Server - Python version
# Same idea as your old Java project, just simpler
import socket
import json
import threading

# Our dictionary - starts with 3 words
dictionary = {
    "hello": "a greeting",
    "code": "instructions for a computer",
    "windhoek": "capital city of Namibia"
}

def handle_client(conn):
    data = conn.recv(1024).decode()
    request = json.loads(data)  # Same JSON as your Java project!
    
    command = request.get("command")
    word = request.get("word", "").lower()
    
    if command == "QUERY":
        meaning = dictionary.get(word, "Word not found")
        response = {"status": "OK", "meaning": meaning}
    elif command == "ADD":
        dictionary[word] = request.get("meaning")
        response = {"status": "OK", "meaning": "Word added!"}
    else:
        response = {"status": "ERROR", "meaning": "Unknown command"}
    
    conn.send(json.dumps(response).encode())
    conn.close()

# Start the server - like your old Java Server
server = socket.socket()
server.bind(("localhost", 5000))
server.listen(5)
print("Abel's Dictionary Server is RUNNING on port 5000...")

while True:
    conn, addr = server.accept()
    print(f"New connection from {addr}")
    threading.Thread(target=handle_client, args=(conn,)).start()