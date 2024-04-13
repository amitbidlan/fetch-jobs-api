# Import the EndPointDB class from the end_point_database module
from end_point_database import EndPointDB
import re
import removeParenthesis 
import logging
class GetCodes:
    #logging.basicConfig(level=logging.DEBUG) 
    def getEndPoint(self, station_name, state_name):
        # Create an instance of the EndPointDB class
        end_point_db_instance = EndPointDB()
        
        # Get the station code end point map
        end_point_map = end_point_db_instance.station_code_end_point_map
        
        # Retrieve the state map based on the provided state name (convert to lowercase)
        #state_map = end_point_map.get(state_name.lower())  # Use lower case for state name

        # Array to store matching station codes
        matching_station_codes = []

        # Check if the state map exists
        if end_point_map:
            # Iterate over railway companies and their lines within the state map
            for railway_company, lines in end_point_map.items():
                for line_name, stations in lines.items():
                    for station, station_info in stations.items():
                        changed_station = removeParenthesis.RemoveParenthesis.ignore_text_in_parentheses(station)
                        #print(changed_station, station_name)
                        #logging.debug(changed_station)
                        if changed_station == station_name:
                            matching_station_codes.append(station_info)
                            #print(matching_station_codes)
        else:
            print("State map not found for the provided state name:", state_name)

        return matching_station_codes

#get_codes = GetCodes().getEndPoint('Shimizu Station','aichi')
#print(get_codes)