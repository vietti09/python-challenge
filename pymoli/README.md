

```python
import pandas as pd
import json
```


```python
# Read with Pandas
purchase_df = pd.read_json('purchase_data.json')
```


```python
#Show database to look at data
purchase_df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate total number of players
total_players = {"Total Players": purchase_df['SN'].nunique()}
total_players_df = pd.DataFrame([total_players])
total_players_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
#caluclate unique items for purchasing analysis table
unique_items = {"Unique Items": purchase_df['Item Name'].nunique()}
items_df = pd.DataFrame([unique_items])
items_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unique Items</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
    </tr>
  </tbody>
</table>
</div>




```python
#calculate average price of unique items for purchasing analysis table
avg_price = {"Average Price":purchase_df["Price"].mean()}
avg_price_df = pd.DataFrame([avg_price])
avg_price_df = pd.DataFrame(avg_price_df["Average Price"].map("${:,.2f}".format))
avg_price_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Add average price to purchasing analysis table
items_df = items_df.join(avg_price_df)
items_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unique Items</th>
      <th>Average Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate number of purchases for purchasing analysis table
number_purchases = {"Number of Purchases":len(purchase_df)}
number_purchases_df = pd.DataFrame([number_purchases])
number_purchases_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Purchases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>780</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Add number of purchases to purchasing analysis table
items_df = items_df.join(number_purchases_df)
items_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate total revenue for purchasing analysis table
total_revenue = {"Total Revenue": purchase_df["Price"].sum()}
total_revenue_df = pd.DataFrame([total_revenue])
total_revenue_df = pd.DataFrame(total_revenue_df["Total Revenue"].map("${:,.2f}".format))
total_revenue_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Add total revenue to purchasing analysis table
items_df = items_df.join(total_revenue_df)
items_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate total number of each gender by adding screen names and subtracting duplicates
purchase_dd_df = purchase_df.drop_duplicates('SN')
total_genders_df = purchase_dd_df['Gender']
total_genders_df = total_genders_df.value_counts()
total_genders_df
```




    Male                     465
    Female                   100
    Other / Non-Disclosed      8
    Name: Gender, dtype: int64




```python
#Calculate total number of players from total of each gender
total_gender_count = total_genders_df.sum()
total_gender_count
```




    573




```python
#Calculate percent of each gender
percent_gender_df = total_genders_df/total_gender_count*100
percent_gender_df
```




    Male                     81.151832
    Female                   17.452007
    Other / Non-Disclosed     1.396161
    Name: Gender, dtype: float64




```python
#Build gender demographics table
genders_df = pd.concat([percent_gender_df.rename("Percentage of Players").map("{:,.1f}%".format), total_genders_df.rename("Total Count")], axis=1)
genders_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.2%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.5%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.4%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Begin purchase analysis by gender calculations; first is total genders by purchase
purchase_analysis_gender = purchase_df['Gender'].value_counts()
purchase_analysis_gender
```




    Male                     633
    Female                   136
    Other / Non-Disclosed     11
    Name: Gender, dtype: int64




```python
#Create a dataframe from our genders by purchase
purchase_count_df = pd.DataFrame(purchase_analysis_gender)
purchase_count_df.index.name = 'Gender'
purchase_count_df = purchase_count_df.rename(columns={'Gender':'Total Purchases'})
purchase_count_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate average purchase price by gender
avg_purchase_price = purchase_df.groupby('Gender')
avg_purchase_price = avg_purchase_price['Price'].mean()
avg_purchase_price
```




    Gender
    Female                   2.815515
    Male                     2.950521
    Other / Non-Disclosed    3.249091
    Name: Price, dtype: float64




```python
#Turn average purchase price into a dataframe and format correctly
avg_purchase_price_df = pd.DataFrame(avg_purchase_price)
avg_purchase_price_df.index.name = 'Gender'
avg_purchase_price_df = avg_purchase_price_df.rename(columns={'Price':'Avg Price'})
avg_purchase_price_df = avg_purchase_price_df['Avg Price'].map("${:,.2f}".format)
avg_purchase_price_df
```




    Gender
    Female                   $2.82
    Male                     $2.95
    Other / Non-Disclosed    $3.25
    Name: Avg Price, dtype: object




```python
#Continue building purchase analysis table (by gender)
purchases_df = purchase_count_df.join(avg_purchase_price_df)
purchases_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
      <th>Avg Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate total purchase value per gender
