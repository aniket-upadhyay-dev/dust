import dust as dst
import numpy as np

df = dst.DDF('examples/Q1_Insurance_Sales.csv')

# approved premium
approved_premium = dst.Filter(df, df['Status'] == 'Approved')['Premium'] >> dst.Sum()

# average customer age by life insurance
avg_customage_lifeinsurance = dst.Filter(df, df['PolicyType'] == 'Life Insurance')['CustomerAge'] >> dst.Avg()

# count of declined sales
count_declinedSales = dst.Filter(df, df['Status'] == 'Declined')['Status'] >> dst.Count()

# premium of salesman Alice
alice_premium = dst.Filter(df, df['Salesman'] == 'Alice')['Premium'] >> dst.Sum()

"""Premium by salesman
group by syntax 
dst.GroupBy(df['Salesman'])['Premium'] >> dst.Sum()
"""