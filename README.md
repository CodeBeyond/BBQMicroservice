# BBQMicroservice
This microservice utilizes a TCP server for a client to send an HTTP request that utilizes JSON in order to send back a full list of BBQ recipes as well as tips. This microservice allows more flexibility for my partner's website because it is an effecient alternative to hardcoding multiple recipes and tips directly.

REQUEST data from the microservice:
First, get the TCP server .py file running. Make sure all firewalls and anti-viruses are turned off so your host machine won't abort the server connection.

Clear instructions for how to RECEIVE data:
Second, get the client .py file running. This will send over the full list of BBQ recipes and tips using the TCP server.

Example code from the client to get tips and recipes:

jsonFile = json.dumps(recipes)

jsonFile2 = json.dumps(tips)

sockTCP = socket(AF_INET, SOCK_STREAM)

try:

    sockTCP.connect((HOST, PORT))
    sockTCP.sendall(bytes(jsonFile, encoding="utf-8"))
    sockTCP.sendall(bytes(jsonFile2, encoding="utf-8"))

    received = sockTCP.recv(1024)
    received = received.decode("utf-8")

finally:

    sockTCP.close()

print("Sent:     {}".format(recipes))

print("Received: {}".format(received))

print("Sent:     {}".format(tips))

print("Received: {}".format(received))


![microserviceUML](https://user-images.githubusercontent.com/77512059/220736364-07e798b2-e0d5-49f0-be0a-ff250f83c8b5.png)
