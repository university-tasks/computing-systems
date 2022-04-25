METHODS_PARAM = {
    "scale": {"name": "l", "default": "2", "range": (2, 10)},
    "histogram": {"name": "BIN", "default": "32", "range": (8, 65)},
    "gradient": {"name": "W", "default": "10", "range": (4, 21)},
    "dft": {"name": "P", "default": "20", "range": (6, 31)},
    "dct": {"name": "P", "default": "20", "range": (6, 31)},
}

DATABASE_CONF = {
    "ORIGINAL": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "/Users/inctnce/Desktop/modern-computing-systems/Task2/data/ORIGINAL/s{g}/{im}.pgm",
    },
    "MASKED": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "/Users/inctnce/Desktop/modern-computing-systems/Task2/data/MASKED/s{g}/{im}.pgm",
    },
    "CLOACKED": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "/Users/inctnce/Desktop/modern-computing-systems/Task2/data/CLOACKED/s{g}/{im}.jpg",
    },
}

DATA_PATH = "/Users/inctnce/Desktop/modern-computing-systems/Task2/data/"
