import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask, jsonify
import datetime
from datetime import timedelta
import json
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():
    year = timedelta(days=365)
    one_year_tobs=session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > (datetime.datetime.today()-year)).all()
    return jsonify(dict(one_year_tobs))

@app.route("/api/v1.0/stations")
def stations():
    row=session.query(Station.station, Station.name).all()
    return jsonify(row)

@app.route("/api/v1.0/tobs")

def tobs():
    year = timedelta(days=365)
    one_year_tobs=session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > (datetime.datetime.today()-year)).all()
    return jsonify(one_year_tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    fifteen_days = timedelta(days=15)
    end_date = start_date + fifteen_days
    start_month_day = str(start_date.month)+"-"+str(start_date.day)
    end_month_day = str(end_date.month)+"-"+str(end_date.day)
  
    results = session.query(func.strftime("%m-%d", Measurement.date), Measurement.tobs).all()

    date1=[]
    tobs1=[]
    for row in results:
        date1.append(row[0])
        tobs1.append(row[1])
    tobs_df=pd.DataFrame({"date":date1,"tobs":tobs1})
    tobs_df=tobs_df[(tobs_df['date'] >= start_month_day) & (tobs_df['date'] <= end_month_day)]

    TMIN=tobs_df['tobs'].min()
    TMAX=tobs_df['tobs'].max()
    TAVG=tobs_df['tobs'].mean()

    tobs_dict={}
    tobs_dict["TMIN"] = int(TMIN)
    tobs_dict["TMAX"] = int(TMAX)
    tobs_dict["TAVG"] = TAVG
    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    start_month_day = str(start_date.month)+"-"+str(start_date.day)
    end_month_day = str(end_date.month)+"-"+str(end_date.day)
    results = session.query(func.strftime("%m-%d", Measurement.date), Measurement.tobs).all()
    date1=[]
    tobs1=[]
    for row in results:
        date1.append(row[0])
        tobs1.append(row[1])
    tobs_df=pd.DataFrame({"date":date1,"tobs":tobs1})
    tobs_df=tobs_df[(tobs_df['date'] >= start_month_day) & (tobs_df['date'] <= end_month_day)]
    TMIN=tobs_df['tobs'].min()
    TMAX=tobs_df['tobs'].max()
    TAVG=tobs_df['tobs'].mean()
    tobs_dict={"TMIN":int(TMIN), "TMAX": int(TMAX), "TAVG": TAVG}
    return jsonify(tobs_dict)

if __name__ == "__main__":
    app.run(debug=True)  