purchase_value = purchase_df.groupby('Gender')
purchase_value_df = purchase_value['Price'].sum().map("${:,.2f}".format)
purchase_value_df
```




    Gender
    Female                     $382.91
    Male                     $1,867.68
    Other / Non-Disclosed       $35.74
    Name: Price, dtype: object




```python
#Create a dataframe from purchase value per gender
purchase_value_df = pd.DataFrame(purchase_value_df)
purchase_value_df.index.name = 'Gender'
purchase_value_df = purchase_value_df.rename(columns={'Price':'Value'})
purchase_value_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>$382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>$1,867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Add total value to dataframe of purchase analysis per gender
purchases_df["Total Value"] = purchase_value_df
purchases_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
      <th>Avg Price</th>
      <th>Total Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Make some changes so I can do math
total_val = purchases_df['Total Value'].replace({'\$': '', ',': ''}, regex=True)
total_val
```




    Gender
    Male                     1867.68
    Female                    382.91
    Other / Non-Disclosed      35.74
    Name: Total Value, dtype: object




```python
#Make one more change for math in next step
total_val = total_val.astype(float)
total_val
```




    Gender
    Male                     1867.68
    Female                    382.91
    Other / Non-Disclosed      35.74
    Name: Total Value, dtype: float64




```python
#Calculate normalized totals of purchases per gender
norm_totals = total_val / total_genders_df
norm_totals = norm_totals.map("${:,.2f}".format)
norm_totals
```




    Gender
    Male                     $4.02
    Female                   $3.83
    Other / Non-Disclosed    $4.47
    dtype: object




```python
#Add normalized totals to get complete table for purchase analysis by genders
purchases_df["Normalized Totals"] = norm_totals
purchases_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
      <th>Avg Price</th>
      <th>Total Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create the bins of ages and labels for Age Demographics table
bins = [0, 10, 15, 20, 25,30,35,40,45,100]
label_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45+']
```


```python
#Start by creating a new column with bins titled "Age Group"
age_bins_df = purchase_df
age_bins_df["Age Group"] = pd.cut(
    purchase_df["Age"], bins, labels=label_names)
age_bins_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Caluclate number of purchases by age group
count_purchases_age = age_bins_df.groupby('Age Group')
count_purchases_age = count_purchases_age.count()['Price']
count_purchases_age
```




    Age Group
    <10       32
    10-14     78
    15-19    184
    20-24    305
    25-29     76
    30-34     58
    35-39     44
    40-44      3
    45+        0
    Name: Price, dtype: int64




```python
#Calculate average of purchases by age group
avg_purchases_age = age_bins_df.groupby('Age Group')
avg_purchases_age = avg_purchases_age.mean()['Price'].map("${:,.2f}".format)
avg_purchases_age = avg_purchases_age.replace('$nan', '$0.00')
avg_purchases_age
```




    Age Group
    <10      $3.02
    10-14    $2.87
    15-19    $2.87
    20-24    $2.96
    25-29    $2.89
    30-34    $3.07
    35-39    $2.90
    40-44    $2.88
    45+      $0.00
    Name: Price, dtype: object




```python
#Calculate total value of purchases by age group
total_purchases_age = age_bins_df.groupby('Age Group')
total_purchases_age = total_purchases_age.sum()['Price'].map("${:,.2f}".format)
total_purchases_age
```




    Age Group
    <10       $96.62
    10-14    $224.15
    15-19    $528.74
    20-24    $902.61
    25-29    $219.82
    30-34    $178.26
    35-39    $127.49
    40-44      $8.64
    45+        $0.00
    Name: Price, dtype: object




```python
#Calculate number of players per age group (dropping duplicates in SN) to use for normalized totals
sn_totals_age = age_bins_df.drop_duplicates(subset=['SN'], keep=False)
sn_totals_age = sn_totals_age.groupby('Age Group')
sn_totals_age = sn_totals_age.count()['Price']
sn_totals_age
```




    Age Group
    <10       13
    10-14     35
    15-19    100
    20-24    175
    25-29     35
    30-34     32
    35-39     12
    40-44      3
    45+        0
    Name: Price, dtype: int64




```python
#Calculate normalized total purchases by age group
norm_age_totals = age_bins_df.groupby('Age Group')
norm_age_totals = norm_age_totals.sum()['Price']
norm_age_totals = norm_age_totals / sn_totals_age
norm_age_totals = norm_age_totals.map("${:,.2f}".format)
norm_age_totals = norm_age_totals.replace('$nan', '$0.00')
norm_age_totals
```




    Age Group
    <10       $7.43
    10-14     $6.40
    15-19     $5.29
    20-24     $5.16
    25-29     $6.28
    30-34     $5.57
    35-39    $10.62
    40-44     $2.88
    45+       $0.00
    Name: Price, dtype: object




```python
#Start to build purchases by age group table
age_df = pd.DataFrame(count_purchases_age)
age_df = age_df.rename(columns={'Price':'Total Purchases'})
age_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>78</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>184</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>305</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>76</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>58</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>44</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>3</td>
    </tr>
    <tr>
      <th>45+</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Next step in building purchase by age group table
