from src.config import CHANNELS, SESSION_NAME, API_ID, API_HASH, PREF_METADATA
# print(CHANNELS)
from prefect import flow, task
from telethon import TelegramClient
from metadata import dict_metadata

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
)

@task(
    name="save metadata",
    retries=3,
    retry_delay_seconds=10,
    log_prints=True
)

async def extract_messages(chanel):
    """
    Ответ от источника надо ждать поэтому async
    """
    async for msg in client.iter_messages(chanel, limit=100, reverse=False):
        # print(msg)
        yield msg

def comparison(msg_id, word, meta_date):
    """
    * msg_id - нужен для группировки метадаты
    """
    for name_mdata, pref_total in PREF_METADATA.items():

        for pref in pref_total:

            # if name_mdata in ['CHANNEL_NAME', 'MESSAGE_DATE', 'RESUME_LINK']:

            if word.startswith(pref):
                value_metadata = word

                # d[msg_id][name_mdata].add(value_metadata)  # msg_id нужен для группировки метадаты

                dict_metadata.setdefault(msg_id, {}).setdefault('MESSAGE_DATE', meta_date.date().strftime("%Y-%m-%d"))

                dict_metadata[msg_id].update({name_mdata: value_metadata})

                if dict_metadata[msg_id].get("GRADE"):
                    # print(d[msg_id])
                    # metadt = metadata_messages(d, msg_id)

                    return dict_metadata[msg_id]