from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="SqL#@123",
    database="mywebsite"
)


@app.route("/")
def home():
    return render_template("signup.html")


@app.route("/register", methods=["POST"])
def register():

    username = request.form.get("username")
    mobilenumber = request.form.get("mobilenumber")
    email = request.form.get("email")
    password = request.form.get("password")
    confirmpassword = request.form.get("confirmpassword")
    membership = request.form.get("browser")
    terms = request.form.get("checkbox")

    # Check password
    if password != confirmpassword:
        return "Passwords do not match!"

    # Check Terms & Conditions
    if not terms:
        return "Please accept Terms & Conditions."

    cursor = mydb.cursor()

    sql = """
        INSERT INTO users
        (name, email, password, mobilenumber, membership)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        username,
        email,
        password,
        mobilenumber,
        membership
    )

    try:
        cursor.execute(sql, values)
        mydb.commit()

        return "Registration successful!"

    except mysql.connector.Error as err:
        return f"Database error: {err}"

    finally:
        cursor.close()


if __name__ == "__main__":
    app.run(debug=True)