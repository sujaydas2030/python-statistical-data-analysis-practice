#restoring missing data with help of mean
from ast import literal_eval

def restore_missing_sale(data):
    # Code here
    sales_data,avg = data
    sales_excluding_missing_data=sum(sales_data)
    total_days=len(sales_data)+1
    total_sales=avg*total_days
    missing_sale=total_sales-sales_excluding_missing_data
    return missing_sale


# (do not edit)
user_input = input()
parsed_input = literal_eval(user_input)
print(round(restore_missing_sale(parsed_input), 2))
