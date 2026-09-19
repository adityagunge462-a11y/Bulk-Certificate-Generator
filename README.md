
# Bulk Certificate Generator

A Python-based application that generates certificates in bulk from a CSV file and provides certificate verification using unique Certificate IDs.

## Features

- Generate multiple certificates from CSV data
- Create PDF certificates
- Generate QR codes for certificate verification
- Verify certificates using unique Certificate IDs
- Create ZIP files containing generated certificates
- Simple graphical user interface

## Technologies Used

- Python
- Tkinter
- Flask
- ReportLab
- CSV
- QR Code

## Project Structure

```text
Bulk_Certificate_Generator/
│
├── certificates/
│   └── app.py
├── gui.py
├── main.py
├── students.csv
├── zip_certificates.py
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/adityagunge462-a11y/Bulk-Certificate-Generator.git
```

### 2. Open Project Folder

```bash
cd Bulk-Certificate-Generator
```

### 3. Install Dependencies

```bash
pip install reportlab qrcode[pil] flask
```

### 4. Run Certificate Generator

```bash
python main.py
```

### 5. Run Certificate Verification

```bash
python certificates/app.py
```

Open the browser and visit:

```text
http://127.0.0.1:5000
```

## Certificate Verification

Enter a valid Certificate ID to verify the certificate details.

Example:

```text
CERT0001
```

## Future Scope

- Online certificate management
- Database integration
- User authentication
- Cloud deployment
- Improved certificate templates

## Author

Aditya Gunge

B.Tech CSE (AI & ML)

Rai Technology University
