en_consonant_mapper = {
    'p': ['p', 'pp'],
    'b': ['b'],
    't': ['t'],
    'd': ['d', 'dd'],
    'k': ['k', 'c', 'q', 'ck', 'ch'],
    'g': ['g', 'gg'],
    'ʔ': ['t', 'tt'],
    'm': ['m', 'mm'],
    'n': ['n', 'nn'],
    'ŋ': ['ng'],
    'ɾ': ['tt', 'dd', 't', 'd'],
    'f': ['f', 'ph', 'gh'],
    'v': ['v', 'f'],
    'θ': ['th'],
    'ð': ['th'],
    's': ['s', 'c', 'ss'],
    'z': ['z', 's', 'th'],
    'ʃ': ['sh', 'si', 'ti', 's'],
    'ʒ': ['g', 's', 'z', 'si'],
    'h': ['h'],
    'ɹ': ['r'],
    'j': ['y'],
    'l': ['l', 'll'],
    't͡ʃ': ['ch', 't'],
    'd͡ʒ': ['g', 'dg', 'j', 'd'],
    'w': ['w', 'u'],
}


en_consonant_ipa = {
    'p': {
        'place': 'bilabial',
        'manner': 'stop',
        'voiced': False,
    },
    'b': {
        'place': 'bilabial',
        'manner': 'stop',
        'voiced': True,
    },
    't': {
        'place': 'alveolar',
        'manner': 'stop',
        'voiced': False,
    },
    'd': {
        'place': 'alveolar',
        'manner': 'stop',
        'voiced': True,
    },
    'k': {
        'place': 'velar',
        'manner': 'stop',
        'voiced': False,
    },
    'g': {
        'place': 'velar',
        'manner': 'stop',
        'voiced': True,
    },
    'ʔ': {
        'place': 'glottal',
        'manner': 'stop',
        'voiced': False,
    },
    'm': {
        'place': 'velar',
        'manner': 'nasal',
        'voiced': True,
    },
    'n': {
        'place': 'alveolar',
        'manner': 'nasal',
        'voiced': True,
    },
    'ŋ': {
        'place': 'velar',
        'manner': 'nasal',
        'voiced': True,
    },
    'ɾ': {
        'place': 'alveolar',
        'manner': 'tap',
        'voiced': True,
    },
    'f': {
        'place': 'labio-dental',
        'manner': 'fricative',
        'voiced': False,
    },
    'v': {
        'place': 'labio-dental',
        'manner': 'fricative',
        'voiced': True,
    },
    'θ': {
        'place': 'dental',
        'manner': 'fricative',
        'voiced': False,
    },
    'ð': {
        'place': 'dental',
        'manner': 'fricative',
        'voiced': True,
    },
    's': {
        'place': 'alveolar',
        'manner': 'fricative',
        'voiced': False,
    },
    'z': {
        'place': 'alveolar',
        'manner': 'fricative',
        'voiced': True,
    },
    'ʃ': {
        'place': 'post-alveolar',
        'manner': 'fricative',
        'voiced': False,
    },
    'ʒ': {
        'place': 'post-alveolar',
        'manner': 'fricative',
        'voiced': True,
    },
    'h': {
        'place': 'glottal',
        'manner': 'fricative',
        'voiced': False,
    },
    'ɹ': {
        'place': 'alveolar',
        'manner': 'approximant',
        'voiced': True,
    },
    'j': {
        'place': 'palatal',
        'manner': 'approximant',
        'voiced': True,
    },
    'l': {
        'place': 'alveolar',
        'manner': 'lateral approximant',
        'voiced': True,
    },
    't͡ʃ': {
        'place': 'post-alveolar',
        'manner': 'affricate',
        'voiced': False,
    },
    'd͡ʒ': {
        'place': 'post-alveolar',
        'manner': 'affricate',
        'voiced': True,
    },
    'w': {
        'place': 'velar',
        'manner': 'glide',
        'voiced': False,
    },
}