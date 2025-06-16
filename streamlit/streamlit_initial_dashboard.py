import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#cleaned data
df = pd.read_csv("data/processed/marketing_campaign_cleaned.csv")

st.title("📊 Marketing Analytics Dashboard")

#total spending by education
st.subheader("Total Spending by Education Level")
spend_by_edu = df.groupby('Education')['Total_Spent'].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots()
spend_by_edu.plot(kind='bar', ax=ax1)
ax1.set_ylabel("Total Spend")
st.pyplot(fig1)

#new Ccustomers over time
st.subheader("Customer Acquisition Over Time")
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
customers_over_time = df.groupby(df['Dt_Customer'].dt.to_period("M")).size()

fig2, ax2 = plt.subplots()
customers_over_time.plot(ax=ax2)
ax2.set_ylabel("Number of New Customers")
st.pyplot(fig2)

# campaign response Pie Chart
st.subheader("Campaign Response Rate")
response_counts = df['Response'].value_counts()

fig3, ax3 = plt.subplots()
ax3.pie(response_counts, labels=response_counts.index, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
st.pyplot(fig3)
