import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Data/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Convert the query results to a Dictionary using date as the key and prcp as the value.
    # Return the JSON representation of your dictionary.

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return date as the key and prcp as the value"""
    # Query all precipitation
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from date as the key and prcp as the value append to a list of precip
    prcp_list = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_list.append(prcp_dict)

    return jsonify(prcp_list)



@app.route("/api/v1.0/stations")
def stations():
    # Return a JSON list of stations from the dataset
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations from the dataset"""
    # Query all stations
    results = session.query(Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    station_names = list(np.ravel(results))

    return jsonify(station_names)



@app.route("/api/v1.0/tobs")
def tobs():
    # query for the dates and temperature observations from a year from the last data point.
    # Return a JSON list of Temperature Observations (tobs) for the previous year.
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tobs from a year from the last data point"""
    # Query tobs
    results = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
        order_by(Measurement.date.desc()).limit(365).all()

    session.close()

    # Convert list of tuples into normal list
    tobs_list = list(np.ravel(results))

    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def tobs_calc_start(start):
    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a 
    #   given start or start-end range.
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date"""
    # Query tobs
    result_min = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    result_avg = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
  
    result_max = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    session.close()

 
    return jsonify(f"min: {result_min}, avg: {result_avg}, max: {result_max}")


@app.route("/api/v1.0/<start>/<end>")
def tobs_calc_start_end(start, end):
    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a 
    #   given start-end range
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between 
    #   the start and end date inclusive
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date"""
    # Query tobs
    result_min = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date<=end).all()
        
    result_avg = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date<=end).all()

    result_max = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date<=end).all()

    session.close()

 
    return jsonify(f"min: {result_min}, avg: {result_avg}, max: {result_max}")



if __name__ == '__main__':
    app.run(debug=True)