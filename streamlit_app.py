import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome! See the Power of Square!


"""

x_range = list(range(0, st.slider("X axis", 1, 1000, 1)))

fig, ax = plt.subplots()
ax.plot(x_range, [x ** 2 for x in x_range], "r-*")
st.pyplot(fig)