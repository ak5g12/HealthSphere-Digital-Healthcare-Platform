from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")
        return render_template("confirm.html", name=name, date=date)
    return render_template("appointment.html")

@app.route("/doctors")
def doctors():
    return render_template("doctors.html")

@app.route("/patient_register")
def patient_register():
    return render_template("patient_register.html")

@app.route("/save_appointment", methods=["POST"])
def save_appointment():
    name = request.form.get("name")
    email = request.form.get("email")
    doctor = request.form.get("doctor")
    date = request.form.get("date")
    time = request.form.get("time")

    with open("appointments.txt", "a") as f:
        f.write(f"Name: {name}, Email: {email}, Doctor: {doctor}, Date: {date}, Time: {time}\n")

    return "Appointment Saved ✅"

@app.route("/save_login", methods=["POST"])
def save_login():
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")

    secure_password = generate_password_hash(password)

    with open("logins.txt", "a") as f:
        f.write(f"Username: {username}, Password: {secure_password}, Role: {role}\n")

    return "Login Data Saved ✅"

@app.route("/save_patient", methods=["POST"])
def save_patient():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    age = request.form.get("age")
    gender = request.form.get("gender")
    address = request.form.get("address")

    with open("patients.txt", "a") as f:
        f.write(f"{name},{email},{phone},{age},{gender},{address}\n")

    return "Patient Registered Successfully ✅"

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

@app.route("/pharmacy")
def pharmacy():
    return render_template("pharmacy.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)