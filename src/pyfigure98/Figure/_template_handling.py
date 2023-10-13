from ._place_holder import Figure

import os.path
import os


def getTemplate(file_path) -> dict:
    template = dict()
    with open(
        os.path.dirname(__file__) + "/Templates/" + file_path + ".txt"
    ) as f:

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
