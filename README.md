# maldetect

A web application built using django to detect malicious URL(s) which include phishing/social engineering/malware infected URL(s).


# To run 

```bash

$ cd maldetect
$ echo "export API_KEY='[SECRET]'" > .env
$ echo "export SECRET_KEY='[SECRET]'" >> .env
$ source maldetect/bin/activate 
(maldetect) $ source .env
(maldetect) $ python3 manage.py makemigrations
(maldetect) $ python3 manage.py migrate
(maldetect) $ python3 manage.py runserver IP:PORT

```


1) Make sure to export the API_KEY from virustotal to .env
2) Make sure to create and export a secret_key for django to .env




# Contributors

 
@[abhiabhi2306](https://github.com/abhiabhi2306)
@[v1dhun](https://github.com/v1dhun)  from Team Bi0s :hearts:
