import cv2

# Define function to track using Lucas-Kanade optical flow
def track_point(frame, prev_gray, prev_pt):
  # Convert frame to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # Parameters for Lucas-Kanade optical flow
  lk_params = dict(winSize=(15, 15), 
                   maxLevel=2,
                   criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
  
  # Track the point
  pt, status, err = cv2.calcOpticalFlowPyLK(prev_gray, gray, prev_pt, None, **lk_params)
  
  # Check for successful tracking
  if status[0] == 1:
    return pt[0]
  else:
    return None

# Open video capture
cap = cv2.VideoCapture("path/to/your/video.mp4")

# Check if video opened successfully
if not cap.isOpened():
  print("Error opening video")
  exit()

# Get the first frame
ret, frame = cap.read()

# Select the point to track (using mouse click)
def select_point(event, x, y, flags, param):
  global tracking_point
  if event == cv2.EVENT_LBUTTONDOWN:
    tracking_point = (x, y)
    cv2.circle(frame, tracking_point, 5, (0, 255, 0), -1)

cv2.namedWindow("Select Point")
cv2.setMouseCallback("Select Point", select_point)
cv2.imshow("Select Point", frame)
cv2.waitKey(0)
cv2.destroyWindow("Select Point")

# Convert frame to grayscale for initial tracking
prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Track point in subsequent frames
while True:
  # Capture frame-by-frame
  ret, frame = cap.read()
  
  # Check if frame is read correctly
  if not ret:
    print("No more frames captured")
    break

  # Track the point
  tracking_point = track_point(frame, prev_gray, tracking_point)

  # Draw circle on tracked point
  if tracking_point is not None:
    cv2.circle(frame, tracking_point, 5, (0, 255, 0), -1)

  # Update previous frame
  prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Display the resulting frame
  cv2.imshow('Tracking Point', frame)

  # Exit on 'q' key press
  if cv2.waitKey(1) == ord('q'):
    break

# Release capture
cap.release()
cv2.destroyAllWindows()
