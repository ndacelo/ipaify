from vowels.en_vowels import en_vowel_mapper
from consonants.en_consonants import en_consonant_mapper
from collections import defaultdict




class Converter():
    """ Conversion class """

    def __init__(self, word):
        self.word_list = list(word)
        self.all_vowels = [val for sublist in en_vowel_mapper.values() for val in sublist]
        self.all_cons = [val for sublist in en_consonant_mapper.values() for val in sublist]
        self.init = []
        count = 0
        for char in self.word_list:
            d = {}
            if char in self.all_cons:
                d['raw_char'] = char
                d['raw_class'] = 'C'
            elif char in self.all_vowels:
                d['raw_char'] = char
                d['raw_class'] = 'V'
            d['pos'] = count
            count = count + 1
            self.init.append(d)

    def eliminate_double_consonant(self):
        """ reduce certain double consonants """
        double_consonants = ['d', 't', 'p', 'm', 'n', 'r', 'g']
        previous = ''
        for char in self.init:
            if char['raw_char'] in double_consonants and char['raw_char'] == previous:
                self.init.remove(char)
            previous = char['raw_char']
        return self.init

    def past_tense(self):
        """ find appropriate past tense ipa
        ex:
            ortho     transcribed
            walked -> [walkt]  in this case a /t/ sound is heard
            played -> [playd]  in this case a /d/ sound is heard
            molded -> [moldid] in this case an /ɪd/ sound is heard
        """
        ultimate_char = self.init[-1]['raw_char']
        penaultimate_char = self.init[-2]['raw_char']
        id_pronunciation = ['t', 'd']
        t_pronunciation = ['p', 'f', 's', 'h', 'k']
        d_pronunciation = ['n', 'w', 'y', 'a', 'e', 'i', 'o', 'u', 'g']
        target_char = self.init[-3]['raw_char']

        if ultimate_char == 'd' and penaultimate_char == 'e':
            if target_char in t_pronunciation:
                self.init.remove(self.init[-2])
                self.init[-1]['ipa_char'] = 't'
                self.init[-1]['place'] = 'alveolar'
                self.init[-1]['manner'] = 'stop'
                self.init[-1]['voiced'] = False

            elif target_char in d_pronunciation:
                self.init.remove(self.init[-2])
                self.init[-1]['ipa_char'] = 'd'
                self.init[-1]['place'] = 'alveolar'
                self.init[-1]['manner'] = 'stop'
                self.init[-1]['voiced'] = True
                

            elif target_char in id_pronunciation:
                self.init[-1]['ipa_char'] = 'd'
                self.init[-1]['place'] = 'alveolar'
                self.init[-1]['manner'] = 'stop'
                self.init[-1]['voiced'] = True
                self.init[-2]['ipa_char'] = 'ɪ'
                self.init[-2]['place'] = 'front high'
                self.init[-2]['voiced'] = True

    
        return self.init

    def tap(self):
        """ replace intervocalic t or d with tap """
        tap_list  = ['t', 'd']
        l = len(self.init)
        key = 'ipa_char'
        has_final_n = self.init[-1]['raw_char'] == 'n'
        for char in range(l):
            if self.init[char]['raw_char'] in tap_list and key not in self.init[char]:
                left = self.init[char - 1]['raw_class']
                right = self.init[char + 1]['raw_class']
                if left  and right == 'V' and not has_final_n:
                    self.init[char]['ipa_char'] = 'ɾ'
                    self.init[char]['place'] = 'alveolar'
                    self.init[char]['manner'] = 'tap'
                    self.init[char]['voiced'] = True
                else:
                    self.init[char]['ipa_char'] = 'ʔ'
                    self.init[char]['place'] = 'glottal'
                    self.init[char]['manner'] = 'stop'
                    self.init[char]['voiced'] = False


        return self.init

    def nasals(self):
        
        if self.init[-1] or self.init[1] == 'n':
            self.init[-1]['ipa_char'] = 'n'
            self.init[-1]['place'] = 'alveolar'
            self.init[-1]['manner'] = 'nasal'
            self.init[-1]['voiced'] = True
        elif self.init[-1] or self.init[1] == 'm':
            self.init[-1]['ipa_char'] = 'm'
            self.init[-1]['place'] = 'velar'
            self.init[-1]['manner'] = 'nasal'
            self.init[-1]['voiced'] = True
       
        return self.init
    
    

    # def second_pass(self):
    #     """ try to assign more ipa values """

    #     l = len(self.init)
    #     key = 'ipa_char'
    #     for char in range(l):
    #         if key not in self.init[char]:



            
