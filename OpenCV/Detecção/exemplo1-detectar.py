import cv2

classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('pessoas/pessoas2.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=9, minSize=(20,20))
print(len(facesDetectadas), "faces detectadas")

for(x, y, l, a) in facesDetectadas:
	cv2.rectangle(imagem, (x, y), (x + l, y + a), (112, 35, 205), 2)

cv2.imshow("Faces encontradas", imagem)
cv2.waitKey()