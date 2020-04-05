#!/usr/bin/env python
# coding: utf-8

# ## Heroes Of Pymoli Data Analysis
# 
# Of the 576 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# Our peak age demographic falls between 20-24 with a total purchase price of $1,114.06.
# The total value spend by the top spender is $18,96.

# In[498]:


#Dependencies
import pandas as pd


# In[499]:


#Set path for file
data_file = "Resources/purchase_data.csv"


# In[500]:


#Reading data
data_file_df = pd.read_csv(data_file)
data_file_df.head()


# ## Player Count

# In[501]:


# Total Number of Players
total_players = data_file_df["SN"].nunique()
total_players_df = pd.DataFrame([{"Total Players":total_players}])
total_players_df


# ## Purchasing Analysis (Total)

# In[502]:


# Number of Unique Items
unique_items = len(data_file_df["Item Name"].unique())
unique_items


# In[503]:


# Average Purchase Price
avg_pp = data_file_df["Price"].mean()
avg_pp


# In[504]:


# Total Number of Purchases
total_np = data_file_df["Purchase ID"].count()
total_np


# In[505]:


# Total Revenue
total_rev = data_file_df["Price"].sum()
total_rev


# In[506]:


# Frame and Format
purchase_analysis = pd.DataFrame({"Unique_Items":[179],"Avg_Price":[3.05],"Total_Purchases":[780],"Total_Revenue":[237977]})
purchase_analysis["Avg_Price"]= purchase_analysis["Avg_Price"].map("${:.2f}".format)
purchase_analysis["Total_Revenue"]= purchase_analysis["Total_Revenue"].map("${:}".format)
purchase_analysis


# ## Gender Demographics

# In[507]:


#Percentage and Count of Male, Female Players and Others
gender_count = data_file_df["Gender"].value_counts()
print(gender_count)


# In[508]:


#Percentage and Count of Male, Female Players and Others
gender_grouped = data_file_df.groupby("Gender")
players_gender = gender_grouped["SN"].nunique()
pct_players = (players_gender / total_players)*100
print(players_gender)
print(pct_players)

gender_summary = pd.DataFrame({"Total Players": players_gender, "Percentage of Players": pct_players})
gender_summary


# ## Puchasing Analysis (Gender)

# In[509]:


# Number of puchases by gender
purchase_gender = gender_grouped["Purchase ID"].count()
purchase_gender


# In[510]:


# Average prince of purchases by gender
avg_price_gender = gender_grouped["Price"].mean()
avg_price_gender


# In[511]:


# Total purchase value by gender
total_purchase_gender = gender_grouped["Price"].sum()
total_purchase_gender


# In[512]:


# Average purchase total per person by gender
avg_purchase_gender = (gender_grouped["Price"].sum()/total_players)
avg_purchase_gender


# In[513]:


# Print purchasing summary
purchasing_summary = pd.DataFrame({"Purchase Count": purchase_gender, "Average Purchase Price": avg_price_gender, "Total Purchase Price": total_purchase_gender, "Average Total Purchase per Person": avg_purchase_gender})
purchasing_summary


# ## Age Demographics

# In[514]:


# Create bins of 4 years
bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[515]:


# Purchase count by age
data_file_df["Age Group"] = pd.cut(data_file_df["Age"], bins=bins, labels=labels)
data_file_df.head()


# In[516]:


# Create age groupby
age_grouped = data_file_df.groupby("Age Group")
players_age = age_grouped["SN"].nunique()


# In[517]:


# Number of puchases by age
purchase_age = age_grouped["Purchase ID"].count()
purchase_age


# In[518]:


# Average prince of purchases by age
avg_price_age = age_grouped["Price"].mean()
avg_price_age


# In[519]:


# Total purchase value by age
total_purchase_age = age_grouped["Price"].sum()
total_purchase_age


# In[520]:


# Average purchase total per person by age
avg_purchase_age = (age_grouped["Price"].sum()/total_players)
avg_purchase_age


# In[521]:


# Print age demographics summary
age_demo_summary = pd.DataFrame({"Purchase Count": purchase_age, "Average Purchase Price": avg_price_age, "Total Purchase Price": total_purchase_age, "Average Total Purchase per Person": avg_purchase_age})
age_demo_summary


# ## Top Spenders

# In[522]:


# Create a groupby on SN
sn_grouped = data_file_df.groupby("SN")


# In[523]:


# Purchase count by SN
purchase_sn = sn_grouped["Purchase ID"].count()
purchase_sn


# In[524]:


# Average prince of purchases by SN
avg_price_sn = sn_grouped["Price"].mean()
avg_price_sn


# In[525]:


# Total purchase value by SN
total_purchase_sn = sn_grouped["Price"].sum()
total_purchase_sn


# In[526]:


# Print top 5 spenders summary
top_spenders_summary_df = pd.DataFrame({"Purchase Count": purchase_sn, "Average Purchase Price": avg_price_sn, "Total Purchase Price": total_purchase_sn})
top_spenders_summary_df.sort_values("Purchase Count", ascending=False, inplace=True)
top_spenders_summary_df.head(5)


# ## Most Popular Items

# In[527]:


# Create .loc and groupby
popular_df = data_file_df.loc[:,["Item ID", "Item Name", "Price"]]
pop_grouped = data_file_df.groupby(["Item ID", "Item Name"])
popular_df


# In[528]:


# 5 most popular items by purchase count
pop_purchase = pop_grouped["Age"].count()
pop_purchase


# In[529]:


# 5 most popular items by price
pop_price = pop_grouped["Price"].mean()
pop_price


# In[530]:


# 5 most popular items by total purchase value
pop_value = pop_grouped["Price"].sum()
pop_value


# In[531]:


# Print 5 most popular items summmary
pop_summary_df= pd.DataFrame({"Purchase Count": pop_purchase,"Item Price": pop_price, "Total Purchase Value": pop_value})
pop_summary_df.sort_values("Purchase Count", ascending=False, inplace=True)
pop_summary_df.head(5)


# ## Most Profitable Items

# In[532]:


# Sort above table by total purchase value
pop_summary_df.sort_values("Total Purchase Value", ascending=False, inplace=True)
pop_summary_df.head(5)


# In[ ]:





# In[ ]:





# In[ ]:




