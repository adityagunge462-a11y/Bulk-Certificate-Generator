import shutil
import os

# Folder containing certificates
folder_name = "certificates"

# ZIP file name
zip_name = "All_Certificates"

# Create ZIP file
shutil.make_archive(
    zip_name,
    "zip",
    folder_name
)

print("All certificates added to ZIP successfully!")
print("ZIP file created:", zip_name + ".zip")