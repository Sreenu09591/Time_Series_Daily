import configparser

class common_utils:

    def get_url(self):
        config = configparser.ConfigParser()
        config.read('utils/properties.ini')
        return config['URL']['endpoint_url']

    def get_req_params(self):
        params={
            'function':'TIME_SERIES_DAILY',
            'symbol' : 'IBM',
            'apikey' : '6ICDX7I7QDC4B3EI'
        }
        return params