
from flask import Flask, request
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Certificate Verification</h1>
    <p>Enter your Certificate ID to verify.</p>

    <form action="/verify" method="get">
        <input type="text" name="id"
               placeholder="Enter Certificate ID" required>
        <button type="submit">Verify</button>
    </form>
    """


@app.route("/verify")
def verify():
    certificate_id = request.args.get("id", "").strip().upper()

    if not certificate_id:
        return "<h2>Please enter a Certificate ID.</h2>"

    with open("students.csv", "r", encoding="utf-8") as file:
        students = csv.DictReader(file)

        for number, student in enumerate(students, start=1):

            current_id = f"CERT{number:04d}"

            if current_id == certificate_id:

                return f"""
                <h1>Certificate Verification</h1>

                <h2>Certificate Found</h2>

                <p><b>Certificate ID:</b> {current_id}</p>
                <p><b>Student Name:</b> {student["name"]}</p>
                <p><b>Course:</b> {student["course"]}</p>
                <p><b>Date:</b> {student["date"]}</p>

                <h3 style="color: green;">
                    Certificate Record Found
                </h3>
                """

    return """
    <h2 style="color: red;">
        Certificate Not Found
    </h2>
    <p>Please check the Certificate ID.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
