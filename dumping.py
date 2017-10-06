import pickle
import base64

def tmp_dump(x):
    return base64.b64encode(pickle.dumps(x)).decode('utf-8')

handlers = {}
handlers[object] = lambda x: {'data': tmp_dump(x)}
