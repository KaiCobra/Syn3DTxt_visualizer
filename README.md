# Syn3DTxt_render Visualizer
![Visualizer](https://img.shields.io/badge/Visualizer-8A2BE2)
[![GitHub Repo](https://img.shields.io/badge/GitHub-SynTxt--Gen-blue?logo=github)](https://github.com/theohsiung/SynTxt-Gen)

Visualizer for [Syn3DTxt: Embedding 3D Cues for Scene Text Generation](https://arxiv.org/abs/2505.18479)

Main Repository: [SynTxt-Gen](https://github.com/theohsiung/SynTxt-Gen)

This project provides visualization and rendering tools for Syn3DTxt, as presented at the CVPR 2025 Syntagen Workshop. 

Click here to try it out [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://syn3dtxt-visualizer.streamlit.app/)

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

> @misc{hsiung2025syn3dtxtembedding3dcues,
      title={Syn3DTxt: Embedding 3D Cues for Scene Text Generation}, 
      author={Li-Syun Hsiung and Jun-Kai Tu and Kuan-Wu Chu and Yu-Hsuan Chiu and Yan-Tsung Peng and Sheng-Luen Chung and Gee-Sern Jison Hsu},
      year={2025},
      eprint={2505.18479},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2505.18479}, 
}

[OpenReview link (CVPR 2025 SyntaGen Workshop)](https://arxiv.org/abs/2505.18479)



## Acknowledgements
- Developed for the Syn3DTxt project and Syntagen Workshop @ CVPR 2025.

---
中文版簡介：

本專案為 Syn3DTxt: Embedding 3D Cues for Scene Text Generation 的可視化工具，
用於 3D 場景文字生成的視覺化與渲染，並已於 CVPR Syntagen Workshop 發表。

如需協助或有問題，歡迎開 issue！
