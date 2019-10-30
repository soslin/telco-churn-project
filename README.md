# Telco Churn Project

GitHub storage 
soslin/telco-churn-project

Link to slides: https://docs.google.com/presentation/d/1nWUGKW1OIz850A8pwzPJi-7lRo7XLNlQhPGVnpLmJXw/edit?usp=sharing

## Data source
Data pulled from telco_churn database. All three associated tables were joined.

Within MySQL, data was filtered to remove tenure that was 0 or 1 months. Reasons: clients cannot churn without completing at least 1 month. Also, the high number of clients who churn at month 1 skews the churn distribution to such an extent that insights into why other clients churn are obscured. 

Data was also filtered for total_charges equal to null to ensure  missing were filtered out at the database level.

Records were reduced from 7,043 to 6,419.

## Checking for missing/anomalous values
When converting binary questions from text to 0/1, I discovered non-binary responses to 'multiple lines' (No phone service). I converted this response to 0 since a client cannot have multiple lines if they do not have phone service. Additionally, numerous columns pertaining to internet services offered by Telco had the response of 'No internet service'. I converted all of these to 0 for the same reason as above.  

I verified there were no additional missing values when I ran the .info() function. It confirmed that number count for each column was completed and the data types were correct (e.g. no Object data types).


## Definitions for new variables
1. Combined 'partner' and 'dependents' 
Variables are strongly correlated. Merged into a new variable called 'family'.

2. Combined two streaming variables
Variables are strongly correlated. Merged into a new variable called 'streaming'.

3. Combined 4 on-line service variables
Variables are strongly correlated. Merged into a new variable called 'services'

4. Dropped payment and billing variables as unnecessary for analysis

5. 'Internet_service_type_id' and 'contract_type_id' were each split into three new variables each to facilitate analysis
Internet = 'DSL', 'fiber_optic' and 'no_internet'
Contract = 'monthly', 'one_year', 'two_year'

6. Create new variable 'tenure_years
'tenure_years' is the number of months divided by 12 and rounded down to the nearest whole number. 

