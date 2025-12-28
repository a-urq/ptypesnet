# Acts as a wrapper for the mPING API. Returns just the data needed for this project.
# Will hopefully make this eaier to deal with later on in the project.

import requests
import json

api_key = None
with open('mping-api-key.txt') as f:
    api_key = f.read()

reqheaders = {
    'content-type':'application/json',
    'Authorization': f'Token {api_key:s}'
    }

def retrieve_mping_reports(year: int = 2025, month: int = 12, day: int = 27, hour: int = None) -> dict:
    reqparams = {
        'category':'Rain/Snow',
        'year':str(year),
        'month':str(month),
        'day':str(day)
    }

    if hour is not None:
        reqparams = {
            'category':'Rain/Snow',
            'year':str(year),
            'month':str(month),
            'day':str(day),
            'hour':str(hour)
        }

    url = 'http://mping.ou.edu/mping/api/v2/reports'
    response = requests.get(url, params=reqparams, headers=reqheaders)

    if response.status_code != 200:
        print('Request Failed with status code %i' % response.status_code)

        return None
    else:
        # print('Request Successful')
        dump = response.json()
        data = json.loads(json.dumps(dump,indent=4))

        print(data['results'][0])
        print(len(data['results']))

        condensed_reports = [None] * len(data['results'])

        for i in range(len(condensed_reports)):
            condensed_report = {
                'obtime':data['results'][i]['obtime'],
                'ptype':data['results'][i]['description'],
                'latitude':data['results'][i]['geom']['coordinates'][1],
                'longitude':data['results'][i]['geom']['coordinates'][0]
            }

            condensed_reports[i] = condensed_report

        condensed_data = {'reports':condensed_reports}

        return condensed_data
    
if __name__ == "__main__":
    mping_reports = retrieve_mping_reports(2025, 12, 27)
    print(mping_reports)

    ptypes = []

    for i in range(len(mping_reports['reports'])):
        ptype = mping_reports['reports'][i]['ptype']

        if ptype not in ptypes:
            ptypes.append(ptype)

    print("unique ptypes:", ptypes)