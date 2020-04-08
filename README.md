# flask-firestore
Flask web-application using Google Cloud service

 [Crash guide for Flask Firestore](https://medium.com/google-cloud/building-a-flask-python-crud-api-with-cloud-firestore-firebase-and-deploying-on-cloud-run-29a10c502877)
 
 [Firestore quickstart](https://cloud.google.com/firestore/docs/quickstart-servers)
 
### Flask

Terminal

```
export FLASK_APP=app.py
flask run
```

PowerShell

``` 
$env:FLASK_APP = "src.app.py" 
flask run
```

### Google Cloud Authentication

Terminal

```
export GOOGLE_APPLICATION_CREDENTIALS="key.json"
```

PowerShell

```
$env:GOOGLE_APPLICATION_CREDENTIALS="app.json"
```

### Google Cloud SDK

```
gcloud init
```

