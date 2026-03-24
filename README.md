# Cube Rotation + 3D Color Histogram Visualization

A 3-stage computer vision pipeline connecting 3D rendering, real-time image analysis, and interactive visualization.

## Pipeline

| Stage | Tool | Role |
|-------|------|------|
| 1 | Blender | Animated rotating cube with texture-mapped images |
| 2 | C++ / OpenCV | Frame capture, HSV conversion, histogram computation |
| 3 | Python / Matplotlib | Interactive 3D bar chart visualization |

---

## Features

- Rotating 3D cube with real images mapped onto each face (Blender)
- Real-time HSV color histogram computation using `cv::calcHist`
- Preprocessing pipeline: Gaussian Blur → HSV Color Space Conversion
- Interactive 3D bar chart (Hue × Saturation × Frequency) via `mpl_toolkits.mplot3d`
- Demonstrates how color histograms form sparse distributions in 3D space

## Project Structure

```
cube-histogram-visualizer/
├── histogram.slnx          # OpenCV histogram computation (C++)
├── plot_histogram.py       # Matplotlib 3D visualization (Python)
├── assets/
│   └── demo.gif            # Demo recording
└── README.md
```

## Setup & Usage

### Prerequisites
- Blender 3.x+
- C++17 compiler
- OpenCV 4.x
- Python 3.x — `pip install numpy matplotlib opencv-python`

### Run

**Step 1 – Render frames in Blender**
Open your Blender scene, texture-map images onto the cube faces, and render the animation.

**Step 2 – Compute histogram (C++)**
```bash
g++ histogram.slnx -o histogram `pkg-config --cflags --libs opencv4`
./histogram
```

**Step 3 – Visualize (Python)**
```bash
python plot_histogram.py
```

## Acknowledgements

Developed under the guidance of **Prof. Maxwell Bruce** as part of Computer Vision coursework at **Northeastern University**.

## Tech Stack

`Blender` `C++` `OpenCV` `Python` `NumPy` `Matplotlib` `mpl_toolkits.mplot3d`
