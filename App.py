import socket
import email
from email.policy import HTTP

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ("0.0.0.0", 80) )


def parse_request(request):
	a = email.message_from_string( request.decode(), policy=HTTP )
	request = str( a ).split( "\r\n" )
	return from_mail_to_dict( request )


def from_mail_to_dict(lst):
	http_dict = {}
	for i in lst:
		if i == "":
			continue
		if not ":" in i:
			temp_var = i.split()
			http_dict["http-method"] = temp_var[0]
			http_dict["route"] = temp_var[1]
			http_dict["http-version"] = temp_var[2]
			continue
		temp_list = i.split( ":" )
		http_dict[temp_list[0]] = temp_list[1]
	return http_dict


s.listen( 5 )
print( f"listening at 80" )
while True:
	c, adrs = s.accept()
	print( f"Connected to {adrs}" )
	request = "".encode( "utf-8" )
	while True:
		a = c.recv( 1024 )
		request += a
		if a[len( a ) - 4:len( a )] == "\r\n\r\n".encode( "utf-8" ):
			break
	request = parse_request(request)
	c.send( """<!DOCTYPE html>
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
</html>""".encode() )
