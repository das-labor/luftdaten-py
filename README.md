### Prerequisites

- Setup a virtual environment folder `env` with virtualenv
`virtualenv -p python3 env`
- Source the virtual environment via:
`source env/bin/activate`
- Install the required packages via `pip`
`pip install -r requirements.txt`
- If you want to speed up the processing by ~50%, install pypy3 and make sure its on the PATH.


### Run dvc pipeline

Running
```
dvc repro evaluation/sensor_data_dortmund.dvc
```
will create `data/sensor_2019-12_dortmund.csv`.
