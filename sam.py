import cv2
import numpy as np
import matplotlib.pyplot as plt

# Chemin vers l'image
image_path = '/path/to/your/image.jpg'  # Remplacez par le chemin de votre image

# Lire l'image et la convertir en niveaux de gris
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un flou gaussien pour réduire le bruit
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Utiliser un seuillage adaptatif pour une binarisation efficace
thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Trouver les contours dans l'image seuillée
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrer les contours pour ne garder que ceux qui ont une forme rectangulaire
rectangles = []
for c in contours:
    # Approximer le contour à une forme polygone
    epsilon = 0.02 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    # Si le polygone a 4 côtés, il est probablement un rectangle
    if len(approx) == 4:
        rectangles.append(approx)

# Dessiner les rectangles trouvés sur l'image originale
output_image = image.copy()
cv2.drawContours(output_image, rectangles, -1, (0, 255, 0), 2)

# Afficher les résultats
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Image Seuillée")
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Contours des Plaques")
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
