import json


def load_json_lines(path):
    with open(path, 'r') as f:
        t_lt = f.readlines()
        d_lt = []
        for t in t_lt:
            try:
                d_lt.append(json.loads(t))
            except:
                pass
    return d_lt


def load_json(path):
    with open(path, 'r') as f:
        d_ = json.load(f)
    return d_


def save_json(path, obj):
    with open(path, 'w') as f:
        json.dump(obj, f)
