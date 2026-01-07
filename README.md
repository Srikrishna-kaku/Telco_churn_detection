

# Telco Customer Churn Analysis
This project analyzes customer behavior to understand "Telco Customer Churn" data to figure out why some customers stay and others leave (churn). After looking at the charts, here are the main findings:

1. The Big Picture (Overall Churn)
What it shows: A pie chart of everyone in the data.

** Most customers (about 73%) are happy and staying. However, a significant portion (27%) has left the company. This 27% is the group we need to focus on.

2. The "Contract" Trap
What it shows: Comparing people on month-to-month plans versus those on 1 or 2-year contracts.

** This is the biggest factor. People on month-to-month plans are much more likely to leave. Those who sign a 1 or 2-year contract almost always stay. It seems loyalty is tied directly to the type of contract they sign.

3. New Customers vs. Loyal Veterans
What it shows: How long a customer has been with the company (Tenure).

** We have two main groups: a lot of brand-new customers and a lot of very old, loyal ones. The "danger zone" is the beginning. If a customer makes it past the first few months, they are likely to stay for years.

4. Price Matters
What it shows: A comparison of monthly bills between those who left and those who stayed.

** Customers who leave generally have higher monthly bills than those who stay. When the bill gets too high, customers start looking for cheaper options elsewhere.

5. Senior Citizens
What it shows: Churn rates specifically for older customers.

** Senior citizens are a smaller group, but they are leaving at a higher rate than younger people. We may need to look at whether our technology is too complicated for them or if they need better-priced senior plans.

Simple Recommendations:
Move people off month-to-month plans: Offer a small discount if they switch to a 1-year plan.

Watch the high bills: If a customer's bill crosses a certain high threshold, reach out with a loyalty discount before they decide to leave.

Focus on  customers problems: Give extra support to customers in their first 3–6 months to make sure they get settled in and don't cancel early.

🛠️ How to Run the Analysis

I was installed Pandas,Numpy,Matplotlib and Seaborn libraries in python
##Data Cleaning: 
*Converting TotalCharges to numeric values.
*Filling missing values in TotalCharges using the median.
*Removing unnecessary columns like customerID.
