from .classifiers import classifiers
from ..utils.load import load

def train():
    
    print("LOADING DATABASES")
    data = load()
        
    X_train = [img for img, _ in data]
    y_train = [style for _, style in data]

        # fit classifiers
    for name, classifier in classifiers.items():
        print(f"TRAINING METHOD: {name}")
        classifier.fit(X_train, y_train)
    print("FINISHED TRAINING CLASSIFIERS")