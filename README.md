Telco Churn Project

GitHub: soslin/telc-churn-project

Data pulled from telco_churn database. All three tables were joined.

Missing values: tenure had 0 for new customers, total_charges had missing values. Since this is an analysis of churn, I removed customers who have had no time to churn. 

When converting binary questions from text to 0/1, I discovered non-binary responses to 'multiple lines' (No phone service). I converted this response to 0 since a client cannot have multiple lines if they do not have phone service. Additionally, numerous columns pertaining to internet services offered by Telco had the response of No internet service. I converted all of these to 0 for the same reason as above.  

I verified there were no additional missing values when I ran the .info() function. It confirmed that number count for each column was completed and the data types were correct.