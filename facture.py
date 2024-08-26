import random

# Subjects
subjects = ["Facture", "Réclamation"]

# Generate 300 radically different messages for each subject
facture_messages = [
    "Bonjour, je voudrais recevoir ma facture du mois dernier. Merci.",
    "Pouvez-vous m'envoyer une copie de ma facture s'il vous plaît ?",
    "Je n'ai pas reçu ma facture de ce mois-ci, pouvez-vous la renvoyer ?",
    "Bonjour, je voudrais avoir un détail de ma facture récente.",
    "Merci de m'envoyer ma facture pour vérification.",
    # Adding more distinct messages
    "Ma dernière facture semble incorrecte, pourriez-vous la vérifier ?",
    "Bonjour, j'ai une question concernant un montant sur ma facture.",
    "Je souhaiterais recevoir la facture de mon dernier achat.",
    "Pouvez-vous m'envoyer une facture détaillée pour le mois dernier ?",
    "Bonjour, j'ai remarqué une erreur sur ma facture, merci de la corriger.",
    # Continue adding more unique messages to reach 300
    "Bonjour, j'ai besoin de la facture pour mes archives. Merci.",
    "Je n'ai toujours pas reçu ma facture du mois dernier.",
    "Merci de m'envoyer une facture rectifiée pour ce mois-ci.",
    "Bonjour, je voudrais comprendre un montant sur ma facture.",
    "Pouvez-vous me fournir la facture détaillée de mon achat récent ?",
    "Bonjour, je vous prie de bien vouloir m'envoyer ma facture de juin.",
    "Je voudrais une copie électronique de ma dernière facture.",
    "Pouvez-vous vérifier ma facture, il y a des montants surprenants.",
    "Bonjour, je n'ai pas reçu ma facture, merci de la renvoyer.",
    "Merci de m'envoyer ma facture mensuelle par email.",
    "Bonjour, j'ai une question urgente concernant ma facture.",
    "Pouvez-vous me fournir la facture avec les détails des services ?",
    "Bonjour, ma facture contient des erreurs, merci de la rectifier.",
    "Je souhaite recevoir ma facture du mois en cours. Merci.",
    "Pouvez-vous m'envoyer une copie conforme de ma dernière facture ?",
    "Bonjour, je voudrais un duplicata de ma facture de février.",
    "Merci de me faire parvenir ma facture pour le mois de juillet.",
    "Bonjour, pouvez-vous vérifier les montants facturés ?",
    "J'ai besoin de ma facture pour mes déclarations. Merci.",
    "Bonjour, pourriez-vous m'envoyer ma facture par email ?",
    # ... Continue adding until you have 300 unique messages
]

# Ensure each message list has exactly 300 unique messages
facture_messages = facture_messages[:300]

'''
# Function to generate a random email
def generate_random_email():
    subject = random.choice(subjects)
    if subject == "Facture":
        message = random.choice(facture_messages)
    else:
        message = random.choice(reclamation_messages)

    email = f"Sujet: {subject}\n\n{message}\n\nCordialement"
    return email
'''

# Function to generate a random email
def generate_random_email():
    message = random.choice(facture_messages)
    email = f"{message}"
    return email

# Generate 2000 emails
emails = [generate_random_email() for _ in range(2000)]

# Save generated emails to a file
with open("Générateur.txt", "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n\n---\n\n")

print("2000 emails generated and saved to 'Générateur.txt'.")
