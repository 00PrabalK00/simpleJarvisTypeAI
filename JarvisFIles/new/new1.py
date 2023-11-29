import cv2

cap = cv2.VideoCapture("sample.mp4")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

path = "SlowedReversedVideo.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(path, fourcc, fps / 2, (width, height))

frame_index = total_frames - 1

while frame_index >= 0:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = cap.read()

    cv2.imshow("frame", frame)
    output.write(frame)

    k = cv2.waitKey(int(1000 / (fps / 2)))
    if k == ord("q"):
        break

    frame_index -= 1

cap.release()
output.release()
cv2.destroyAllWindows()
