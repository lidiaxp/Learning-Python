import cv2

video = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
classificadorOlhos = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

while True:
	conectado, frame = video.read()
	
	frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	facesDetectadas = classificador.detectMultiScale(frameCinza, scaleFactor=1.1, minNeighbors=9, minSize=(75,75), maxSize=(500,500))

	for(x, y, l, a) in facesDetectadas:
		cv2.rectangle(frame, (x, y), (x + l, y + a), (112, 35, 205), 2)
		regiao = frame[y : y + a, x : x + l]
		regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
		olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinzaOlho, scaleFactor=1.1, minNeighbors=9, minSize=(40,40))
		for (ox, oy, ol, oa) in olhosDetectados:
			cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

	cv2.imshow("Video", frame)
	
	if(cv2.waitKey(1) == ord('q')):
		break

video.release()
cv2.destroyAllWindows()