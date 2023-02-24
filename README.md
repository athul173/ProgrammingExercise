# Accelerometer Autocalibration error correction

Python program on the derivation of correction factors for sensor axis-specific calibration error in Autocalibration of accelerometer data studies. (Details and outputs explained in the [solution document](https://github.com/athul173/ProgrammingExercise/blob/master/Solution%20documentation.pdf))

## Folder Structure
 - /
	 - -- `bin/`
	 - -- `Data/`: Contains the csv data file
		 - -- GT3X+ (01 day)RAW.csv
	 - -- `project/`: Contains the project program files including the main file
		 - -- `calculations/`: Folder containing all the methods used
			 - -- calculations.py
			 - -- calibration/
			 - -- methods.py
		 - -- `windows/`: Folder containing the sample threshold window calculations
			 - -- windows.py
		 - -- `main.py`: Main entry file
	 - requirements.txt
	 - pyvenv.cfg
	 - `Folder Structure.txt`: Explaining the folder structure
	 - `Solutions Documentation.pdf`: Solution document containing procedure, workflows, methods and plotted results
   
 ## Base dependencies
 - Scipy
 - Pyplot
 - numpy
 - pandas
