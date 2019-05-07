# A nowcasting model for Medellin city

In this repository we present the first steps of a nowcasting methodology for the Medell\'{i}n unemployment rate by
using time-series regression to identify the generating process of the series and object detection to identify
several categories of automobiles in images, in order to follow a first step to prove the hypothesis of how well
the traffic of the city can reflect the employment, or in general, the economic activity inside it. 

Two models were evaluated: 
* SARIMA model to forecast the unemployment rate using historical data, the code can be found in the notebook: Time Series analysis for the Unemployment rate
* Single-Shot Detector, trained to detect 8 classes of vehicles in CCTV traffic cameras installed in Medell\'{i}n. The training can be found in the training notebook.

## Set up conda enviroment
0. Install Anaconda or Miniconda (See [this installation guide](https://conda.io/docs/user-guide/install/index.html))
1. Create an environment:
```
$ conda env create -f environment.yml
```
2. Activate the new environment:
```
$ source activate RiSE-mvasqu49
```
3. Let's play
```
$ jupyter notebook training.ipynb
```
Once you have installed the environment, you will be able to use allthe resources for this repository.

## Built With

* [Python 3.7](https://www.python.org/) - Time Series analysis, Fourier Analysis. 
* [TensorFlow](https://www.tensorflow.org/) - Deep learning framework by Google.
* [Object detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) - Framework built in Tensorflow.

## Authors

* **María Camila Vásquez Correa** - *Initial work* - [camivasz](https://github.com/camivasz).
* **RiSE group** - *Advisory* - [RiSE group](https://github.com/Rise-group)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* [Metrics for object detection](https://github.com/rafaelpadilla/Object-Detection-Metrics).
* [Training framework](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10).
* [Image augmentation](https://github.com/aleju/imgaug).