age_df['Avg Purchase Price'] = avg_purchases_age
age_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
      <th>Avg Purchase Price</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>78</td>
      <td>$2.87</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>184</td>
      <td>$2.87</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>305</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>76</td>
      <td>$2.89</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>58</td>
      <td>$3.07</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>44</td>
      <td>$2.90</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>3</td>
      <td>$2.88</td>
    </tr>
    <tr>
      <th>45+</th>
      <td>0</td>
      <td>$0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Next step in building purchase by age group table
age_df['Total Purchase Value'] = total_purchases_age
age_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
      <th>Avg Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>78</td>
      <td>$2.87</td>
      <td>$224.15</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>184</td>
      <td>$2.87</td>
      <td>$528.74</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>305</td>
      <td>$2.96</td>
      <td>$902.61</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>76</td>
      <td>$2.89</td>
      <td>$219.82</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>58</td>
      <td>$3.07</td>
      <td>$178.26</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>44</td>
      <td>$2.90</td>
      <td>$127.49</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
    </tr>
    <tr>
      <th>45+</th>
      <td>0</td>
      <td>$0.00</td>
      <td>$0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Last step in building purchase by age group table
age_df['Normalized Purchase Price'] = norm_age_totals
age_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchases</th>
      <th>Avg Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Purchase Price</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$7.43</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>78</td>
      <td>$2.87</td>
      <td>$224.15</td>
      <td>$6.40</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>184</td>
      <td>$2.87</td>
      <td>$528.74</td>
      <td>$5.29</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>305</td>
      <td>$2.96</td>
      <td>$902.61</td>
      <td>$5.16</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>76</td>
      <td>$2.89</td>
      <td>$219.82</td>
      <td>$6.28</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>58</td>
      <td>$3.07</td>
      <td>$178.26</td>
      <td>$5.57</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>44</td>
      <td>$2.90</td>
      <td>$127.49</td>
      <td>$10.62</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
      <td>$2.88</td>
    </tr>
    <tr>
      <th>45+</th>
      <td>0</td>
      <td>$0.00</td>
      <td>$0.00</td>
      <td>$0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate total amount spent per screen name, sort from most to least
total_price = purchase_df.groupby(['SN']).sum()["Price"]
total_price_df = pd.DataFrame(total_price).sort_values('Price', ascending=False)
total_price_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate total number of purchases by screen name
total_count = purchase_df.groupby(['SN']).count()["Price"]
total_count.sort_values(ascending=False).head()
```




    SN
    Undirrala66    5
    Hailaphos89    4
    Mindimnya67    4
    Qarwen67       4
    Sondastan54    4
    Name: Price, dtype: int64




```python
#Combine purchase count with price to begin top spenders table
total_price_df["Purchase Count"] = total_count
total_price_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Purchase Count</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate average price paid per screen name
avg_price = purchase_df.groupby(['SN']).mean()["Price"].map("${:,.2f}".format)
avg_price.head()
```




    SN
    Adairialis76    $2.46
    Aduephos78      $2.23
    Aeduera68       $1.93
    Aela49          $2.46
    Aela59          $1.27
    Name: Price, dtype: object




```python
#Add average price per screen name to top spenders table
total_price_df["Average Price"] = avg_price
total_price_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Average Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
      <td>$3.41</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
      <td>$3.39</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
      <td>$3.18</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
      <td>$4.24</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
      <td>$3.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate total purchase value per screen name
