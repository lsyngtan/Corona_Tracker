from bs4 import BeautifulSoup as bf
import requests
import _const_cases as const

num_places = 220 #number of countries

def getting_world_value(today): #getting the value from website
    data_list = []
    html = requests.get("https://www.worldometers.info/coronavirus")
    soup = bf(html.text,'html.parser')
    if today:
        tag = soup("tr")[9:9 + num_places]
    else:
        tag = soup("tr")[239:239 + num_places]

    def extract_vals(arr):
        temp_list = []
        arr_size = len(arr) - 2
        for j in range(arr_size):
            if j == 1:
                temp_list.append(arr.contents[j].contents[0].contents[0])
            elif j % 2 == 1:
                value = arr.contents[j].contents
                if len(value) == 0:
                    value.append('0')
                value = value[0]
                value = value.replace("\n", "")
                value = value.replace("+", "")
                value = value.replace(",", "")
                value = value.replace("N/A", "")
                if len(value) == 0 or value == ' ':
                    value = '0'
                temp_list.append(value)
        return temp_list  
          
    compare_list = extract_vals(tag[-1])

    for i in range(len(tag)):        
        insert_list = extract_vals(tag[i])

        def continents(arg, day):
            if day:
                switcher = { 
                    212: 'North America', 
                    213: 'Europe', 
                    214: 'Asia',  
                    215: 'South America', 
                    216: 'Oceania', 
                    217: 'Africa', 
                    218: 'Unknown',
                    219: 'World',
                } 
            else:
                switcher = { 
                    211: 'Asia', 
                    212: 'North America', 
                    213: 'Europe',  
                    214: 'South America', 
                    215: 'Oceania', 
                    216: 'Africa', 
                    217: 'Unknown',
                    218: 'World'
                }
            return switcher.get(arg, insert_list[const.country])
        
        data_name = continents(i, today)
        data = {
            const.TOTAL_CASES : insert_list[const.w_total_cases],
            const.NEW_CASES : insert_list[const.w_new_cases],
            const.TOTAL_DEATHS : insert_list[const.w_total_deaths],
            const.NEW_DEATHS : insert_list[const.w_new_deaths],
            const.TOTAL_RECOVERED : insert_list[const.w_total_recovered],
            const.ACTIVE_CASES : insert_list[const.w_active_cases],
            const.SERIOUS_CRITICAL : insert_list[const.w_serious_critical],
            const.TOT_CASES_M : insert_list[const.w_tot_cases_M],
            const.DEATHS_M : insert_list[const.w_deaths_M],
            const.TOTAL_TESTS : insert_list[const.w_total_tests],
            const.TESTS_M : insert_list[const.w_tests_M],
            const.TOTAL_CASES_PERCENT : const.get_percentage(insert_list[const.w_total_cases],compare_list[const.w_total_cases]),
            const.NEW_CASES_PERCENT : const.get_percentage(insert_list[const.w_new_cases],compare_list[const.w_new_cases]),
            const.TOTAL_DEATHS_PERCENT : const.get_percentage(insert_list[const.w_total_deaths],compare_list[const.w_total_deaths]),
            const.NEW_DEATHS_PERCENT : const.get_percentage(insert_list[const.w_new_deaths],compare_list[const.w_new_deaths]),
            const.TOTAL_RECOVERED_PERCENT : const.get_percentage(insert_list[const.w_total_recovered],compare_list[const.w_total_recovered]),
            const.ACTIVE_CASES_PERCENT : const.get_percentage(insert_list[const.w_active_cases],compare_list[const.w_active_cases]),
            const.SERIOUS_CRITICAL_PERCENT : const.get_percentage(insert_list[const.w_serious_critical],compare_list[const.w_serious_critical]),
            const.DEATHS_VS_CASES : const.get_percentage(insert_list[const.w_total_deaths],insert_list[const.w_total_cases]),
            const.RECOVERED_VS_CASES : const.get_percentage(insert_list[const.w_total_recovered], insert_list[const.w_total_cases])
        }
        data_list.append(const.get_sensor(data_name, data))
    return data_list