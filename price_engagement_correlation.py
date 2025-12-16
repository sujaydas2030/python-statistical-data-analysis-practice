#Impact of Pricing on User Engagement(establishing correlation)
from ast import literal_eval

def analyze_price_time_relation(data):
    # Code here
    x,y=data
    x_bar=sum(x)/len(x)
    y_bar=sum(y)/len(y)
    numerator= sum((x[i]-x_bar)*(y[i]-y_bar) for i in range(len(x)))
    denomenator=(sum((x[i]-x_bar)**2 for i in range(len(x))))**0.5 * (sum((y[i]-y_bar)**2 for i in range(len(y))))**0.5
    correlation= numerator/denomenator
    if abs(correlation)>=0.7:
      return "Strong"
    elif abs(correlation)>0.3:
      return "Weak"
    else:
      return "Neutral"
    #numerator=sum((x-x_bar)(y-y_bar))
    #denomenator= sqrt(sum((x-x_bar)^2)) * sqrt(sum((Y-Y_bar)^2))
# (do not edit)
print(analyze_price_time_relation(literal_eval(input())))

