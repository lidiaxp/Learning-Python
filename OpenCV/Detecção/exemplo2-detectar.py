import cv2

classificadorFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
classificadorOlhos = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('pessoas/pessoas1.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificadorFace.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=9, minSize=(20,20))

for(x, y, l, a) in facesDetectadas:
	cv2.rectangle(imagem, (x, y), (x + l, y + a), (112, 35, 205), 2)
	regiao = imagem[y : y + a, x : x + l]
	regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
	olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinzaOlho, scaleFactor=1.1, minNeighbors=9)
	for (ox, oy, ol, oa) in olhosDetectados:
		cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)
	#if(len(olhosDetectados) >= 2):
	#	cv2.rectangle(imagem, (x, y), (x + l, y + a), (112, 35, 205), 2)

cv2.imshow("Faces encontradas", imagem)
cv2.waitKey()