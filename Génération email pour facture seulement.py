import random


# Adresses d'expéditeurs
expediteurs = [
    "teamrocket794@gmail.com",
    "jonnyjohnjonju@gmail.com",
    "patricppppo@gmail.com",
    "namasse.pass@gmail.com",
    "leo.paronn@gmail.com",
    "facture0devis@gmail.com",
    "tristan.lavoue2@gmail.com",
    "emilian.volib@gmail.com",
    "moi419737@gmail.com"
]

# Sujets possibles
sujets_possibles = ["facture", "Facture", "factur", "Factur", "fature", "Fature", "facturre", "Facturre", "facturree", "Facturree", "factires", "Factires", "factrue", "Factrue", "invioce","Invice", "invioce", "Invioce", "invoice", "Invoice", "invoices", "Invoices","facturation", "Facturation", "facturaion", "Facturaion", "fcturation","Fcturation","reçu", "Reçu", "recu", "Recu", "reçue", "Reçue", "recue", "Recue", "billet","Billet", "note", "Note", "relevé", "Relevé", "releve", "Releve"]

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

# Function to generate a random email
def generate_random_email():
    message = random.choice(facture_messages)
    email = f"{message}"
    return email

# Générer les sujets et les corps des e-mails
sujets = [random.choice(sujets_possibles) for _ in range(2000)]
#messages = [f"Message {i+1}" for i in range(2000)]
emails = [generate_random_email() for _ in range(2000)]


# Générer le tableau et le fichier texte
fi = open('version_bis.csv', 'w')
for i in range(2000):
    expediteur = expediteurs[i % len(expediteurs)]
    sujet = sujets[i]
    message = emails[i]
    fi.write(str(expediteur) + ';' + str(sujet) + ';' + str(message) + '\n')
fi.close()
'''
