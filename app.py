from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Sebastian Cantarilho! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/greeting')
def greeting():
    return render_template('greeting.html')

@app.route('/jquery')
def jquery():
    return render_template('jquery.html')

@app.route("/favorite-course")
def favorite_course1():
    # read query parameters from URL: ?subject=ARTH&course_number=260C
    subject = request.args.get("subject", "")
    course_number = request.args.get("course_number", "")
    return render_template("favorite-course.html", subject=subject, course_number=course_number)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # read form fields
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        extra_field = request.form.get("extra_field")
        # show thank-you page with submitted values
        return render_template(
            "contact.html",
            submitted=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
            extra_field=extra_field
        )
    # show the form when GET
    return render_template("contact.html", submitted=False)



if __name__ == '__main__':
    app.run()

