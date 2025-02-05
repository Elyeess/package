import cv2
import numpy as np
import matplotlib.pyplot as plt

# Chemin vers l'image
image_path = 'second.png'  #  chemin de votre image

# Lire l'image et la convertir en niveaux de gris
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un flou gaussien et un seuillage adaptatif
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 45, 15)

# Effectuer l'analyse des composants connectés
_, labels = cv2.connectedComponents(thresh)
mask = np.zeros(thresh.shape, dtype="uint8")

# Définir les critères pour filtrer les caractères
total_pixels = image.shape[0] * image.shape[1]
lower = total_pixels // 70
upper = total_pixels // 20

# Boucle sur les composants uniques
for (i, label) in enumerate(np.unique(labels)):
    if label == 0:
        continue

    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    numPixels = cv2.countNonZero(labelMask)

    if numPixels > lower and numPixels < upper:
        mask = cv2.add(mask, labelMask)

# Trouver les contours et dessiner les boîtes englobantes
cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image.copy()
cv2.drawContours(contour_image, cnts, -1, (0, 255, 0), 2)

# Afficher les résultats
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title("Image Originale")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Image Seuillée")
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Contours des Caractères")
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
