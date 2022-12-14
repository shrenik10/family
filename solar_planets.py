import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun", 
            (100,80), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "mercury", 
            (110,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "venus", 
            (210,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "earth", 
            (310,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "mars", 
            (410,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "jupiters", 
            (510,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "saturn", 
            (710,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "uranus", 
            (910,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
cv2.putText(img,
            "neptune", 
            (1110,180), 
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255,255,255)
            )
            
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("solarsystemwithnames.jpg",img)