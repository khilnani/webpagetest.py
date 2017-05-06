#!/usr/bin/env python

import json

def get_config(config_file='config.json'):
    with open(config_file, "r") as f:
        config = json.load(f)
        print( json.dumps(config, indent=2)) 
        return config

