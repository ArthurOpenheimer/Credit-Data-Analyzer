from sqlalchemy import create_engine
import pandas as pd
import config

def get_engine():
    return create_engine(
        f"mysql+mysqlconnector://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@localhost:3307/{config.MYSQL_DATABASE}"
    )

def load_data():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM germancredit", engine)
    engine.dispose()
    return df