from ._place_holder import Figure

import os.path
import os


def getTemplate(file_path) -> dict:
    template = dict()
    with open(
        os.path.dirname(__file__) + "/Templates/" + file_path + ".txt"
    ) as f:

        for line in f:
            line = line.replace(" ", "").strip()
            name, equal, size = line.partition("=")
            template[name] = float(size)

    return template


def getAllTemplates() -> dict:
    all_files = os.listdir(os.path.dirname(__file__) + "/Templates/")
    txt_files = filter(lambda x: x[-4:] == '.txt', all_files)
    try:
        template_list = dict()
        for file in txt_files:
            file = file[0:-4]
            new_template = getTemplate(file)
            template_list[file] = new_template
    except ImportError:
        raise ImportError("""Error occured when importing templates, check if
                          everything is setup correctly."""
                          )

    return template_list
