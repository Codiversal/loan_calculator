#Κάνουμε import τις απαιτούμενες βιβλιοθήκες
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from pathlib import Path


def calculate_payment():
    try:
        # Δημιουργούμε ένα άδειο λεξικό για να αποθηκεύσουμε τα υπολογισμένα δεδομένα
        data = {"Έτη Αποπληρωμής": [], "Τοκοχρεολύσιο": [], "Τόκος": [], "Χρεολύσιο": [], "Υπόλοιπο Δανείου": [], "Μηνιαία Δόση": []}
        # Διαμορφώνουμε την τιμή που θα δώσει ο χρήστης για το ποσό του δανείου
        if "." in poso_daneiou_entry.get():
            poso_daneiou_string = (poso_daneiou_entry.get()).replace(".","")
            if "," in poso_daneiou_entry.get():
                poso_daneiou_string = poso_daneiou_string.replace(",", ".")
        elif "," in poso_daneiou_entry.get():
            poso_daneiou_string = (poso_daneiou_entry.get()).replace(",", ".")
        else:
            poso_daneiou_string = poso_daneiou_entry.get()
        # Διαμορφώνουμε την τιμή που θα δώσει ο χρήστης για το επιτόκιο
        epitokio_string = (epitokio_entry.get()).replace(",", ".")
        #Μετατρέπουμε τις συμβολοσειρές σε δεκαδικούς αριθμούς
        poso_daneiou = float(poso_daneiou_string)
        epitokio = float(epitokio_string) / 100
        #Παίρνουμε την συμβολοσειρά για τα έτη αποπληρωμής και την μετατρέπουμε σε ακέραιο
        eti_apopliromis = int(eti_apopliromis_entry.get())
    except:
        #Σε περίπτωση που ο χρήστης βάλει σύμβολα ή κείμενο θα εμφανίζεται ένα παράθυρο σφάλματος
        messagebox.showerror("Σφάλμα", "Έχει προκύψει ένα σφάλμα. Μην χρησιμοποιείτε κείμενο και σύμβολα για την σωστή λειτουργία του προγράμματος!")

    #Υπολογίζουμε το ετήσιο τοκοχρεολύσιο
    tokoxreolisio = poso_daneiou * epitokio / (1 - (1 + epitokio)**(-eti_apopliromis))
    #Ξεκινάμε μια μεταβλητή για να υπολογίσουμε στην συνέχεια το συνολικό ποσό που θα πληρώσουμε στην τράπεζα για το δάνειο που ζητάμε
    synoliko_poso_pliromis = 0
    #Δημιουργούμε μια συνάρτηση για να μετατρέψουμε τους αριθμούς σε κείμενο που θα εμφανίζει το σύμβολο του ευρώ(€)
    def number_to_euro(number):
        return f"{number:.2f}€"
    #Δημιουργούμε ένα βρόχο επανάληψης μέχρι το πέρας των ετών του δανείου
    while eti_apopliromis > 0:
        #Προσθέτουμε τις τιμές στην λίστα του λεξικού
        data["Έτη Αποπληρωμής"].append(eti_apopliromis)
        data["Τοκοχρεολύσιο"].append(number_to_euro(tokoxreolisio))
        tokos = poso_daneiou * epitokio
        data["Τόκος"].append(number_to_euro(tokos))
        xreolisio = tokoxreolisio - tokos
        data["Χρεολύσιο"].append(number_to_euro(xreolisio))
        poso_daneiou -= xreolisio
        data["Υπόλοιπο Δανείου"].append(number_to_euro(poso_daneiou))
        eti_apopliromis -= 1
        data["Μηνιαία Δόση"].append(number_to_euro(tokoxreolisio/12))
        synoliko_poso_pliromis += tokoxreolisio
    #Μετατρέπουμε τα δεδομένα μας σε πλαίσιο δεδομένων με την χρήση της βιβλιοθήκης Pandas
    df = pd.DataFrame(data)
    #Προσθέτουμε στην τελευταία σειρά το συνολικό ποσό που θα πληρώσουμε στην τράπεζα
    df.at[(len(df)+1), "Έτη Αποπληρωμής" ] = "Συνολική Πληρωμή"
    df.at[(len(df)), "Τοκοχρεολύσιο"] = number_to_euro(synoliko_poso_pliromis) 
    #Δοκιμάζουμε να εξάγουμε το πλαίσιο δεδομένων σε αρχείο excel
    try:
        #Παίρνουμε την διαδρομή για την επιφάνεια εργασίας του χρήστη
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        #Καθορίζουμε τη διαδρομή του αρχείου χρησιμοποιώντας τη διαδρομή της επιφάνειας εργασίας και το επιθυμητό όνομα αρχείου.
        file_path = Path(desktop) / "Υπολογισμός Δανείου.xlsx"
        #Αποθηκεύουμε τα δεδομένα σε αρχείο excel
        df.to_excel(file_path, index = False)
        minima_label.config(text = f"Μηνιαία Δόση Δανείου: {number_to_euro(tokoxreolisio/12)}€")
        #Ανοίγουμε το αρχείο excel
        os.startfile(file_path)
    #Σε περίπτωση που έχουμε ήδη ανοιχτό το αρχείο excel, τότε θα κλείσει και θα τρέξει εκ νέου με τα νέα δεδομένα
    except:
        import win32com.client
        #Παίρνουμε την διαδρομή για την επιφάνεια εργασίας του χρήστη
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        #Καθορίζουμε τη διαδρομή του αρχείου χρησιμοποιώντας τη διαδρομή της επιφάνειας εργασίας και το επιθυμητό όνομα αρχείου.
        file_path = os.path.abspath(desktop+"/Υπολογισμός Δανείου.xlsx")
        excel = win32com.client.GetObject(file_path)
        #Κλείνουμε το ήδη ανοικτό αρχείο excel
        excel.Close(SaveChanges=0)
        #Αποθηκεύουμε τα δεδομένα στο αρχείο excel
        df.to_excel(file_path, index = False)
        minima_label.config(text = f"Μηνιαία Δόση Δανείου: {number_to_euro(tokoxreolisio/12)}€")
        #Ανοίγουμε το αρχείο excel
        os.startfile(file_path)
