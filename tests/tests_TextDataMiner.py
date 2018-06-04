# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
from aplication.text_data_miner import text_data_miner
import unittest

class tester_text_data_miner(unittest.TestCase):
    def test_short_test(self):
        text = "Hola, me llamo Alfonso"
        result = text_data_miner(text)
        assert result == [['me', 1], ['llamo', 1], ['alfonso', 1], ['hola', 1]]

    def test_long_text(self):
        text = "Hola, me llamo Arturo, y Alfonso es más guapo y más listo que yo, pero no es que esto lo esté " \
               "escribiendo Alfonso, para nada. Solo que estoy muy de acuerdo con su superioridad en cualquier " \
               "aspecto de la vida, sobretodo a la hora de hacer tests unitarios, es un crack."
        result = text_data_miner(text)
        assert result == [['que', 3], ['alfonso', 2], ['y', 2], ['hora', 1], ['esté', 1], ['esto', 1],
                          ['superioridad', 1], ['llamo', 1], ['guapo', 1], ['no', 1], ['vida', 1], ['escribiendo', 1],
                          ['sobretodo', 1], ['crack', 1], ['tests', 1], ['unitarios', 1], ['nada', 1], ['listo', 1],
                          ['cualquier', 1], ['aspecto', 1], ['hola', 1], ['arturo', 1], ['me', 1], ['acuerdo', 1]]


    def test_param_error(self):
        text = 1702.2019
        self.assertRaises(TypeError, text_data_miner, text, "stop_words.txt")

    def test_short_text_stop_words(self):
        text = "vosotras solo solamente saber a agüita de coco"
        result = text_data_miner(text)
        assert result == [['agüita', 1], ['coco', 1]]

    def test_long_text_stop_words(self):
        text = "vosotras solo solamente saber a agüita de melocotón ellas nos nosotros vosotros vosotras si dentro " \
               "solo solamente  un una unas unos uno sobre todo también tras otro algún trabaja trabajamos trabajais " \
               "trabajan podria podrias podriamos podrian podriais yo aquel"
        result = text_data_miner(text)
        assert result == [['agüita', 1], ['también', 1], ['todo', 1],
                          ['melocotón', 1], ['algún', 1]]

    def test_sort_times_appear(self):
        text_times = ["eselsolquetealumbra ", "tuspiernasquemandan ", "somostresentucama ", "vienedespués ",
                      "tuscontinentes ", "lasmediasfaenas ", "sonlospecadoscometidos ", "sumanconmigo ",
                      "losquetecobro ",
                      "Másdehesentido "]
        text = ""
        for i in range(0, 10):
            for _ in range(i+1):
                text += text_times[i]

        result = text_data_miner(text)
        assert result == [['másdehesentido', 10], ['losquetecobro', 9], ['sumanconmigo', 8],
                          ['sonlospecadoscometidos', 7], ['lasmediasfaenas', 6], ['tuscontinentes', 5],
                          ['vienedespués', 4], ['somostresentucama', 3], ['tuspiernasquemandan', 2],
                          ['eselsolquetealumbra', 1]]

    def test_codification(self):
        text = "妹妹背著洋娃娃 ДеньПобеды 사람은"
        result = text_data_miner(text)
        assert result == [['ДеньПобеды', 1], ['妹妹背著洋娃娃', 1], ['사람은', 1]]

    def test_long_text_punctuation_marks(self):
        text = "Hola, me llamo Alfonso y Arturo es más guapo y más listo que yo!!! pero no es que esto lo esté " \
               "escribiendo Arturo.. para nada. Solo que estoy (muy) de acuerdo con su ''superioridad' en cualquier " \
               "aspecto de la vida!!! sobretodo, a la hora de hacer tests unitarios"
        result = text_data_miner(text)
        assert result == [['que', 3], ['y', 2], ['arturo', 2], ['hora', 1], ['esté', 1], ['esto', 1],
                          ['superioridad', 1], ['llamo', 1], ['guapo', 1], ['alfonso', 1], ['no', 1], ['vida', 1],
                          ['escribiendo', 1], ['sobretodo', 1], ['tests', 1], ['unitarios', 1], ['nada', 1],
                          ['listo', 1], ['cualquier', 1], ['aspecto', 1], ['hola', 1], ['me', 1], ['acuerdo', 1]]


    def test_short_text_punctuation_marks(self):
        text = "...:-´`+*¨+´+´++++++´+´ que bien es eso `+´+´+...,.,'''?!!!!¿'¡"
        result = text_data_miner(text)
        assert result == [['eso', 1], ['que', 1]]

    def test_caps(self):
        text = "hola Hola hOla hoLa holA HOla HoLa HolA HOLa HOlA HOLA"
        result = text_data_miner(text)
        assert result == [['hola', 11]]

    def test_fail_type_stop_words(self):
        self.assertRaises(TypeError, text_data_miner, "Hola", 48)


if __name__ == '__main__':
    import xmlrunner

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-report'))