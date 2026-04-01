import cv2
import os
import time

# --- SETTINGS ---
CHESSBOARD_SIZE = (10, 7)
SAVE_PATH = "calib_images"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("--- AUTO-CAPTURE MODE ---")
print("Move the board slowly. Script will save every 2 seconds if lines appear.")
print("Press 'Q' to stop when you have 20+ images.")

last_save_time = time.time()
count = 0

while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret_corners, corners = cv2.findChessboardCorners(gray, CHESSBOARD_SIZE, None)

    display_frame = frame.copy()
    if ret_corners:
        cv2.drawChessboardCorners(display_frame, CHESSBOARD_SIZE, corners, ret_corners)
        
        # Check if 2 seconds have passed since the last save
        if time.time() - last_save_time > 2.0:
            filename = os.path.join(SAVE_PATH, f"auto_img_{count:02d}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Auto-Saved Image {count:02d}")
            count += 1
            last_save_time = time.time()

    cv2.imshow("Auto-Calibration", display_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
