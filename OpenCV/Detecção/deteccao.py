import cv2

imagem = cv2.imread('opencv-python.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", imagem)
cv2.imshow("Cinza", imagemCinza)
cv2.waitKey() #quando aperta uma tecla fecha