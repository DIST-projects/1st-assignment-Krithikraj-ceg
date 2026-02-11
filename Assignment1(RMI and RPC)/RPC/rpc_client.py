import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://135.235.193.254:8000/")

print("Addition:", proxy.add(5, 3))
print("Multiplication:", proxy.multiply(4, 6))
