import COVID19Py

covid19 = COVID19Py.COVID19()

def getcorona(country):
    final_message = ""
    get_message_bot = country
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевшие: </b>{location['confirmed']}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgT1-A4QeHcYRTjLeh7Q35tkpYaU2IAAIZBgACu-LZS7x-ZyzJUUkPGwQ')
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"

    return final_message