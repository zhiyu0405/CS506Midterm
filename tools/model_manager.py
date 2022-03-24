import joblib

class model_manager:
    
    def __init__(self, model_name, model_path, model = None):
        self.model_name = model_name
        self.model_path = model_path
        self.model = model
        
    def save(self, path = None, name = None):
        
        try:
        
            if not self.model:
                print('No model to save')
                return

            if not path:
                path = self.model_path
            if not name:
                name = self.model_name
            if '.pkl' not in name:
                name += '.pkl'
            if path[-1] != '/':
                path += '/'
            joblib.dump(self.model, f'{path}{name}')
            print('Done')
            
        except Exception as e:
            print(e)
        
    def load(self):
        
        try:
            name = self.model_name
            path = self.model_path
            if '.pkl' not in name:
                name += '.pkl'
            if path[-1] != '/':
                path += '/'
#             print(f'{path}{name}')
            self.model = joblib.load(f'{path}{name}')
            print('Done')
        except Exception as e:
            print(e)