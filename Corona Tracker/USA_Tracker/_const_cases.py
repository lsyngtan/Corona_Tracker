# WORLD CASES CONSTANTS
country = 0
w_total_cases = 1
w_new_cases = 2
w_total_deaths = 3
w_new_deaths = 4
w_total_recovered = 5
w_active_cases = 6
w_serious_critical = 7
w_tot_cases_M = 8
w_deaths_M = 9
w_total_tests = 10
w_tests_M = 11

# USA CASES CONSTANTS
usa_state = 0
usa_total_cases = 1
usa_new_cases = 2
usa_total_deaths = 3
usa_new_deaths = 4
usa_active_cases = 5
usa_tot_cases_M = 6
usa_deaths_M = 7
usa_total_tests = 8
usa_tests_M = 9

# JSON CONSTANTS
COUNTRY_OTHER = 'Country'
USA_STATE = 'USA States'
TOTAL_CASES = 'Total Cases'
NEW_CASES = 'New Cases'
TOTAL_DEATHS = 'Total Deaths'
NEW_DEATHS = 'New Deaths'
TOTAL_RECOVERED = 'Total Recovered'
ACTIVE_CASES = 'Active Cases'
SERIOUS_CRITICAL = 'Serious Critical'
TOT_CASES_M = 'Total Cases per Million'
DEATHS_M = 'Deaths per Million'
TOTAL_TESTS = 'Total Tests'
TESTS_M = 'Tests per Million'

# EXTRA JSON CONSTANTS
TOTAL_CASES_PERCENT = 'Total Cases %'
NEW_CASES_PERCENT = 'New Cases %'
TOTAL_DEATHS_PERCENT = 'Total Deaths %'
NEW_DEATHS_PERCENT = 'New Deaths %'
TOTAL_RECOVERED_PERCENT = 'Total Recovered %'
ACTIVE_CASES_PERCENT = 'Active Cases %'
SERIOUS_CRITICAL_PERCENT = 'Serious Critical %'

def get_sensor(id, value, type=None, unit=None, prefix=None, dt=None):
    sensor = {
        'id': id,
        'data': value
    }
    return sensor

def get_percentage(str_num, str_dem):
    if str_dem == '0':
        return '0'
    return str(int(float(str_num) / float(str_dem) * 100))