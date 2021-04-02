import configparser

class common_utils:

    def get_url(self):
        config = configparser.ConfigParser()
        config.read('utils/properties.ini')
        print("nothing")
        return config['URL']['endpoint_url']

    def get_req_params(self):
        params={
            'function':'TIME_SERIES_DAILY',
            'symbol' : 'IBM',
            'apikey' : 'W2JTZ3CF2X8X4XW4'
        }
        return params