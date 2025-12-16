#Portfolio Risk Analysis by calculating Variance and Std_Dev
from ast import literal_eval

# Function to calculate portfolio risk
def analyze_portfolio_risk(data):
    # Code here
    daily_returns,variance_threshold,std_dev_threshold=data
    if len(daily_returns)<2:
      return 'Low Risk: Within Acceptable Limits'
    mean_return=sum(daily_returns)/len(daily_returns)
    variance= sum((daily_return-mean_return)**2 for daily_return in daily_returns)/len(daily_returns)
    std_dev=variance**0.5
    if variance>variance_threshold and std_dev>std_dev_threshold:
      return 'High Risk: Exceeds Both Thresholds'
    elif variance>variance_threshold:
      return 'Moderate Risk: High Variance Only'
    elif std_dev>std_dev_threshold:
      return 'Moderate Risk: High Standard Deviation Only'
    elif variance<variance_threshold and std_dev<std_dev_threshold:
      return 'Low Risk: Within Acceptable Limits'

# Taking the input as a tuple (do not edit)
# Format: (daily_returns, variance_threshold, std_dev_threshold)
data = literal_eval(input())

# Calculate and output the risk status
print(analyze_portfolio_risk(data))
