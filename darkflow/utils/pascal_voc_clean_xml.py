import json

def pascal_voc_clean_xml(ANN, pick, exclusive = False):
    return json.load(open(ANN))
