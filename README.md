# UR3 Robotic Arm Pick-and-Place System
[![Watch Demo](https://img.youtube.com/vi/4Bmv51sXYaY/0.jpg)](https://youtu.be/4Bmv51sXYaY)
A real-time robotic system that detects objects using computer vision and executes autonomous pick-and-place on a UR3 arm.

Combines perception, coordinate transformations, and inverse kinematics to convert camera observations into precise robot actions.

## Overview

This system enables a UR3 robot to:
- Detect objects using AR (Aruco) markers
- Convert image-space detections into real-world coordinates
- Compute inverse kinematics for precise manipulation
- Execute autonomous pick-and-place operations

## Key Files (Start Here)

- [`block_detection_with_aruco.py`](https://github.com/Anusha-Sharma-2/UR3-Pick-and-Place/blob/main/UR3_Control/enme480_project/enme480_project/block_detection_aruco.py) → Detects markers and extracts object positions  
- [`get_perspective_warping_with_aruco.py`](https://github.com/Anusha-Sharma-2/UR3-Pick-and-Place/blob/main/UR3_Control/enme480_project/enme480_project/get_perspective_warping_with_aruco.py) → Computes camera → table transformation  
- [`main_pipeline.py`](https://github.com/Anusha-Sharma-2/UR3-Pick-and-Place/blob/main/UR3_Control/enme480_project/enme480_project/main_pipeline.py) → Core pipeline (perception → transform → control)  
- [`kinematic_functions.py`](https://github.com/Anusha-Sharma-2/UR3-Pick-and-Place/blob/main/UR3_Control/enme480_project/enme480_project/kinematic_functions.py) → Forward Kinematics and Inverse Kinematics functions

## Pipeline

1. **Perception** – Detect ArUco markers (OpenCV)  
2. **Transform** – Map image → world coordinates (homography)  
3. **Planning** – Compute joint angles (inverse kinematics)  
4. **Execution** – Pick, move, and place object (ROS + UR3)
## Future Improvements

- Replace marker-based detection with general object detection (e.g., YOLO)
- Add multi-object sorting and task planning
- Integrate feedback-based control for higher precision
- Improve robustness to camera movement and noise

---
