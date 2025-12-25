# import
import streamlit as st 
import matplotlib.pyplot as plt 
import numpy as np 

# header
st.title("Praktikum 06 Stacked Vertical Bar Chart")
st.write("Kelompok: 1")
st.markdown("""
            1. **MUHAMMAD ZIDAN** - 0110222280
            2. **IQLIMA FASHA RIZQIA** – 0110122006   
""")

# dataset
stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female = [120, 230, 170]

# data transaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

# data quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

# 1 Grafik Stacked Vertical Bar Chart
st.subheader("1. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, label='Female', color='pink')
ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)


# 2 Grafik Stacked Vertical Bar Chart
st.subheader("2. Stacked Vertical Bar Chart dengan Matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='green')

ax.set_title('Sales Transactions by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 3 Grafik Kustomisasi Stacked Vertical Bar Chart
st.subheader("3. Kustomisasi Stacked Vertical Bar Chart ")

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color='black')
st.pyplot(fig)

# 4 Grafik Multiple Stacked Vertical Bar Chart
st.subheader("4. Multiple Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# Quarter 1
ax.bar(x - width/2, q1_male, label='Q1 Male', color='lightblue', width=width)
ax.bar(x - width/2, q1_female, bottom=q1_male, label='Q1 Female', color='pink', width=width)

# Quarter 2
ax.bar(x - width/2, q2_male, label='Q1 Male', color='blue', width=width)
ax.bar(x - width/2, q2_female, bottom=q1_male, label='Q2 Female', color='red', width=width)

ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)