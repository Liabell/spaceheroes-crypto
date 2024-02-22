import string
import random
import sys

from flask import Flask, send_file

app = Flask(__name__)

# Define the combined_array and shifted_array
combined_array = list(string.ascii_letters + string.digits)
shifted_array = combined_array[:]
random.shuffle(shifted_array)

# Encrypt plaintext.txt and store in encrypted.txt
def encrypt_plain():
    with open('plaintext.txt', 'r') as file, open('encrypted.txt', 'w') as out:
        for line in file:
            for char in line:
                shifted_char = shifted_array[combined_array.index(char)] if char in combined_array else char
                out.write(shifted_char)

@app.route('/spaceheroes-crypto/')  # Adjusted route path
def index():
    encrypt_plain()  # Call the encryption function
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Encrypted Text</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #3b3a3a;
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh; /* Ensure the body takes up the full viewport height */
        }
        .container {
            max-width: 900px; /* Adjust max-width as needed */
            width: 90%; /* Ensure the container takes up 90% of the available width */
            background-color: #ededed;
            padding: 40px; /* Increase padding */
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            background-image: linear-gradient(to right, #7300ff 2%, #00fbff 98%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        p {
            color: black;
        }
        a {
            background: linear-gradient(to left, 
            violet, indigo, blue, green, yellow, orange, red);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-decoration: underline;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Alien Movie Time</h1>
        <p>I was partaking in a fun viewing of something with my alien bros but couldn't understand anything due to the language difference.</p>
        <p>I've managed to download a copy of what was said during the viewing but it's come across as encrypted, can you help me decrypt it?</p>
        <p><b>EbopBeeops Translated to Human Readable Markings: <a href="/spaceheroes-crypto/download">download</a></b></p> <!-- Adjusted href -->
    </div>
</body>
</html>
'''

@app.route('/spaceheroes-crypto/download')  # Adjusted route path
def download_file():
    return send_file('encrypted.txt', as_attachment=True)

if __name__ == '__main__':
    ip = '0.0.0.0'  # Host on all available network interfaces
    port = 5000  # Default port
    app.run(debug=True, host=ip, port=port)
