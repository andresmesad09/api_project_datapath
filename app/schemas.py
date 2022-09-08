from pydantic import BaseModel
import pandas as pd


class PostResponse(BaseModel):
    df: pd.DataFrame

    # to read it even if it's not a dict
    class Config:
        arbitrary_types_allowed = True
