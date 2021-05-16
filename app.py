import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station


app = Flask(__name__)


@app.route("/")
def welcome():
    return (
        f"Welcome<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date > '2016-08-23').all()

    prcp_data = results
    return jsonify(prcp_data)


@app.route("/api/v1.0/stations")
def stations():

    session = Session(engine)

    results = session.query(Station.station).all()

    all_stations = results

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)

    results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date > '2016-08-23').\
            filter(Measurement.station == 'USC00519281').all()

    temp_data = results
    return jsonify(temp_data)


if __name__ == '__main__':
    app.run()
