import cv2
img =cv2.imread("thug_duck.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,250)
images= cv2.hconcat([edges])
cv2.imshow("output",images)
cv2.waitKey()