total_purchase_value = purchase_df.groupby(['SN']).sum()["Price"].map("${:,.2f}".format)
total_purchase_value.head()
```




    SN
    Adairialis76    $2.46
    Aduephos78      $6.70
    Aeduera68       $5.80
    Aela49          $2.46
    Aela59          $1.27
    Name: Price, dtype: object




```python
#Add total purchase value per screen name to top spenders table
total_price_df["Total Purchase Value"] = total_purchase_value
total_price_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Average Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Delete an unnecessary column, display final top spenders table
total_price_df = total_price_df.drop('Price', 1)
total_price_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Begin most popular items table by sorting by item ID and name and sorting from most to least
purchases_count = purchase_df.groupby(['Item ID','Item Name']).count()['Price']
purchases_count_df = pd.DataFrame(purchases_count)
purchases_count_df = purchases_count_df.sort_values('Price',ascending=False)
purchases_count_df = purchases_count_df.rename(columns={"Price":"Purchase Count"})
purchases_count_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate average purchase price per item for most popular items table
purchase_price = purchase_df.groupby(['Item ID','Item Name'])['Price']
purchase_price = purchase_price.mean().map("${:,.2f}".format)
```


```python
#Calculate total purchase price per item for most popular items table
total_price = purchase_df.groupby(['Item ID','Item Name'])['Price']
total_price = total_price.sum().map("${:,.2f}".format)
```


```python
#Finalize most popular items table
purchases_count_df['Price'] = purchase_price
purchases_count_df['Total Price']=total_price
purchases_count_df.head(6)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Price</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Sum total purchase values for each item
item_total_purchase = purchase_df.groupby(['Item ID','Item Name'])['Price']
item_total_purchase = item_total_purchase.sum()
item_total_purchase_df = pd.DataFrame(item_total_purchase)
item_total_purchase_df = item_total_purchase_df.rename(columns={"Price":"Total Purchase Value"})
item_total_purchase_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <th>Splinter</th>
      <td>1.82</td>
    </tr>
    <tr>
      <th>1</th>
      <th>Crucifer</th>
      <td>9.12</td>
    </tr>
    <tr>
      <th>2</th>
      <th>Verdict</th>
      <td>3.40</td>
    </tr>
    <tr>
      <th>3</th>
      <th>Phantomlight</th>
      <td>1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <th>Bloodlord's Fetish</th>
      <td>2.28</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Calculate item purchase count and add to most profitable item table
item_purchase_count = purchase_df.groupby(['Item ID','Item Name'])['Price']
item_purchase_count = item_purchase_count.count()
item_total_purchase_df['Total Purchase Count'] = item_purchase_count
item_total_purchase_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Purchase Value</th>
      <th>Total Purchase Count</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <th>Splinter</th>
      <td>1.82</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <th>Crucifer</th>
      <td>9.12</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <th>Verdict</th>
      <td>3.40</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <th>Phantomlight</th>
      <td>1.79</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <th>Bloodlord's Fetish</th>
      <td>2.28</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Use purchase price calculated before; add to most profitable item table
item_total_purchase_df['Purchase Price'] = purchase_price
item_total_purchase_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Purchase Value</th>
      <th>Total Purchase Count</th>
      <th>Purchase Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <th>Splinter</th>
      <td>1.82</td>
      <td>1</td>
      <td>$1.82</td>
    </tr>
    <tr>
      <th>1</th>
      <th>Crucifer</th>
      <td>9.12</td>
      <td>4</td>
      <td>$2.28</td>
    </tr>
    <tr>
      <th>2</th>
      <th>Verdict</th>
      <td>3.40</td>
      <td>1</td>
      <td>$3.40</td>
    </tr>
    <tr>
      <th>3</th>
      <th>Phantomlight</th>
      <td>1.79</td>
      <td>1</td>
      <td>$1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <th>Bloodlord's Fetish</th>
      <td>2.28</td>
      <td>1</td>
      <td>$2.28</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Sort most profitable item table by total purchase value
item_total_purchase_df = item_total_purchase_df.sort_values('Total Purchase Value', ascending=False)
item_total_purchase_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Purchase Value</th>
      <th>Total Purchase Count</th>
      <th>Purchase Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>37.26</td>
      <td>9</td>
      <td>$4.14</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>29.75</td>
      <td>7</td>
      <td>$4.25</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>29.70</td>
      <td>6</td>
      <td>$4.95</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>29.22</td>
      <td>6</td>
      <td>$4.87</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>28.88</td>
      <td>8</td>
      <td>$3.61</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Reorder columns for final most profitable item table
cols = ['Total Purchase Count','Purchase Price', 'Total Purchase Value']
item_total_purchase_df = item_total_purchase_df[cols]
item_total_purchase_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Purchase Count</th>
      <th>Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


