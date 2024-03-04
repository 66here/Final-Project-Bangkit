import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
    """
    # Dashboard E-Commerce Dataset
    """
)
df1 = pd.read_csv("https://raw.githubusercontent.com/66here/Final-Project-Bangkit/main/df_1.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/66here/Final-Project-Bangkit/main/df_2.csv")

df1['shipping_limit_date'] = pd.to_datetime(df1['shipping_limit_date'])
df_2017 = df1[df1['shipping_limit_date'].dt.year == 2017]
result = df_2017.groupby('product_category_name_english').agg(
    total_orders=('order_id', 'nunique'),
    total_sales=('price', 'sum')
).reset_index()
top_categories = result.nlargest(5, 'total_sales')
st.subheader('Top 5 Penjualan Produk berdasarkan Kategori pada 2017')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_categories['product_category_name_english'], top_categories['total_sales'], color='skyblue')
ax.set_xlabel('Kategori Produk')
ax.set_ylabel('Total Penjualan')
ax.set_title('Top 5 Penjualan Produk berdasarkan Kategori pada 2017')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)


df2['order_purchase_timestamp'] = pd.to_datetime(df2['order_purchase_timestamp'])
df_2018 = df2[(df2['order_purchase_timestamp'].dt.year == 2018)]
monthly_sales = df_2018.resample('M', on='order_purchase_timestamp')['price'].sum()
st.subheader('Tren Pembelian Tahun 2018')
st.line_chart(monthly_sales)
