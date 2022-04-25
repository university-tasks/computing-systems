from .HCDClassifier import HCDClassifier
from .ORBClassifier import ORBClassifier
from .SIFTClassifier import SIFTClassifier

classifiers = {
        "HCD": HCDClassifier(),
        "ORB": ORBClassifier(),
        "SIFT": SIFTClassifier()
    }