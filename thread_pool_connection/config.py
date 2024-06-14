import os
from configparser import ConfigParser


def config(filename="config.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)

        for item in params:
            db[item[0]] = item[1]

    else:
        raise Exception(f"Section {section} not found in the filename {filename}")
    
    return db