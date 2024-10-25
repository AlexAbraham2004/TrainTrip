import pandas as pd

# Load the static GTFS data files
agency_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/agency.txt')
calendar_dates_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/calendar_dates.txt')
feed_info_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/feed_info.txt')
routes_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/routes.txt')
shapes_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/shapes.txt')
stops_times_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/stop_times.txt')
stops_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/stops.txt')
transfers_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/transfers.txt')
trips_df = pd.read_csv('C:/Users/alexa/OneDrive/Documents/TrainTrip Project/GTFS Data/trips.txt')

print(agency_df.index(0))




    # DISPLAY THE DATA - #Their importance
    
# print(agency_df) #One line, LIRR Title w/ accompany information

# print(calendar_dates_df) #Specifies exceptions to the regular service calendar (like holidays).

# print("Feed infor", feed_info_df) #One line, LIRR Title w/ accompany information

# print(routes_df)    #All branches with specific color, text-color, and route_id

# print(shapes_df)    #Describes the geometric shapes of the routes, usually as a series of latitude/longitude points.

# print(stops_times_df) #Contains information about the stop times for each trip, including arrival and departure times.

# print(stops_df)   #Lists all the stops in the system, including stop IDs, names, and geographic coordinates

# print(transfers_df) #Indicates transfer points between different routes.

# print(trips_df) #Contains information about each trip, including route IDs, service IDs, and trip IDs.