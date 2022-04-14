import pickle

class DataModel:

    def __init__(self):
        try :
            self.load("logConfig")
        except Exception as err:
            print(err)
            print("Loaoad failed")
            self.config = {"scaleFactor" : 101,
                    "minNeighbors" : 2,
                    "minSize" : 200,
                    "maxSize" : 2000,
                    "classCascadesFiles" : [], 
                    "move_speed" : 1
                    }

        self.settings = {"tracking" : False,
        "face_delta" : (0,0)}

    def setMaxSize(self, arg):
        self.config["maxSize"] = arg
        self.save()

    def setMinSize(self, arg):
        self.config["minSize"] = (arg, arg)
        self.save()

    def setMinNeighbors(self, arg):
        self.config["minNeighbors"] = arg
        self.save()

    def setScaleFactor(self, arg):
        self.config["scaleFactor"] = arg
        self.save()

    def addClassCascadesFiles(self, file):
        self.config["classCascadesFiles"].append(file)
        self.save()

    def removeClassCascadesFilesByIndex(self, index):
        del self.config["classCascadesFiles"][index]
        self.save()

    def setTracking(self, boolean):
        self.settings["tracking"] = boolean
        self.save()

    def setFaceDelta(self, delta):
        self.settings["face_delta"] = delta

    def save(self):
        with open('logConfig', 'wb') as f:
            pickle.dump(self, f)

    def load(self, fl):
        with open(fl, 'rb') as f:
            log = pickle.load(f).config
            print(log)
            self.config = log






"""
# Face_Tracking
    # Software_side
    scaleFact
    minNeighbors
    minSize
    maxSize
    classCascade

    # Hardware_side
    move_speed

"""


