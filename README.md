### Prerequisites

- Setup a virtual environment folder `env` with virtualenv
`virtualenv -p python3 env`
- Source the virtual environment via:
`source env/bin/activate`
- Install the required packages via `pip`
`pip install -r requirements.txt`

For performance we'll use another Python interpreter for the second `dvc`
pipeline:

- Firstly check and install `pypy` with your package manager

- Setup a virtual environment `env_pypy` with virtualenv:
`virtualenv -p pypy3 env_pypy`


### Initial setup

- Initialise dvc. Usually this is already done in this repository
```
dvc init
```

- Import a new data source into dvc control:
```
dvc import-url http://archive.luftdaten.info/csv_per_month/2019-12/2019-12_sds011.zip data/
``` 

### Setup up and run dvc pipelines

Firstly:
- Download the city boundaries according to DE:regionalschluessel, here
    `059130000000`.  `.wkb` is a binary format. `.bounds` is a text format for
    the boundaries. For perfomance we'll use the `.bounds` later on with pypy
    instead of `.wkb` and shapely to perform the boundary check of sensors
    within the given shape 
```
dvc run -d evaluation/scripts/download_shape.py -o data/dortmund.wkb -o data/dortmund.bounds -f evaluation/download_shape_dortmund.dvc python evaluation/scripts/download_shape.py 059130000000 data/dortmund.wkb data/dortmund.bounds
```

Secondly:
- Filter the raw data, here the last full month of `sds011` particulate matter
    sensors which is version controlled by dvc, based on the city boundaries of
    interest, here the city of Dortmund. 

```
dvc run -d evaluation/scripts/geo_filter_zip2csv.py -d data/2019-12_sds011.zip -d data/dortmund.bounds -o data/sensor_2019-12_dortmund.csv -f evaluation/sensor_data_dortmund.dvc env_pypy/bin/python evaluation/scripts/geo_filter_zip2csv.py data/2019-12_sds011.zip data/sensor_2019-12_dortmund.csv data/dortmund.bounds
```


