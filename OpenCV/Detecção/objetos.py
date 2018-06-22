import cv2

#classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalcatface.xml')
#classificador = cv2.CascadeClassifier('haarcascades/relogios.xml')
#classificador = cv2.CascadeClassifier('haarcascades/cars.xml')
classificador = cv2.CascadeClassifier('haarcascades/banana-classifier.xml')

imagem = cv2.imread('pessoas/banana1.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

detectado = classificador.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=5)

for(x, y, l, a) in detectado:
	cv2.rectangle(imagem, (x, y), (x + l, y + a), (112, 35, 205), 2)

cv2.imshow("Gatos Encontrados", imagem)
cv2.waitKey()