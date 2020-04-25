from django.shortcuts import render
from django.http import HttpResponse
from .forms import MalUrlForm
import urllib.request as urllib
import os
import re
import json
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

apikey =  os.environ.get('API_KEY')

def error_500(request,exception=None):
    return render(request, "urlerror.html", {})
    
def error_404(request,exception=None):
    return render(request, "urlerror.html", {})

        

def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False 


def malurl_form(request):
    if request.method == 'POST':
        form = MalUrlForm(request.POST)

        if form.is_valid():
            geturl = request.POST.get("url", "")
            if is_valid_url(geturl)==False:
               return render(request, 'urlerror.html')
            cmd = "curl -s --request GET --url 'https://www.virustotal.com/vtapi/v2/url/report?apikey="+apikey+"&resource="+geturl+"'"
            resp = os.popen(cmd)
            output = resp.read()
            try:
                imprint = json.loads(output)['positives']
            except:
                return render(request, 'urlerror.html')
            print(imprint)
            if imprint==1:
               result="The site may be malicious, "+str(imprint)+ " of our databases has marked it as malicious"
            elif imprint>1:
               result="The site is malicious, "+str(imprint)+" of our databases has marked it as malicious"
            else:
               result="The site seems to be safe according to our databases"
            return render(request, 'result.html', {'result': result})
    else:
        form = MalUrlForm()
    return render(request, 'index.html', {'form': form})
