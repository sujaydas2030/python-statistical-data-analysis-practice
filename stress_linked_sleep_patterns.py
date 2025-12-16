#Detect Stress-Linked Sleep Patterns with the help of correlation
# Libraries (do not edit)
from ast import literal_eval

def find_stress_linked_users(user_data):
    # Code here
  heart_rate=[]
  sleeping_hour=[]
  data_storage_with_user_id={}
  for user,heart_rate_with_sleeping_hour in user_data:
    for heart_rate_ , sleeping_hour_ in heart_rate_with_sleeping_hour:
      heart_rate.append(heart_rate_)
      sleeping_hour.append(sleeping_hour_)
    data_storage_with_user_id[user]=[heart_rate,sleeping_hour]
    heart_rate=[]
    sleeping_hour=[]
  # return data_storage_with_user_id
  correlation_mapping={} #initializing an empty dictionary
  for user, datas in data_storage_with_user_id.items():
    heart_data,sleeping_data = datas
    heart_rate_mean=sum(heart_data)/len(heart_data) #mean of heart_data
    sleeping_hour_mean=sum(sleeping_data)/len(sleeping_data) #mean of sleeping hour
    numerator=sum((heart_data[i]-heart_rate_mean)*(sleeping_data[i]-sleeping_hour_mean) for i in range(len(heart_data))) #covariance of hte dataset
    denomenator= (sum((heart_data[i]-heart_rate_mean)**2 for i in range(len(heart_data))))**0.5 * (sum((sleeping_data[i]-sleeping_hour_mean)**2 for i in range(len(sleeping_data))))**0.5 #standard deviation of the dataset
    if denomenator==0:
      correlataion=0
    else:
      correlataion= numerator/denomenator
    #correlation=covariance/std_dev
    correlation_mapping[user]=correlataion #updating dictionary with key=user, value=correlation

  stress_linked_patients=[] #initializing an empty list
  for user,correlataion_value in correlation_mapping.items():
    if correlataion_value<=-0.7:
      stress_linked_patients.append(user) #appending value to list, who has a correlation value less than or equal to 0.7

  if len(stress_linked_patients)==0:
    return 'No stress-linked patterns detected'
  else:
    return sorted(stress_linked_patients)

# Input and output processing (do not edit)
print(find_stress_linked_users(literal_eval(input())))

