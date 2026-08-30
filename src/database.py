from src.config import DB_PATH
import duckdb
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

from pathlib import Path

# print(Path.cwd(), "\n")
# print(DB_PATH, "\n")
# print(DB_PATH.resolve())

def init_database():
    """
    Если будет ошибка, то finally гарантирует закрытие соединения в любом случае.
    id INTEGER PRIMARY KEY - вариант для контроля дубликатов id сообщений
    """

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = duckdb.connect(str(DB_PATH))

    # TODO Однократное удаление БД
    # conn.execute("""
    # DROP TABLE metadata;
    # """)

    try:
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS metadata (
                        id INTEGER,
                        message_date DATE,
                        grade VARCHAR,
                        vacancy_name VARCHAR,
                        location VARCHAR,
                        channel_name VARCHAR,
                        channel_link VARCHAR,
                        PRIMARY KEY (channel_link, id)
                    )
                """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_metadata_id
            ON metadata(id)
        """)



    finally:
        conn.close()

def save_into_database(metadata):
    """
    ON CONFLICT (id) DO NOTHING - вариант для отказ записи Дубликата
    Перед заполнением таблицы очищаем данные
    """
    conn = duckdb.connect(str(DB_PATH))

    try:
        conn.execute("""
        TRUNCATE TABLE metadata;
        """)
        for content in metadata.values():
            conn.execute("""
                    INSERT INTO metadata
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT (channel_link, id) DO NOTHING
                """, (
                content.id,
                content.message_date,
                content.grade,
                content.vacancy_name,
                content.location,
                content.channel_name,
                content.channel_link,
            ))

    finally:
        conn.close()

def table_data():
    """
    Три варианта вывода таблицы
    """

    conn = duckdb.connect(str(DB_PATH))

    # TODO Вариант 1
    # table = conn.execute("""
    #     select *
    #     from metadata
    # """).fetchall()

    # print(table)

    # TODO Вариант 2

    table = conn.sql("""
        SELECT *
        FROM metadata
        where message_date >= CURRENT_DATE - INTERVAL '2 months'
        order by message_date
    """)

    print(table.show(max_rows=1000))

    # TODO Вариант 3

    # table = conn.execute("""
    #         SELECT *
    #         FROM metadata
    #     """).fetchdf()
    #
    # print(table)

    # TODO Вариант 4
    # pd.set_option('display.max_columns', None)
    #
    # df_mdata = pd.DataFrame(table.show(max_rows=1000), columns=table.columns)
    #
    # print(df_mdata)

    # TODO Проверка типа даты
    # typed = conn.sql("""
    #    SELECT pg_typeof(message_date)
    #    FROM metadata
    #    """)
    # print(typed)

    conn.close()
    # return table
