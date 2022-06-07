# Created in a team

import numpy as np


def translate_gt_and_predicts(mapping_set, data_set):
    translated_set = np.empty(np.size(data_set), dtype=int)
    for i in range(np.size(data_set)):
        translated_set[i] = np.array([int(mapping_set[data_set[i]])])
    return translated_set


# Created by me


def translate_classes(data_set):
    translated_classes = np.empty(np.size(data_set), dtype=str)
    for i in range(np.size(data_set)):
        print("Class", data_set[i], "means", transldict[int(data_set[i])])


# Created by me

transldict = {
    0: "20km/h",
    1: "30km/h",
    2: "50km/h",
    3: "60km/h",
    4: "70km/h",
    5: "80km/h",
    6: "80km/h aufgehoben",
    7: "100km/h",
    8: "120km/h",
    9: "Überholverbot für Autos",
    10: "Überholverbot für LKWs",
    11: "Vorfahrt",
    12: "Vorfahrtsstraße",
    13: "Vorfahrt gewähren",
    14: "Stop",
    15: "Durchfahrtsverbot",
    16: "Durchfahrtsverbot für LKWs",
    17: "Einfahrt verboten",
    18: "Achtung",
    19: "Linkskurve",
    20: "Rechtskurve",
    21: "Kurvige Strecke",
    22: "Unebene Fahrbahn",
    23: "Schleudergefahr",
    24: "Verengung Fahrbahn",
    25: "Baustelle",
    26: "Ampel voraus",
    27: "Achtung Fußgänger",
    28: "Achtung Kinder",
    29: "Achtung Radfahrer",
    30: "Achtung Glätte",
    31: "Achtung Wildwechsel",
    32: "Begrenzungen aufgehoben",
    33: "Rechts abbiegen",
    34: "Links abbiegen",
    35: "Geradeaus fahren",
    36: "Geradeaus oder rechts",
    37: "Geradeaus oder links",
    38: "Rechts vorbei fahren",
    39: "Links vorbei fahren",
    40: "Kreisverkehr",
    41: "Überholverbot aufgehoben Autos",
    42: "Überholverbot aufgehoben LKWs",
}
