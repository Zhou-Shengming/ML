# ML
## About ML

ML:prediction of the vacancy formation energy of metallic vanadium.

The SPREAD models is available in `ML.m`. The prediction code can be found in `SPREAD.py`.

### Requirements:

- python 3.7
- numpy==1.18.0
- scikit-learn==0.22.1
- joblib==1.0.1

# Usage
## parameters

'--number'         The number of atoms missing from the vacancy.

'--surface_area'   Wiger-Seitz primary cell surface area.

'--output'         Save the prediction results.The default value is 'output.txt'.

## example
```
python ML.py --number 26 --surface_area 37.93 --output result.txt
```
