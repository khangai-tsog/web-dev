from flask import Flask

# Creating a WSGI application (Python web application)
app = Flask(__name__)


# Creating a route for the home page
@app.route("/")
def hello_world():
  return "Hello, world"


# Letting the app run without changing the replit file
# Port 8080 typically used for web servers
# Host 0.0.0.0 allows connections from anywhere, anyone
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
