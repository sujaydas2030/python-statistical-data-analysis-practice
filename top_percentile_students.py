#Identifying Top Performers in Test, more than 95 percentile
scores=[]
def top_percentile_students(data):
    # Code here
  for student in data:
    id,student_score=student
    scores.append(student_score)
  top_performers=[]
  scores.sort()
  index=0.95*(len(scores)-1) #finding index of the 95 percentile
  lower=int(index) #As the index is float, we need to find the lower value
  upper=lower+1 # and then the upper value
  fraction=index-lower #this is the rest fraction values

  the_percentile=scores[lower]+fraction*(scores[upper]-scores[lower]) #formula to get the the percentile value
  for student in data:
    id,student_score=student
    if student_score>=the_percentile:
      top_performers.append(id)
  return sorted(top_performers)

# Input and output processing (do not edit)
from ast import literal_eval
print(top_percentile_students(literal_eval(input())))

