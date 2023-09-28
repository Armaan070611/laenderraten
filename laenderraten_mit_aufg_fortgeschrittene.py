"""
Challenge: Länderraten
======================
"""

# Erstelle eine Liste mit Hauptstädten
import random

Hauptstaedte =["Kabul" , "Kairo" , "Tirana" , "Algier" , "Andorra La Vella"]

# Erstelle eine Liste mit Ländern
laender =["Afghanistan" , "Aegypten" , "Albanien" , "Algerien" , "Andorra"]
# Erzeuge eine Zufallszahl, die im Bereich aller möglichen Indexe der Liste liegt.
zufall = random.randint(0, 4)

# Gib die Hauptstadt aus, die an der Stelle der Zufallszahl steht.
idx = Hauptstaedte[zufall]
print(idx)
print(zufall)
# Frage den Benutzer nach dem Land, das zu der Hauptstadt gehört.
Stadt = input("Welches Land gehört zu der Hauptstadt " + (Hauptstaedte[zufall]) + "?")


# Vergleiche die Eingabe des Benutzers mit dem Land, das zu der Hauptstadt gehört.

laender_idx = laender.index(Stadt)



# Gib eine entsprechende Meldung aus, ob die Hauptstadt erraten wurde oder nicht.
if laender_idx != zufall:

    print("Falsch du netter mensch")

else:

    print("Richtig")



# Erweiterung 1:
# ============
# Erweitere das Programm so, dass der Benutzer so lange raten kann, bis er das Land erraten hat.

# Erweiterung 2:
# ============
# Nutze die Datei 'laender-hauptstaedte.csv' (eine Liste mit allen Ländern und Hauptstädten der Welt) und bereite die Daten so auf, dass du aus den Daten jeweils eine Liste mit Ländern und eine Liste mit Hauptstädten erzeugst.

# Erweiterung 3:
# ============
# Erweitere das Programm so, dass die Länder und Hauptstädte, die richtig geraten wurden, aus den Listen genommen werden, damit sie nicht noch einmal abgefragt werden.

# Erweiterung 4:
# ============
# Erweitere das Programm so, dass der Benutzer die Anzahl der Länder bestimmen kann, die er erraten möchte.

# Erweiterung 5:
# ============
# Differenziere zwischen Kontinenten und lasse den Benutzer entscheiden, aus welchem Kontinent er Länder erraten möchte.
