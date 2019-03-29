import gender_guesser.detector as gender

_detector = gender.Detector(case_sensitive=False)

_mapping = {'mostly_male': 'male',
            'mostly_female': 'female',
            'andy': 'unknown',
            'male': 'male',
            'female': 'female',
            'unknown': 'unknown'}


def consolidated_gender(name):
    return _mapping[_detector.get_gender(name)]
