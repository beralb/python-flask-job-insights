<h1 align="left">Python/Flask Project - Job Insights</h1>
</br>

In this project we implement analyzes from a dataset about jobs. The implementations were incorporated into a web application developed with Flask (a very popular web framework in the Python community). We also had the opportunity to write tests for implementing a data analysis.

The data was extracted from the Glassdoor website and obtained through Kaggle, a platform that makes datasets available to data scientists.

Skills worked:

Using the Python interactive terminal.
Use of conditional and repeating structures.
Using built-in Python functions.
Implementation of exception handling.
File manipulation (Input/Output).
Function development.
Writing tests with Pytest.
Writing modules and importing them into other codes.

<h3>:gear: Instructions</h3>

------------

<p>To run the repository locally, clone the project and use the following commands to initialize Docker and install the dependencies:</p>

````
docker-compose up -d

python3 -m pip install -r dev-requirements.txt // to install the dependencies
docker-compose up -d // to execute the app 
in your favorite browser, go to address bar and navigate to address localhost:500 // to see html pages rendering the app
docker-compose down // to completely stop the application
````

<h3>## How can I run the created tests?</h3>
Considering that you have already installed all the necessary dependencies, thus running **Job Insights**, for testing purposes, you can run the following commands:
</br>
</br>

Run all the tests created for the *Model, Controller* and *Service* layers:
```
python3 -m pytest
```
</br>

</br>

<h3 align="left">Technologies, languages and Tools:</h3>
<p align="left"> 

<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
</a>
<a href="https://palletsprojects.com/p/flask//" target="_blank" rel="noreferrer"> <img src="https://github.com/beralb/python-flask-job-insights/blob/main/images/flask.png" alt="flask" width="40" height="40"/> 
</a>
<a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> 
</a>



</p>