#Δημιουργούμε το παράθυρο με την βοήθεια της βιβλιοθήκης tkinter         
root = tk.Tk()
#Δίνουμε τον τίτλο του παραθύρου
root.title("Υπολογιστής Δανείου")

#Δημιουργούμε την ετικέτα και το πεδίο εγγραφής του Ποσού του δανείου που θα δώσει ο χρήστης
poso_daneiou_label = tk.Label(root, text="Ποσό Δανείου")
poso_daneiou_label.grid(row=0, column=0)

poso_daneiou_entry = tk.Entry(root)
poso_daneiou_entry.grid(row=0, column=2)
#Όταν ανοίγει το πρόγραμμα ο κέρσορας θα ξεκινάει από το ποσό του δανείου
poso_daneiou_entry.focus_set()

#Δημιουργούμε την ετικέτα και το πεδίο εγγραφής για το επιτόκιο του δανείου που θα δώσει ο χρήστης
epitokio_label = tk.Label(root, text="Επιτόκιο (%)")
epitokio_label.grid(row=1, column=0)

epitokio_entry = tk.Entry(root)
epitokio_entry.grid(row=1, column=2)

#Δημιουργούμε την ετικέτα και το πεδίο εγγραφής τα έτη αποπληρωμής του δανείου
eti_apopliromis_label = tk.Label(root, text="Έτη αποπληρωμής")
eti_apopliromis_label.grid(row=2, column=0)

eti_apopliromis_entry = tk.Entry(root)
eti_apopliromis_entry.grid(row=2, column=2)

#Δημιουργούμε μία κενή στήλη για να γίνει πιο κατανεμημένη η εμφάνιση του προγράμματος.
just_a_gap = tk.Label(root, text="\t")
just_a_gap.grid(row=0, column = 1)

#Δημιουργούμε το κουμπί που θα υπολογίσει το ποσό του δανείου και θα κάνει εξαγωγή του αρχείου excel 
ypologismos_button = tk.Button(root, text="Υπολογισμός", command=calculate_payment)
ypologismos_button.grid(row=3, column=0, columnspan=3, pady=10)

#Δημιουργούμε μία ετικέτα που θα ενημερώσουμε για να εμφανιστεί στον χρήστη η μηνιαία δόση του δανείου του 
minima_label = tk.Label(root, text="")
minima_label.grid(row=4, column=0, columnspan=3)

#Διαμορφώνουμε το παράθυρο στις διαστάσεις που επιθυμούμε
root.geometry("310x140")
root.resizable(False, False)
root.attributes("-topmost", True)
root.focus_force()
root.mainloop()
