# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Dockerized Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
