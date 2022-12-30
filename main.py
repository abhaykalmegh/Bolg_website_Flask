from flask import Flask, render_template, request
from datetime import datetime
import requests
import smtplib
app = Flask(__name__)

MY_EMAIL = "abhaykalmegh@gmail.com"
MY_PASSWORD = "wzzryyieycshbvvl"

posts = requests.get('https://api.npoint.io/82616525f477bf9308d1').json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", year=year, all_post=posts)


@app.route("/about")
def about():
    return render_template("about.html", year=year)


@app.route("/contact")
def contact():
    return render_template("contact.html", year=year)


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/login', methods=['POST'])
def form_contact():
    data = request.form
    send_mail(data["name"], data["email"], data["phone"], data["message"])
    return "<h1>Successfully sent your message</h1>"


def send_mail(name, email, phone, message):
    email_message = f"Subject:New Message from pictorobo\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="sanket1111bhagat87@gmail.com",
                    msg=email_message
                )


if __name__ == "__main__":
    year = datetime.now().year
    app.run(debug=True)

    # print(data["name"])
    # print(data["email"])
    # print(data["phone"])
    # print(data["message"])
    # return "<h1>Successfully sent your message</h1>"