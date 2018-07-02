
from flask import Flask, render_template, jsonify, redirect
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# create flask instance 
app = Flask(__name__)

# Create engine using the `sqlite`
engine = create_engine('sqlite:///belly_button_biodiversity.sqlite', echo=False)
Base = automap_base()

# Use the Base class to reflect the database tables# Use t 
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
Otu_id = Base.classes.otu
name = Base.classes.samples
sample_metaData = Base.classes.samples_metadata

session = Session(engine)

#  create route to render index.html template
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

#  create route to return list of sample names
@app.route('/names', methods=['POST','GET'])
def names():

    samples_cols_list = Base.classes.samples.__table__.columns.keys()
    sample_list = samples_cols_list[1:]
    return jsonify(sample_list)

# create route to return otu for a sample
@app.route('/otu', methods=['POST','GET'])
def otu():
    otu_desc = session.query(Otu_id.lowest_taxonomic_unit_found).all()
    otu_descriptions = [i[0] for i in otu_desc]
    return jsonify(otu_descriptions)

# create route to return MetaData for a sample
@app.route('/metadata/<sample>')
def metadata(sample):
    sample_number = sample.split('_')
    sample_data = session.query(sample_metaData).filter(sample_metaData.SAMPLEID == sample_number).all()
    sample_details = {}
    for each in sample_data:
        sample_details['AGE'] = each.AGE
        sample_details['BBTYPE'] = each.BBTYPE
        sample_details['ETHNICITY'] = each.ETHNICITY
        sample_details['GENDER'] = each.GENDER
        sample_details['LOCATION'] = each.LOCATION
        sample_details['SAMPLEID'] = each.SAMPLEID
    return jsonify(sample_details)    

@app.route('/wfreq/<sample>')
def washing_freq(sample):
    sample_number = sample.split('_')
    washing_freq = session.query(sample_metaData.WFREQ).filter(sample_metaData.SAMPLEID == sample_number).all()
    return jsonify(washing_freq )


if __name__ == '__main__':
    app.run()    
