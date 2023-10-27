from ._place_holder import Figure_

import os
import json
import sys


def addCustomTemplate(self: Figure_, file_path:str):
    """
    
    """
    
    template = dict()

    # Get the path to the file that called addCustomTemplate()
    namespace = sys._getframe(1).f_globals # caller's globals
    callerPath = namespace['__file__']

    # Get the directory of the file that called addCustomTemplate()
    callerDirectory = "\\".join(callerPath.split("\\")[:-1]) 

    with open(
        callerDirectory + "\\" + file_path + ".json"
    ) as f:
            template:dict
            template = json.load(f)
    
    defaultTemplate = self.templates['default']
    
    for key, value in defaultTemplate.items():
        if(key not in template.keys()):
            template[key] = value

    self.templates[file_path] = template

def getTemplate(file_path:str) -> dict:
    template = dict()
    with open(
        os.path.dirname(__file__) + "/Templates/" + file_path + ".json"
    ) as f:
        template = json.load(f)

    return template


def getAllTemplates() -> dict:
    all_files = os.listdir(os.path.dirname(__file__) + "/Templates/")
    json_files = filter(lambda x: x[-5:] == '.json', all_files)
    try:
        template_list = dict()
        for file in json_files:
            file = file[0:-5]
            new_template = getTemplate(file)
            template_list[file] = new_template
    except ImportError:
        raise ImportError("""Error occured when importing templates, check if
                          everything is setup correctly."""
                          )

    return template_list
