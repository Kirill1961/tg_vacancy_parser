from pydantic import BaseModel, ConfigDict

dict_metadata = {}

class MessageMetadata(BaseModel):
    """ Модель для таблицы метаданных.
        str | None = None   ---  это говорит что значение может быть строкой или None
    """
    model_config = ConfigDict(frozen=True)

    id: int
    message_date: str | None = None
    grade: str | None = None
    vacancy_name: str | None = None
    location: str | None = None
    channel_name: str | None = None
    channel_link: str | None = None

def metadata_from_messages(id, compar, chanel_name, chanel_link):
    # print(compar.get("VACANCY_NAME"))

    metadata = MessageMetadata(
        id=id
        , message_date=compar.get("MESSAGE_DATE")
        , grade=compar.get("GRADE")
        , vacancy_name=compar.get("VACANCY_NAME")
        , location=compar.get("LOCATION")
        , channel_name=chanel_name
        , channel_link=chanel_link
    )

    # print("METADATA:", metadata)

    return metadata