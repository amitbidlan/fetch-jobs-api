from get_codes import GetCodes
from lcb_value import LCB_Value
from sc_value import SC_Value
from beforelcb import BeforeLCB
from get_occupation import GetOccupation
from get_job_code import GetJobCode
import logging
class GenerateUrl:
    logging.basicConfig(level=logging.DEBUG) 
    def __init__(self):
        # Create instances of helper classes to use their methods
        self.get_codes_instance = GetCodes()
        self.lcb_value_instance = LCB_Value()
        self.sc_value_instance = SC_Value()
        self.before_lcb_instance = BeforeLCB()
    def generate_url(self, state_name, nearest_station, occupation, employment_status, free_word, language):
        matching_station_codes = self.get_codes_instance.getEndPoint(nearest_station, state_name)

        # Create search URL based on retrieved station codes
        if matching_station_codes:
            lcb_value = self.lcb_value_instance.extract_lcb_substring(matching_station_codes[0])
            #sc_value = self.sc_value_instance.extract_value_by_index(matching_station_codes[0])
            front_end_point = BeforeLCB.get_text_before_last_slash(matching_station_codes[0])
            occupation_code = GetOccupation.get_occulation(occupation)
            job_code = GetJobCode.getJobCode(employment_status)
            #logging.debug(lcb_value,sc_value)
            # Generate the search URL with extracted values
            #https://townwork-net.translate.goog/shizuoka/ct_ma60000/tw_sa99127/sc_st04661/jc_021/emc_07/?lcb=320112&_x_tr_sl=ja&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp
            search_url = f"https://townwork-net.translate.goog{front_end_point}/{occupation_code}/{job_code}/?lcb={lcb_value}&ds=03&_x_tr_sl=ja&_x_tr_tl={language}&_x_tr_hl=en&_x_tr_pto=wapp"
            #logging.debug(search_url)
            print(search_url)
            return search_url
        
        else:
            
            raise Exception(f"No matching station codes found for state '{state_name}' and nearest station '{nearest_station}'")
            
        

#state_name = "aichi"
#nearest_station = "Shimizu Station"
#occupation = "Dining/food service"
#employment_status = "full-time employee"
#free_word = "Python"

#generate_url = GenerateUrl()
#generate_url.generate_url(state_name,nearest_station,occupation,employment_status,free_word,language="hi")
