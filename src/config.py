import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

print(API_ID, "<<<<<<<<<<<<<<<")

CHANNELS = {
    # "Мой канал": "@Kirill_50plus_DS",
    # "Тёмная Башня": "@tbaudiobook",
    "Работа и вакансии в IT": "@proglib_jobs",
    "Доска AI-объявлений": "@DS_avitotech",
    "Вакансии ИТ": "@prog_itjobs",
    "Machine Learning Jobs": "@Machinelearning_Jobs",
    "Data Science Jobs": "@datascienceml_jobs",
    "ML & Data Science Jobs": "https://t.me/+dJGMlUsazwU4NGRi",
    "Data jobs": "@datajob",
    "ML / DS_Jobs": "@ml_data_science_job",
    "Data Analyst/Science Jobs": "@data_analyst_science_jobs",
    "Data science: Remote job of the day": "@data_science_remote_jobs",
    "Data Science jobs": "https://t.me/datascience_job",
    "getmatch": "https://t.me/g_jobbot",
    "Python Django Jobs": "@python_django_work",
    "Python Jobs": "@python_djangojobs",
    "Ит Вакансии ": "@hr_itwork",
    "fFinder1": "@theyseeku",
    "fFinder2": "@finder",
    "fFinder3": "@finderwork"

}

PREF_METADATA = {
    'VACANCY_NAME': ["datanalyst", "analys", "datas", "scientist", "data scientist", "аналит", "разраб"],
    'GRADE': [
        "jun",
        "intern",
        "стаже",
        "стажё",
        # "middle",
        "стажир"
    ]
    , 'LOCATION': [
        "удалён",
        "remote",
        "удален"
    ]
    , 'CHANNEL_NAME': []
    , 'MESSAGE_DATE': []
    , "ID": []

}

SESSION_NAME = "vacancy_parser"

# DB_PATH = Path("data/metadata.duckdb")
DB_PATH = Path("C:/Users/Kirill/PycharmProjects/tg_vacancy_parser/data/metadata.duckdb")

