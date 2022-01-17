import pyrebase

config = {
  "apiKey": "AIzaSyD0liM23zMk_HgnZicjO2uHbvsNmmKx3H8",
  "authDomain": "sentimentanalysis-9bdac.firebaseapp.com",
  "databaseURL": "https://sentimentanalysis-9bdac-default-rtdb.firebaseio.com",
  "storageBucket": "sentimentanalysis-9bdac.appspot.com"
}

firebase = pyrebase.initialize_app(config)