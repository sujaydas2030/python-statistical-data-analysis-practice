#Detecting Non-Standard Franchise Pricing

# Libraries (do not edit)
from ast import literal_eval
import math
def identify_non_standard_outlets(outlet_data):
    # Code here
  parameters_together=[]
  for outlet,data in outlet_data: #sequence unpacking
    avg=math.floor(sum(data)/len(data)) #floor of the achived average
    std= math.floor((sum((price-avg)**2 for price in data)/len(data))**0.5) #floor of the achieved standard deviation
    parameters_together.append((outlet,(avg,std)))

  parameters_identifier={} #creating a dictionary, key is parameters and values are counts of parameters
  for outlet,parameters in parameters_together:
    parameters_identifier[parameters]=parameters_identifier.get(parameters,0)+1

  max_count = 0
  candidate_base_parameters = [] #identifying hte parameters and append in a list
  for parameters, count in parameters_identifier.items():
      if count > max_count:
          max_count = count
          candidate_base_parameters = [parameters]
      elif count == max_count:
          candidate_base_parameters.append(parameters)

  # If there's a tie for the most frequent parameter set,
  # pick the one that is numerically smallest (lexicographical sort for tuples)
  base_parameter = sorted(candidate_base_parameters)[0]

  outlier_outlets=[] #identifying the outlier parameters and appending hte outlet
  for outlet,parameters in parameters_together:
    if parameters!=base_parameter:
      outlier_outlets.append(outlet)
  if len(outlier_outlets)>0:
    return sorted(outlier_outlets)
  else:
    return"All outlets aligned"



# Input and output processing (do not edit)
print(identify_non_standard_outlets(literal_eval(input())))
