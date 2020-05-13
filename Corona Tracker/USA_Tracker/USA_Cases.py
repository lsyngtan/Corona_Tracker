from bs4 import BeautifulSoup as bf
import requests
import _const_cases as const

num_places = 52 #number of states

def getting_usa_value(): #getting the value from website
    data_list = []
    html = requests.get("https://www.worldometers.info/coronavirus/country/us/")
    soup = bf(html.text,'html.parser')
    tag = soup("tr")[1:1 + num_places]

    def extract_vals(arr):
        temp_list = []
        arr_size = len(arr) - 2
        for j in range(arr_size):
            if j % 2 == 1:
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

    compare_list = extract_vals(tag[0])

    for i in range(len(tag)):
        insert_list = extract_vals(tag[i])

        data_name = insert_list[const.usa_state]
        data = {
            const.TOTAL_CASES : insert_list[const.usa_total_cases],
            const.NEW_CASES : insert_list[const.usa_new_cases],
            const.TOTAL_DEATHS : insert_list[const.usa_total_deaths],
            const.NEW_DEATHS : insert_list[const.usa_new_deaths],
            const.ACTIVE_CASES : insert_list[const.usa_active_cases],
            const.TOT_CASES_M : insert_list[const.usa_tot_cases_M],
            const.DEATHS_M : insert_list[const.usa_deaths_M],
            const.TOTAL_TESTS : insert_list[const.usa_total_tests],
            const.TESTS_M : insert_list[const.usa_tests_M],
            const.TOTAL_CASES_PERCENT : const.get_percentage(insert_list[const.usa_total_cases],compare_list[const.usa_total_cases]),
            const.NEW_CASES_PERCENT : const.get_percentage(insert_list[const.usa_new_cases],compare_list[const.usa_new_cases]),
            const.TOTAL_DEATHS_PERCENT : const.get_percentage(insert_list[const.usa_total_deaths],compare_list[const.usa_total_deaths]),
            const.NEW_DEATHS_PERCENT : const.get_percentage(insert_list[const.usa_new_deaths],compare_list[const.usa_new_deaths]),
            const.ACTIVE_CASES_PERCENT : const.get_percentage(insert_list[const.usa_active_cases],compare_list[const.usa_active_cases])
        }
        data_list.append(const.get_sensor(data_name, data))
    return data_list