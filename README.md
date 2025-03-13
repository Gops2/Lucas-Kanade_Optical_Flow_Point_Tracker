# **Lucas-Kanade Optical Flow Point Tracker**

This project tracks a user-selected point in a video using the **Lucas-Kanade Optical Flow** algorithm from OpenCV.

## **Features**
- Allows the user to select a point in the first frame.
- Uses **Lucas-Kanade Optical Flow** to track the point across frames.
- Displays the tracked point in real-time.
- Stops tracking when the video ends or the user presses `'q'`.

## **Requirements**
Ensure you have the following installed before running the script:

- Python 3.x
- OpenCV (`cv2`)
- NumPy

### **Install Dependencies**
Run the following command to install the required libraries:

```bash
pip install opencv-python numpy
```

## **Usage**
1. **Prepare Your Video**  
   - Replace `"path/to/your/video.mp4"` in the script with the actual path to your video file.

2. **Run the Script**
   ```bash
   python track_point.py
   ```

3. **Select a Point to Track**
   - The first frame of the video will be displayed.
   - Click on a point in the frame to select it.
   - Press any key to start tracking.

4. **Track the Point**
   - The selected point will be marked with a green circle.
   - The tracking continues until the video ends or you press `'q'`.

## **Code Breakdown**
- **Video Capture**: Reads video frames using OpenCV.
- **Point Selection**: Waits for the user to click a point on the first frame.
- **Lucas-Kanade Optical Flow**: Computes the motion of the point between frames.
- **Visualization**: Draws a green circle on the tracked point in real-time.

## **Potential Improvements**
- Improve error handling if tracking fails.
- Add a bounding box tracker instead of a single point.
- Support multiple point tracking.

## **License**
This project is open-source and available under the **MIT License**.
