from contextlib import redirect_stderr
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import pandas as pd
import csv

app = FastAPI()

# Migrate tickers for each sector
sp500 = pd.read_json(open('tickers/sp500.json'))[0]
tech = pd.read_json(open('tickers/tech.json'))[0]
utilities = pd.read_json(open('tickers/utilities.json'))[0]
real_estate = pd.read_json(open('tickers/real_estate.json'))[0]
industrials = pd.read_json(open('tickers/industrials.json'))[0]
healthcare = pd.read_json(open('tickers/healthcare.json'))[0]
financials = pd.read_json(open('tickers/financials.json'))[0]
energy = pd.read_json(open('tickers/energy.json'))[0]
consumer_defensive = pd.read_json(open('tickers/consumer_defensive.json'))[0]
consumer_cyclical = pd.read_json(open('tickers/consumer_cyclical.json'))[0]
basic_materials = pd.read_json(open('tickers/financials.json'))[0]
communication_services = pd.read_json(
    open('tickers/communication_services.json'))[0]
stock_sectors = pd.read_json(open('tickers/sectors.json'))[0]


tickers = {
    "sp500": sp500,
    "technology": tech,
    "utilities": utilities,
    "real-estate": real_estate,
    "industrials": industrials,
    "healthcare": healthcare,
    "financials": financials,
    "energy": energy,
    "consumer-defensive": consumer_defensive,
    "consumer-cyclical": consumer_cyclical,
    "communication-services": communication_services,
    "basic-materials": basic_materials
}


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
            
        </head>
       
        <body>
            <div>
                <h3>Oops Index route is not responding</h3>
                <p>blah</p>
                <a href="https://cash.app/bitcoin">A Story</a>
            </div>
        </body>
    </html>
    """


@app.get("/sectors")
def sectors():
    return stock_sectors


@app.get("/{sector_id}")
def get_ticker(sector_id: str):
    return tickers[sector_id]
