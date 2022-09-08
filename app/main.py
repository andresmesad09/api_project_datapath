from fastapi import FastAPI, Response, HTTPException, status
from .database import Database


# uncomment these two line topopulate the database with the files again
# from .etl import populate_tables_with_csv
# populate_tables_with_csv()
db = Database()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello API world"}

# ref: https://stackoverflow.com/questions/71203579/how-to-return-a-csv-file-pandas-dataframe-in-json-format-using-fastapi   # noqa: E501


@app.get("/analytics/income_by_department")
async def get_income_by_department():
    result = db.income_by_department()
    return Response(result, media_type="application/json")


@app.get("/analytics/top_categories")
async def get_top_categories():
    try:
        result = db.top_categories()
        return Response(result, media_type="application/json")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Working on getting the top categories")


@app.get("/analytics/top_clients")
async def get_top_clients():
    try:
        result = db.top_clients()
        return Response(result, media_type="application/json")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Working on getting the top clients")


@app.get("/analytics/top_products")
async def get_top_products():
    try:
        result = db.top_products()
        return Response(result, media_type="application/json")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Working on getting the top products")


@app.get("/analytics/top_fraud")
async def get_top_fraud():
    try:
        result = db.top_fraud()
        return Response(result, media_type="application/json")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Working on getting the top frauds")

# ----
# CRUD
# ----
