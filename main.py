import csv
import os
import qrcode
import sys

from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors


# Output folder
output_folder = "certificates"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Open CSV file
csv_file = sys.argv[1] if len(sys.argv) > 1 else "students.csv"

with open(csv_file, "r", encoding="utf-8") as file:

    students = csv.DictReader(file)

    # Read each student
    for number, student in enumerate(students, start=1):

        name = student["name"]
        course = student["course"]
        date = student["date"]

        # Unique certificate ID
        certificate_id = f"CERT{number:04d}"

        # QR verification link
        qr_data = (
            f"http://10.96.87.15:5000/verify?id={certificate_id}"
        )

        # Generate QR code
        qr = qrcode.make(qr_data)

        qr_file = f"qr_{certificate_id}.png"
        qr.save(qr_file)

        # PDF file path
        pdf_file = os.path.join(
            output_folder,
            f"{name}_Certificate.pdf"
        )

        # Create landscape A4 PDF
        pdf = canvas.Canvas(
            pdf_file,
            pagesize=landscape(A4)
        )

        width, height = landscape(A4)

        # Background
        pdf.setFillColor(colors.white)
        pdf.rect(
            0, 0, width, height,
            fill=1,
            stroke=0
        )

        # Outer golden border
        pdf.setStrokeColor(
            colors.HexColor("#B8860B")
        )
        pdf.setLineWidth(5)

        pdf.rect(
            25, 25,
            width - 50,
            height - 50
        )

        # Inner blue border
        pdf.setStrokeColor(
            colors.HexColor("#1F3A5F")
        )
        pdf.setLineWidth(2)

        pdf.rect(
            38, 38,
            width - 76,
            height - 76
        )

        # Main title
        pdf.setFillColor(
            colors.HexColor("#1F3A5F")
        )
        pdf.setFont(
            "Helvetica-Bold",
            30
        )

        pdf.drawCentredString(
            width / 2,
            height - 115,
            "CERTIFICATE OF PARTICIPATION"
        )

        # Subtitle
        pdf.setFillColor(colors.black)
        pdf.setFont(
            "Helvetica",
            16
        )

        pdf.drawCentredString(
            width / 2,
            height - 165,
            "This certificate is proudly presented to"
        )

        # Student name
        pdf.setFillColor(
            colors.HexColor("#B8860B")
        )
        pdf.setFont(
            "Helvetica-Bold",
            32
        )

        pdf.drawCentredString(
            width / 2,
            height - 225,
            name
        )

        # Underline
        pdf.setStrokeColor(
            colors.HexColor("#B8860B")
        )
        pdf.setLineWidth(1)

        pdf.line(
            width / 2 - 150,
            height - 240,
            width / 2 + 150,
            height - 240
        )

        # Course details
        pdf.setFillColor(colors.black)
        pdf.setFont(
            "Helvetica",
            16
        )

        pdf.drawCentredString(
            width / 2,
            height - 285,
            f"For successfully participating in {course}"
        )

        # Date
        pdf.setFont(
            "Helvetica",
            13
        )

        pdf.drawCentredString(
            width / 2,
            height - 325,
            f"Date: {date}"
        )

        # Certificate ID
        pdf.setFont(
            "Helvetica",
            11
        )

        pdf.drawString(
            55,
            55,
            f"Certificate ID: {certificate_id}"
        )

        # QR code
        pdf.drawImage(
            qr_file,
            width - 150,
            55,
            width=90,
            height=90
        )

        # QR label
        pdf.setFont(
            "Helvetica",
            8
        )

        pdf.drawCentredString(
            width - 105,
            45,
            "Scan to Verify"
        )

        # Save PDF
        pdf.save()

        # Remove temporary QR image
        os.remove(qr_file)

        print(
            f"Certificate generated for {name} "
            f"({certificate_id})"
        )


print("All certificates generated successfully!")