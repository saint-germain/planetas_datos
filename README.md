# README #

Repositorio para datos del proyecto PACA de síntesis planetaria

## General use 

The following sections explain how to use the scripts for processing simulation data.

### If using repo locally

- Clone this repo (planetas_data)
- Choose a .zip (say `properyam.zip`) that is already in the repo (and was added after 11-04-17, older .zip files might not be complete for the pipeline to work properly)
- Use a py27 environment (I know, I know)
- Type in your terminal `sh pipeline.sh properyam` or whatever your .zip filename prefix is. Note: do not include the .zip portion.
- Your processed data and simulation info is now in the `/properyam/` folder (or whatever the name of your .zip filename prefix is).
- Raw data will be in finalresults.csv (containing info on all the planets).


| Column Name   | Meaning       | Importance (*)  |
| ------------- |:-------------:| :-----:|
| ident     	| unique system identifier | high |
| it   			| iteration index      |   none |
| t 			| simulation time (yr)      | low    |
| a(i)			| planet semi-major axis (AU)| high		|
| emegas(i)		| planet gas mass (M_earth) | medium |
| emepla(i)/emet| planet solid mass (M_earth)| high |
| rplanet(i)/radtie| planet solid radius | low |
| emestar		| stellar mass (g) | high |
| rc            | disk outer cutoff radius (AU) | high |
| qest | Toomre Q at min radius | none |
| sigmag_0 | maximum dust surface density (g/cm^3) | high |
| emed | disk mass (M_sun) | high |
| gama | surface density power law exponent | none |
| apert | perturbation amplitude | high|
| fpert | perturbation length scale | none |
| constmigI | type I migration rate | none |
| emetal | metallicity wrt solar | high |
| taugas | gas dissipation timescale (yr) | high | 

(*) For data in filtered.zip, the master distributions are:
![](distributions.png?raw=true)

- Reduced data (containing consolidated info on each system) will be in terrestrial.txt and giant.txt. The corresponding header is in header.txt. This format is not ideal but it was requested by my student.

## Specific use - Analysis tools

- `quality.py` creates some diagnostic .txt files. It is meant to be used as `python quality.py createdfiles.txt totalsims.txt finished.txt` within a folder that also contains the `results/` folder. Part of this code can be played with in `parallel_sandbox.ipynb`.
- `reduce.py` is meant to be used with `finalresults.csv` files created by `pipeline.sh`. This python script creates two data files, `terrestrial.txt` and `giant.txt`, and a header .txt file. The data files contain Center of Mass, Number of Planets, Mass budget for planets, Mass efficiency (mass budget/disk mass), Sigmag0 (maximum solid surface density), Disk Mass, Characteristic radius, Stellar Mass information for each simulation. `terrestrial.txt` has this information for planets below 10 earth masses, and `giant.txt` for planets above 10 earth masses. It should be used as `reduce.py finalresults.csv`. Part of this  code can be played with in `planets_sandbox.ipynb`. Output file column information is in `header.txt`.

https://arxiv.org/pdf/1106.3281.pdf
https://arxiv.org/pdf/1112.2349.pdf
