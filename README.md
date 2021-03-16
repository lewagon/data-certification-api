
# Data certification API

Le Wagon Data Science certification exam starter pack for the predictive API test.

**💡 This challenge is completely independent of other challenges. It is not required to complete any other challenge in order to work on this challenge.**

## Setup

### Duplicate the repository for the API challenge

**📝 Let's duplicate the repository of the API challenge.**

Go to https://github.com/lewagon/data-certification-api:
- Click on `Use this template`
- Enter the repository name `data-certification-api`
- Set it as **Public**
- Click on `Create repository from template`
- Click on `Code`
- Select `SSH`
- Copy the SSH URL of the repository (the format is `git@github.com:YOUR_NAME/data-certification-api.git`)

### Clone the repository for the API challenge

**📝 Now we will clone your new repository.**

Open your terminal and run the following commands:

👉 replace `YOUR_GITHUB_NICKNAME` with your **github nickname** and `PASTE_REPOSITORY_URL_HERE` with the SSH URL you just copied:

``` bash
cd ~/code/YOUR_GITHUB_NICKNAME
git clone PASTE_REPOSITORY_URL_HERE
cd data-certification-api
```

### Look around

**💡 The content of the challenge should look like this:**

``` bash
tree
```

```
.
├── Dockerfile
├── MANIFEST.in
├── Makefile
├── README.md
├── api
│   ├── __init__.py
│   └── app.py
├── exampack
│   ├── __init__.py
│   ├── data
│   ├── models
│   ├── predictor.py
│   ├── tests
│   │   └── __init__.py
│   └── utils.py
├── notebooks
├── requirements.txt
├── scripts
│   └── exampack-run
└── setup.py
```

You can now open you favorite text editor and proceed with the challenges.

## API challenge

**📝 In this challenge, you are provided with a trained model saved as `model.joblib`. The goal is to create an API that will predict the popularity of a song based on its other features.**

👉 In this challenge you will only need to edit the code of the API in `api/app.py` 🚨

👉 The package versions listed in `requirements.txt` should work out of the box will the pipeline saved in `model.joblib`

### Install the required packages

**📝 Let's install the required packages.**

👉 The `requirements.txt` file lists the exact version of the packages required in order to be able to load the trained pipeline that we provide

``` bash
pip install -r requirements.txt
```

If you encounter an version conflict while installing the packages, you will need to work in a new virtual environment:

👉 Only execute this commands if you encounter an issue while installing the packages 🚨

``` bash
pyenv install 3.8.6
pyenv virtualenv 3.8.6 certif
pyenv local certif
pip install -r requirements.txt
```

## API endpoint

**📝 Let's begin by creating a prediction endpoint.**

### Run a uvicorn server

**📝 Start a `uvicorn` server in order to make sure that the setup works correctly.**

Run the server:

```bash
uvicorn api.app:app --reload
```

Open your browser at http://localhost:8000/

👉 You should see the response `{ "ok": true }`

You will now be able to work on the content of the API while `uvicorn` automatically reloads your code as it changes.

### Create a `prediction` endpoint

**📝 Add a `/predict` endpoint to `api/app.py`.**

👉 Remember, throughout this challenge, you are able to test your endpoint easily at http://localhost:8000/docs

### Load the pipeline

**📝 In the prediction endpoint, load the trained pipeline that is provided.**

👉 You can use the following code:

``` python
import joblib

pipeline = joblib.load("model.joblib")
```

### API definition

**📝 Here is the definition of the API that we want to create.**

The API will take as input the following parameters:
- acousticness: float
- danceability: float
- duration_ms: int
- energy: float
- explicit: int
- id: string
- instrumentalness: float
- key: int
- liveness: float
- loudness: float
- mode: int
- name: string
- release_date: string
- speechiness: float
- tempo: float
- valence: float
- artist: string

💡 The pipeline contained in the `model.joblib` file expects for its predictions a `DataFrame` with the following data types:

```
acousticness        float64
danceability        float64
duration_ms           int64
energy              float64
explicit              int64
id                   object
instrumentalness    float64
key                   int64
liveness            float64
loudness            float64
mode                  int64
name                 object
release_date         object
speechiness         float64
tempo               float64
valence             float64
artist               object
```

👉 The pipeline expects these parameters to be provided in this exact same order 🚨

The API will return a json dictionary with a `pred` key containing the prediction of the popularity of the track as a `int`

``` json
{
  "pred": 22
}
```

### Handle the API parameters

**📝 Add to your `/predict` endpoint the parameters that are required in order to make a prediction. Then create a `DataFrame` variable named `X_pred` from these parameters.**

👉 Remember that `FastAPI` only provides `string` variables as parameters to the endpoint

👉 Remember that the parameters need to be built into the `DataFrame` in the exact **same order** as the one required by the pipeline 🚨

💡 One way of building a `DataFrame` from individual values is to create it from a dictionary of lists

👉 Once `X_pred` is built, you may `print` it and have a look at the output of the `uvicorn` command in order to make sure that it is correctly created

### Make a prediction

**📝 Now that you have a trained pipeline and a `DataFrame` containing one observation, let's make a prediction and return it.**

👉 Remember that `FastAPI` can only handle simple data types as returned `json` values

Test your API using http://localhost:8000/docs and make sure that it works correctly before proceeding to put it in production.

## API in production

**📝 Push your API to production on the hosting service of your choice.**

👉 Remember to test your API locally and make an actual prediction before pushing your code to production in order to save time

👉 You may test your API with the following parameters (change the domain and port with your own):

```
http://localhost:8000/predict?acousticness=0.654&danceability=0.499&duration_ms=219827&energy=0.19&explicit=0&id=0B6BeEUd6UwFlbsHMQKjob&instrumentalness=0.00409&key=7&liveness=0.0898&loudness=-16.435&mode=1&name=Back%20in%20the%20Goodle%20Days&release_date=1971&speechiness=0.0454&tempo=149.46&valence=0.43&artist=John%20Hartford
```

💡 With a configured GCP account, the directives in the `Makefile` should be enough to push your API to production

👉 Remember to update the `GCP_PROJECT_ID` in the `Makefile` 🚨
