#identifying most popular event based on mode
from ast import literal_eval

def verify_event_popularity(events):
    # Code here
  events_dict={} # creating dictionary, key=events, values=no of repeat
  popular_events=[]
  for event in events:
    events_dict[event]=events_dict.get(event,0)+1
  for event,count in events_dict.items():
    if count==max(events_dict.values()):
      popular_events.append(event)
  return sorted(popular_events)
# (do not edit)
print(verify_event_popularity(literal_eval(input())))
