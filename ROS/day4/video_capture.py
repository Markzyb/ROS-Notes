import numpy as np
import cv2



cap = cv2. VideoCapture (0)

while(True):

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	temp = np.rot90(frame)
	 #rotate 90 degrees,RGB




	cv2.imshow('frame',temp)
	

	if cv2.waitKey(1)& 0xFF == ord('q'):
		break

cap.release()
cv.destroyALLWindows()
