import subprocess
import os
import sys

commands = ["pip install pandas", "pip install tkinter", "pip install win2com", "pip install pyinstaller"]

print("Installing...")
for command in commands:
    process = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode != 0:
        print("Failed to install: ", command)
        print("Stdout: ", process.stdout)
        print("Stderr: ", process.stderr)

print("All packages installed.\n")
print("Παρακαλώ περιμένετε μέχρι να ολοκληρωθεί η εγκατάσταση. Αυτό μπορεί να διαρκέσει μερικά λεπτά.\nTο παράθυρο θα κλείσει αυτόματα μόλις ολοκληρωθεί η εγκατάσταση.\n")
print("Μόλις ολοκληρωθεί η εγκατάσταση, ανοίξτε τον φάκελο dist που έχει δημιουργηθεί και εκεί θα βρείτε το αρχείο .exe που μπορείτε να χρησιμοποιήσετε.")
os.environ["PATH"] = os.environ["PATH"] + os.pathsep + os.path.dirname(sys.executable)

command = "pyinstaller --onefile --windowed loan_calculator.py"
process = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

