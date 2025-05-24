# Syn3DTxt_render Visualizer
![Visualizer](https://img.shields.io/badge/Visualizer-8A2BE2)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://syn3dtxt-visualizer.streamlit.app/) [![GitHub Repo](https://img.shields.io/badge/GitHub-SynTxt--Gen-blue?logo=github)](https://github.com/theohsiung/SynTxt-Gen)

Visualizer for [Syn3DTxt: Embedding 3D Cues for Scene Text Generation](https://openreview.net/forum?id=QmY75NG5Vp&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3Dthecvf.com%2FCVPR%2F2025%2FWorkshop%2FSyntaGen%2FAuthors%23your-submissions))

Main Repository: [SynTxt-Gen](https://github.com/theohsiung/SynTxt-Gen)

This project provides visualization and rendering tools for Syn3DTxt, as presented at the CVPR 2025 Syntagen Workshop.

## Features
- 3D scene text generation visualization
- Interactive Streamlit demo for exploring 3D text cues
- Utilities for image transformation, background replacement, and color mapping

## Getting Started

### Requirements
- Python 3.8+
- [Streamlit](https://streamlit.io/)
- numpy
- opencv-python
- plotly
- wand
- tqdm
- scikit-image

You can install dependencies via pip:
```bash
pip install -r requirements.txt
```

### Usage
#### 1. Streamlit Visualizer
Run the interactive demo:
```bash
streamlit run app.py
```

## Project Structure
```
Syn3DTxt_render/
├── utils/                # Utility modules for image processing
├── static/               # Static assets (e.g., images)
├── app.py                # Streamlit demo for visualization
├── Gen2.py               # Main script for data generation
├── packages.txt          # Package list for dependencies
├── README.md             # Project documentation
├── requirements.txt      # Python package requirements
```

## Reference
If you use this tool, please cite:

> Syn3DTxt: Embedding 3D Cues for Scene Text Generation. CVPR 2025 SyntaGen Workshop.

[OpenReview link (CVPR 2025 SyntaGen Workshop)](https://openreview.net/forum?id=QmY75NG5Vp&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3Dthecvf.com%2FCVPR%2F2025%2FWorkshop%2FSyntaGen%2FAuthors%23your-submissions))



## Acknowledgements
- Developed for the Syn3DTxt project and Syntagen Workshop @ CVPR 2025.

---
中文版簡介：

本專案為 Syn3DTxt: Embedding 3D Cues for Scene Text Generation 的可視化工具，
用於 3D 場景文字生成的視覺化與渲染，並已於 CVPR Syntagen Workshop 發表。

如需協助或有問題，歡迎開 issue！
