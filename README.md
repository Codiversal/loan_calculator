# loan_calculator
Τοκοχρεολυτικός υπολογιστής δανείου
Αυτός ο κώδικας είναι ένας υπολογιστής πληρωμής τοκοχρεολυτικού δανείου που επιτρέπει στον χρήστη να εισάγει το ποσό του δανείου, το επιτόκιο και τον αριθμό των ετών για την αποπληρωμή του δανείου και υπολογίζει τη μηνιαία δόση. Η διεπαφή χρήστη δημιουργείται με τη χρήση του Tkinter και οι υπολογισμοί γίνονται με τη χρήση της Python. Τα αποτελέσματα των υπολογισμών εμφανίζονται σε έναν πίνακα.

**Απαιτήσεις Συστήματος**
- Python 3.x
- Tkinter
- Pandas
- OS

**Πώς να το χρησιμοποιήσετε**
- Εισάγετε το ποσό του δανείου στο πεδίο "Ποσό Δανείου".
- Εισάγετε το επιτόκιο στο πεδίο "Επιτόκιο".
- Εισάγετε τον αριθμό των ετών για την αποπληρωμή του δανείου στο πεδίο "Έτη Αποπληρωμής".
- Πατήστε το κουμπί "Υπολογισμός" για να εμφανιστούν τα αποτελέσματα.
- Εάν προκύψει σφάλμα, ένα παράθυρο θα εμφανίσει ένα μήνυμα σφάλματος.

**Περιγραφές συναρτήσεων**

calculate_payment()

Αυτή η συνάρτηση εκτελεί τους υπολογισμούς για την πληρωμή του δανείου.

- Η συνάρτηση δημιουργεί πρώτα ένα κενό λεξικό για την αποθήκευση των υπολογισμένων δεδομένων.
- Το ποσό του δανείου και το επιτόκιο ανακτώνται από τη διεπαφή χρήστη και μετατρέπονται σε δεκαδικούς αριθμούς.
- Ο αριθμός των ετών για την αποπληρωμή του δανείου ανακτάται από τη διεπαφή χρήστη και μετατρέπεται σε ακέραια τιμή.
- Οι υπολογισμοί πληρωμής του δανείου εκτελούνται χρησιμοποιώντας το ποσό του δανείου, το επιτόκιο και τον αριθμό των ετών.
- Εάν προκύψει σφάλμα, εμφανίζεται ένα παράθυρο σφάλματος και ενημερώνει τον χρήστη για το λάθος.
- Τα αποτελέσματα των υπολογισμών αποθηκεύονται στο λεξικό που δημιουργήσαμε στην αρχή και μετατρέπονται σε πλαίσιο δεδομένων με την βιβλιοθήκη Pandas.
- Τα αποτελέσματα αποθηκεύονται σε ένα αρχείο excel για μελλοντική αναφορα.
- Το αρχείο excel ανοίγει αυτόματα. Σε περίπτωση που έχει μείνει ανοικτό το αρχείο excel και ο χρήστης ζητήσει εκ νέου υπολογισμό του δανείου του, τότε το excel θα κλείσει αυτόματα και θα ανοίξει ένα καινούργιο αρχείο με την καινούργια υπολογισμένη δόση. 

*Δεν αποθηκεύονται περισσότερα από ένα αρχεία excel, οπότε αν ο χρήστης θέλει να υπολογίσει και δεύτερο δάνειο και να κρατήσει και τα δυο αρχεία, θα πρέπει να κλείσει το πρώτο αρχείο excel, να μεταφέρει το αρχείο σε κάποιο άλλο φάκελο και στην συνέχεια να πατήσει "Υπολογισμός" του νέου δανείου. Με αυτό τον τρόπο ο χρήστης μπορεί να έχει όσα υπολογισμένα δάνεια θέλει.

Για να δημιουργήσετε το αρχείο .exe μπορείτε να εκτελέσετε το αρχείο install.py και μόλις ολοκληρωθεί μπείτε στον φάκελο dist. 
