# Breaker Synthetic Datagen

A specialized pipeline for generating high-quality synthetic datasets for electrical breaker detection. 

## Overview

This project leverages Blender and domain randomization to create diverse, photorealistic training data. By simulating various lighting conditions, textures, and camera angles, we can train robust YOLO models that generalize well to real-world electrical panels.

## Key Features

- **Blender Automation**: Scripted 3D scene generation for mass data production.
- **Domain Randomization**: Automatic variation of lighting, materials, and object placements.
- **YOLO Integration**: Direct export of labeled data in YOLO-compatible formats.
- **Hybrid Training**: Pipeline designed for pre-training on synthetic data followed by real-world fine-tuning.

## Getting Started

1. **Prerequisites**: [Blender](https://www.blender.org/) 3.x+ and Python 3.9+.
2. **Installation**:
   ```bash
   git clone https://github.com/cerrmcneel/breaker-synthetic-datagen.git
   cd breaker-synthetic-datagen
   pip install -r requirements.txt
   ```

## License

MIT
