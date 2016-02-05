# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 3, 2016

import os
from bottle import route, run, post, request
from utils import fact, integrate, roots

@route('/')
def home():
    return """
	
	<h1> Factorial </h1>
	<form action="/fact" method=post>
        <input type="text" name="Number" placeholder="Number: (required)" />
        <input type="submit" value="Submit!">
    </form>
	
	<h1> Find Roots of ax² + bx + c = 0 </h1>
	<form action="/roots" method=post>
        <input type="text" name="a" placeholder="a: (required)" />
		<input type="text" name="b" placeholder="b: (required)" />
		<input type="text" name="c" placeholder="c: (required)" />
        <input type="submit" value="Submit!">
    </form>

	<h1> Approximates a given function from lower to upper </h1>
	<form action="/intg" method=post>
        <input type="text" name="func" placeholder="function: (required)" />
		<input type="text" name="Lower" placeholder="lower: (required)" />
		<input type="text" name="Upper" placeholder="upper: (required)" />
        <input type="submit" value="Submit!">
    </form>

	"""

@post("/fact")
def factorial_page():
	decoded = request.forms.decode("utf-8")
	print(decoded)
	try:
		number = int(decoded.get("Number"))
	except ValueError:
		return "<h1> Please enter a <strong>valid</strong> number</h1>"

	try:
		result = fact(number)
	except ValueError:
		result = None

	return "The factorial of {} is {}".format(number, result)

@post("/roots")
def roots_page():
	decoded = request.forms.decode("utf-8")

	try:
		a = int(decoded.get("a"))
		b = int(decoded.get("b"))
		c = int(decoded.get("c"))
	except ValueError:
		return "<h1> Please enter a <strong>valid</strong> number</h1>"

	return "The root(s) of {}x² + {}x + {} = 0 is/are {}".format(a,b,c, roots(a,b,c))

@post("/intg")
def intg_page():
	decoded = request.forms.decode("utf-8")

	try:
		a = int(decoded.get("Lower"))
		b = int(decoded.get("Upper"))
	except ValueError:
		return "<h1> Please enter a <strong>valid</strong> Lower/Upper boundary</h1>"

	function = decoded.get("func")
	return "The approximation of {} from {} to {} is {}".format(function, a, b, round(integrate(function, a, b), 4))

run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))