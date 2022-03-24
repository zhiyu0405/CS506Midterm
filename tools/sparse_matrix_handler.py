from scipy import sparse

def save(m, name, path):
    try:
        if path[-1] != '/':
            path += '/'
        if '.npz' not in name:
            name += '.npz'
        sparse.save_npz(f'{path}{name}', m)
        print('Done')
    except Exception as e:
        print(e)

def load(name, path):
    try:
        if path[-1] != '/':
            path += '/'
        if '.npz' not in name:
            name += '.npz'
        m = sparse.load_npz(f'{path}{name}')
        print('Done')
        return m
    except Exception as e:
        print(e)
        return None