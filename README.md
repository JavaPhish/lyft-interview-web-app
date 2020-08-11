<h1> Basic POST JSON web application</h1>
<txt>This is a basic web server that handles a JSON post request formatted like this {'string_to_cut':'example string'}
it returns a JSON string formatted like this {'return_string':'asdasd'}
The web server returns the original string but only every third letter</txt>

<h4>Example</h4>
terminal post request: curl -X POST https://127.0.0.1:5001/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
Output $:{"return_string": "muydv"}


Check out the code for in depth documentation :)

<h4>Stack</h4>
<li>Python</li>
<li>Flask</li>
<li>JSON</li>

-Carter Clements
