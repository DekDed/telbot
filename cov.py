from covid19_data import JHU
import telebot

"""print("The number of COVID-19 recoveries in the US: " + str(JHU.US.recovered))
print("The number of confirmed COVID-19 cases in Texas: " + str(JHU.Texas.confirmed))
print("The number of COVID-19 deaths in California: " + str(JHU.California.deaths))
print("The number of worldwide COVID-19 deaths: " + str(JHU.Total.deaths))
print("The number of COVID-19 deaths in Russia: " + str(JHU.Russia.deaths))
print("The number of confirmed COVID-19 cases in Russia: " + str(JHU.Russia.confirmed))
print("The number of COVID-19 recoveries in the Russia: " + str(JHU.Russia.recovered))
print("The number of COVID-19 deaths in UK: " + str(JHU.UnitedKingdom.deaths))"""

def getcorona(country):
    final_message = ""
    get_message_bot = country
    if get_message_bot == "сша":
        final_message = "Данные по США: " + "\nЗаболевшие: " + str(JHU.US.confirmed) + "\nУмершие: " + str(JHU.US.deaths) + "\nВыздоровевшие: " + str(JHU.US.recovered)

    elif get_message_bot == "россия":
        final_message = "Данные по России: " + "\nЗаболевшие: " + str(JHU.Russia.confirmed) + "\nУмершие: " + str(JHU.Russia.deaths) + "\nВыздоровевшие: " + str(JHU.Russia.recovered)

    elif get_message_bot == "япония":
        final_message = "Данные по Японии: " + "\nЗаболевшие: " + str(JHU.Japan.confirmed) + "\nУмершие: " + str(JHU.Japan.deaths) + "\nВыздоровевшие: " + str(JHU.Japan.recovered)
        
    elif get_message_bot == "италия":
        final_message = "Данные по Италии: " + "\nЗаболевшие: " + str(JHU.Italy.confirmed) + "\nУмершие: " + str(JHU.Italy.deaths) + "\nВыздоровевшие: " + str(JHU.Italy.recovered)
    else:
        final_message = "Данные по всему миру: " "\nЗаболевшие: " + str(JHU.Total.confirmed) + "\nУмершие: " + str(JHU.Total.deaths) + "\nВыздоровевшие: " + str(JHU.Total.recovered)

    return final_message