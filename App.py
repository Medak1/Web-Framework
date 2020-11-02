import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 80))

s.listen(5)
print(f"listening at 80")
while True:
	c,adrs = s.accept()
	print(f"Connected to {adrs}")
	request = "".encode("utf-8")
	while True:
		a = c.recv(1024)
		request+=a
		if a[len(a)-4:len(a)] == "\r\n\r\n".encode("utf-8"):
			print("End of request")
			break
	request_lst_global = request.split("\r".encode("utf-8"))
	request_lst = request_lst_global[0].split()
	method = request_lst[0]
	print(method)
	route = request_lst[1]
	print(route)
	https_version = request_lst[2]
	print(https_version)
	c.send("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The fucking title</title>
</head>
<body>

<h1>The fucking title</h1>
<hr>
<p>My paragraph</p>
<img src="https://www.gravatar.com/avatar/f85efc388ebd6e216e7ab82dac1dc595?s=48&d=identicon&r=PG&f=1">
</body>
</html>""".encode())