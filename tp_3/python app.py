import cv2

image = cv2.imread("renard.png")

if image is not None:

    petite = cv2.resize(image,(400,300))

    cv2.imshow("originale",image)
    cv2.imshow("redimensionnee",petite)
    cv2.waitkey(0)
    cv2.destroyAllwindows()