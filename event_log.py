import pandas as pd 

log_file = pd.read_csv('eventlogs.csv')

df = pd.DataFrame(log_file)

# Total number of events 
total_events = df.count()

print('Total number of events: ',total_events[0])

print('................................')
# Number of events by Task Category

count = df.groupby('Task Category').count()
events_by_category = count.iloc[:,0]

print(events_by_category)

print('....................................')
# logging start and end time 
# end_event_time = df.head(1)['Date and Time']
# start_event_time = df.tail(1)['Date and Time']
# Event times 
df = df.sort_values('Date and Time')
df = df.loc[:,['Event ID','Date and Time']]
# showing 10 events here with time
df = df.head(10)
print(df)

# saving the result into another csv file
df = df.to_csv('result.csv')

