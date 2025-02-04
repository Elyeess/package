import cv2
import face_recognition
import os

# Ouvrir la capture vidéo de la caméra (index 0 pour la première caméra)
cap = cv2.VideoCapture(0)

# Compteur pour le nombre de captures effectuées
capture_count = 0

# Drapeau pour indiquer si la prise de captures d'écran est activée
capture_enabled = True

while True:
    # Lire la vidéo image par image
    ret, frame = cap.read()

    # Convertir l'image de BGR en RGB (compatible avec face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Détecter les emplacements des visages dans l'image
    face_locations = face_recognition.face_locations(rgb_frame)

    # Si des visages sont détectés et la prise de captures d'écran est activée
    if face_locations and capture_enabled:
        # Prendre une capture d'écran du premier visage détecté et l'enregistrer dans un fichier
        top, right, bottom, left = face_locations[0]
        face_image = frame[top:bottom, left:right]

        # Enregistrer la capture d'écran dans le répertoire de travail actuel
        filename = f'face_screenshot_{capture_count + 1}.png'
        cv2.imwrite(filename, cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR))

        # Incrémenter le compteur de captures
        capture_count += 1

        # Désactiver la prise de captures d'écran si le nombre atteint 4
        if capture_count >= 4:
            capture_enabled = False

    # Encadrer les visages détectés avec des rectangles
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Afficher la vidéo avec les visages encadrés
    cv2.imshow('Face Detection', frame)

    # Arrêter la boucle si la touche 'q' est pressée ou si le nombre maximum de captures est atteint
    if cv2.waitKey(1) & 0xFF == ord('q') or capture_count >= 4:
        break

# Libérer la capture vidéo et fermer la fenêtre
cap.release()
cv2.destroyAllWindows()
