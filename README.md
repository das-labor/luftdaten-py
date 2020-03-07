### Prerequisites

- Setup a virtual environment folder `env` with virtualenv
`virtualenv -p python3 env`
- Source the virtual environment via:
`source env/bin/activate`
- Install the required packages via `pip`
`pip install -r requirements.txt`


### Run dvc pipeline

```
dvc repro evaluation/sensor_data_dortmund.dvc
```
