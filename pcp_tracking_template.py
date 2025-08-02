import cv2
import numpy as np

# List of video paths
video_paths = [       # Option 2
    'Car Chase 1.mp4' ,
    'Car Chase 2.mp4' ,
    'Jet Dog Fight1.mp4'       # Option 3
]

# Create instruction screen
instruction_img = 135 * np.ones((400, 700, 3), dtype=np.uint8)

cv2.putText(instruction_img, "Press 1 for Station-1 tracking", (30, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
cv2.putText(instruction_img, "Press 2 for Station-2 tracking", (30, 150),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
cv2.putText(instruction_img, "Press 3 for Air footage tracking", (30, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

cv2.imshow("Select Video", instruction_img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
