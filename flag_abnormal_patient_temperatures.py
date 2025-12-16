#Flagging of Abnormal Patient Temperatures, if exceed 2 STDs
# Libraries (do not edit)
from ast import literal_eval

def flag_highly_deviated_temperatures(temperatures):
    # Code here
  mean_temp=sum(temperatures)/len(temperatures) #mean temperature
  numerator=0
  for temperature in temperatures:
    numerator+=(temperature-mean_temp)**2
  denomenator=len(temperatures)
  std_dev=(numerator/denomenator)**0.5 #standard deviation of temperatures
  upper_limit=mean_temp+(2*std_dev)
  lower_limit=mean_temp-(2*std_dev)
  flag_temp=[]
  for temperature in temperatures:
    if temperature>upper_limit or temperature<lower_limit:
      flag_temp.append(temperature)
  return flag_temp

# Input and output processing (do not edit)
print(flag_highly_deviated_temperatures(literal_eval(input())))

