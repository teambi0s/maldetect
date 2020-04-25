# maldetect

A web application built using django to detect malicious URL(s) which include phishing/social engineering/malware infected URL(s).


# To run 

```bash

$ cd maldetect
$ echo "export API_KEY='[SECRET]'" > .env
$ echo "export SECRET_KEY='[SECRET]'" >> .env
$ source maldetect/bin/activate 
(maldetect) $ source .env
(maldetect) $ python manage.py runserver

```


Make sure that you add your API_KEY from virustotal and change the secret key before running it. 




# Credits

@[abhiabhi2306](https://github.com/abhiabhi2306)
@[v1dhun](https://github.com/v1dhun)
