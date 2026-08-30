from extractor import client, extract_messages, comparison
from database import init_database, save_into_database, table_data
from src.config import CHANNELS
from metadata import metadata_from_messages
import asyncio
async def main():
    init_database()

    await client.start()

    me = await client.get_me()

    print(f"Подключение успешно.")
    print(f"Имя: {me.first_name}")
    print(f"ID: {me.id}")

    num_msg = 0
    dict_mdata = {}  # Словарь Для последней строки
    # metadata_list = []
    for chanel_name, chanel_link in CHANNELS.items():
        print(f"{chanel_name} : {chanel_link}")

        # Вызов генератора
        async for message in extract_messages(chanel_link):
            num_msg += 1
            # print(message)

            if isinstance(message.text, str):
                # print(message.date.date())
                texts = message.text.lower().split()

                # Сохраняем две даты для вывода в строчном формате и для метадаты для в питоновском datetime.datetime
                # date_temporary = message.date.date().strftime('%Y-%m-%d')

                date_metadata = message.date
                for word_text in texts:
                    word_list = re.findall(r"\w+", word_text)

                    for words in word_list:

                        compar = comparison(message.id, words, date_metadata)

                        if compar:
                            # dict_mdata[message.id] = compar
                            #
                            # print(dict_mdata[message.id])
                            # print(compar)

                            dict_mdata[message.id] = metadata_from_messages(message.id, compar, chanel_name, chanel_link)

                            # if metadt:

                            # metadata_list.append(metadt)




            else:
                print(" No messages")

    # print(dict_mdata)

    await client.disconnect()

    save_into_database(dict_mdata)

    table_data()

    return dict_mdata


if __name__ == "__main__":
    # main()
    asyncio.run(main())