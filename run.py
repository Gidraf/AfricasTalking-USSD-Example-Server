from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def printPhoneNumber():
    text = request.values.get("text")
    phone = request.values.get("phoneNumber")

# TODO: check if phone exists

    if (text == ""):
        return "CON please enter your ID number \n"

    #Todo check if the id number exissts

    if (text != ""):
        return """CON Please select service \n
        1.\t Appy for loan \n
        2.\t Check Loan Status \n
        3.\t Exit"""


if __name__ == "__main__":
    app.run(debug=True)
