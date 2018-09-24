import cv2

img = cv2.imread('IMG-20180408-WA0036.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'Hacklab Ghana 2018', (10, 200), font, 4, (255, 0, 0), 2, cv2.LINE_AA)

cv2.putText(img, '2018', (10,500), font, 4, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('Meme', img)

cv2.waitKey(0)

cv2.destroyAllWindows() 
