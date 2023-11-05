from flask import Flask, render_template, jsonify

# Creating a WSGI application (Python web application)
app = Flask(__name__)

Education = [
  {
    'id': 1,
    'school': '電気通信大学',
    'department': 'I類　情報系',
    'major': 'コンピュータサイエンス',
    'degree': '学士',
    'year': '2024年'
  },
  {
    'id': 2,
    'school': '鶴岡工業高等専門学校',
    'department': '創造工学科',
    'major': '電気電子コース',
    'degree': '準学士',
    'year': '2022年'
  },
  {
    'id': 3,
    'school': 'SANT SECONDARY SCHOOL',
    'department': '理系',
    'degree': '高校卒業',
    'year': '2017年'
  }
]

Internship = [
  {
    'id': 1,
    'company': '日本コンピューター開発株式会社',
    'position': 'ウエッブサイトデベロッパー',
    'date': '2020年8月', 
    'duration': '5日間'
  },
  {
    'id': 2,
    'company': 'コスモリサーチ株式会社',
    'position': 'SDRソフトウェア開発',
    'date': '2020年9月', 
    'duration': '5日間'
  },
  {
    'id': 3,
    'company': 'ZeeVaa Communications 株式会社',
    'position': 'ソフトウェア開発企業のコンサルティング',
    'date': '2023年3月', 
    'duration': '5日間'
  },
]

# Creating a route for the home page
@app.route("/")
# Using the render_template function to render the home page
def hello_world():
  return render_template("home.html",
                        education=Education,
                        internship=Internship)

# Listing the education and internship items as JSON
@app.route("/api/education")
def list_education():
  return jsonify(Education)

@app.route("/api/internship")
def list_internship():
  return jsonify(Internship)
  
# Letting the app run without changing the replit file
# Port 8080 typically used for web servers
# Host 0.0.0.0 allows connections from anywhere, anyone
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
