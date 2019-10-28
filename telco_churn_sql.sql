USE telco_churn;

#  Join all telco_churn tables
SELECT * FROM customers AS c
JOIN contract_types AS ct
	ON c.contract_type_id = ct.contract_type_id
JOIN internet_service_types AS i
	ON i.internet_service_type_id = c.internet_service_type_id
JOIN payment_types AS p
	ON c.payment_type_id = p.payment_type_id;
# 7043 rows

# ****** Data to be imported into Python: Remove customers in first month of service (not been billed yet) ******
SELECT * FROM customers AS c
JOIN contract_types AS ct
	ON c.contract_type_id = ct.contract_type_id
JOIN internet_service_types AS i
	ON i.internet_service_type_id = c.internet_service_type_id
JOIN payment_types AS p
	ON c.payment_type_id = p.payment_type_id
WHERE tenure > 0 OR total_charges > 0;
# 7032 rows


# Are there internet_service_type_id not = 1? Yes
SELECT * FROM customers AS c
JOIN contract_types AS ct
	ON c.contract_type_id = ct.contract_type_id
JOIN internet_service_types AS i
	ON i.internet_service_type_id = c.internet_service_type_id
JOIN payment_types AS p
	ON c.payment_type_id = p.payment_type_id
WHERE c.internet_service_type_id != 1;

# Are there contract_type_id not = 1? Yes
SELECT * FROM customers AS c
JOIN contract_types AS ct
	ON c.contract_type_id = ct.contract_type_id
JOIN internet_service_types AS i
	ON i.internet_service_type_id = c.internet_service_type_id
JOIN payment_types AS p
	ON c.payment_type_id = p.payment_type_id
WHERE c.contract_type_id != 1;