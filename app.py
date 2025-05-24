import streamlit as st
import numpy as np
import cv2
import os
import plotly.graph_objects as go

from utils.spherical_2_rgb import spherical2RGB
from utils.Image_transformer import ImageTransformer
from Gen2 import replace_white_with_color

st.set_page_config(page_title="SyntaGen 互動 Demo", layout="wide")

st.title("3D 球面散點圖與圖片旋轉換色")

# 1. 球面參數設定
col1, col2 = st.columns([1,2])
with col1:
    n_theta = st.slider("n_theta", 2, 50, 10)
    n_phi = st.slider("n_phi", 2, 50, 10)
    theta = st.slider('θ (pitch)', -90, 90, 0)
    phi = st.slider('φ (yaw)', -75, 75, 0)

# 2. 生成球面點雲
# 參考 sphere.py 寫法，產生球面點雲
theta_vals = np.linspace(-90, 90, n_theta)
phi_vals = np.linspace(-90, 90, n_phi)
theta_grid, phi_grid = np.meshgrid(theta_vals, phi_vals)
# 與 spherical2RGB 保持一致
theta_adj = (theta_grid + 180) % 360 - 90
phi_adj = 1 * ((phi_grid + 180) % 360 - 180)
theta_rad = np.deg2rad(theta_adj)
phi_rad = np.deg2rad(phi_adj)
x = np.sin(theta_rad) * np.cos(phi_rad)
y = np.sin(theta_rad) * np.sin(phi_rad)
z = np.cos(theta_rad)
x_flat = x.flatten()
y_flat = y.flatten()
z_flat = z.flatten()
vertex_colors = []
for t, p in zip(theta_grid.flatten(), phi_grid.flatten()):
    rgb, _ = spherical2RGB(t, p)
    vertex_colors.append(f"rgb({int(rgb[0])},{int(rgb[1])},{int(rgb[2])})")

sphere_scatter = go.Scatter3d(
    x=x_flat,
    y=y_flat,
    z=z_flat,
    mode='markers',
    marker=dict(
        size=5,
        color=vertex_colors,
        opacity=1.0
    )
)
center_point = go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode='markers+text',
    marker=dict(size=10, color='red', symbol='circle'),
    text=["(0,0,0)"],
    textposition="top center",
    textfont=dict(color="red", size=12)
)
x_axis = go.Scatter3d(
    x=[0, 1], y=[0, 0], z=[0, 0],
    mode='lines+text',
    line=dict(color='blue', width=4),
    text=["", "X"],
    textposition="top center"
)
y_axis = go.Scatter3d(
    x=[0, 0], y=[0, 1], z=[0, 0],
    mode='lines+text',
    line=dict(color='red', width=4),
    text=["", "Y"],
    textposition="top center"
)
z_axis = go.Scatter3d(
    x=[0, 0], y=[0, 0], z=[0, 1],
    mode='lines+text',
    line=dict(color='green', width=4),
    text=["", "Z"],
    textposition="top center"
)
fig = go.Figure(data=[sphere_scatter, center_point, x_axis, y_axis, z_axis])
fig.update_layout(
    scene=dict(
        aspectmode='data',
        xaxis=dict(visible=False, showgrid=False, zeroline=False, showticklabels=False, showbackground=False),
        yaxis=dict(visible=False, showgrid=False, zeroline=False, showticklabels=False, showbackground=False),
        zaxis=dict(visible=False, showgrid=False, zeroline=False, showticklabels=False, showbackground=False)
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)
with col2:
    st.plotly_chart(fig, use_container_width=True)

# 3. 圖片旋轉與換色
rgb, bgr = spherical2RGB(theta, phi)
bgr_tuple = tuple(int(v) for v in bgr)
img_path = os.path.join('static', 'Text_img.png')

transformer = ImageTransformer(img_path, (256, 256))
img_rot = transformer.rotate_along_axis(theta=theta, phi=phi, gamma=0)
img_colored = replace_white_with_color(img_rot.copy(), target_rgb=bgr_tuple)

st.image(img_colored, channels="BGR", caption=f"θ={theta}, φ={phi}, color={bgr_tuple}")

st.markdown(f"""
- 法向量: {np.round(rgb,3)}
- 顏色 (BGR): {bgr_tuple}
""")