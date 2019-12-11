#!/usr/bin/env python3
import PyFunceble
import colorama
from PyFunceble.engine import ci

if __name__ == "__main__":

    colorama.init(autoreset=True)
    
    # We load our custom configuration
    CUSTOM_CONFIG = {
        "ci": True,
        "ci_autosave_final_commit": "Update iana-domains-db.json",
        "multiprocess": True,
        "maximal_processes": 50,
        "dns_server": [
            "one.one.one.one"
        ]
    }

    PyFunceble.load_config(custom=CUSTOM_CONFIG)
    # PyFunceble.cconfig.Preset() 
    
    # We initiate the repostiory.
    ci_engine = ci.TravisCI()
    ci_engine.init() 

    PyFunceble.lookup.Iana().update()

    ci_engine.end_commit()