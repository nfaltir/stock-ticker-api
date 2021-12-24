import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import csv

app = FastAPI()

#Migrate tickers for each sector
sp500 = pd.read_json(open('tickers/sp500.json'))[0]
tech = pd.read_json(open('tickers/tech.json'))[0]
utilities = pd.read_json(open('tickers/utils.json'))[0]
real_estate = pd.read_json(open('tickers/real_estate.json'))[0]
industrials = pd.read_json(open('tickers/industrials.json'))[0]
healthcare = pd.read_json(open('tickers/healthcare.json'))[0]
financials = pd.read_json(open('tickers/financials.json'))[0]
energy = pd.read_json(open('tickers/energy.json'))[0]
consumer_defensive = pd.read_json(open('tickers/consumer_defensive.json'))[0]
consumer_cyclical = pd.read_json(open('tickers/consumer_cyclical.json'))[0]
basic_materials = pd.read_json(open('tickers/financials.json'))[0]
communication_services = pd.read_json(open('tickers/communication_services.json'))[0]
stock_sectors = pd.read_json(open('tickers/sectors.json'))[0]

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

tickers = {
    "sp500":sp500,
    "technology":tech,
    "utilities": utilities,
    "real-estate":real_estate,
    "industrials":industrials,
    "healthcare":healthcare,
    "financials":financials,
    "energy": energy,
    "consumer-defensive": consumer_defensive,
    "consumer-cyclical":consumer_cyclical,
    "communication-services":communication_services,
    "basic-materials": basic_materials
}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/resource", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

@app.get("/sectors")
def sectors():
    return stock_sectors

@app.get("/get-tickers/{sector_id}")
def get_ticker(sector_id: str):
    return tickers[sector_id]

