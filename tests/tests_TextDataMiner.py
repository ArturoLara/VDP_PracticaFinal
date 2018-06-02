from sample.TextDataMiner import Text_Data_Miner
import unittest

class tester_text_data_miner(unittest.TestCase):
    def test_short_test(self):
        text = "Hola, me llamo Alfonso"
        result = Text_Data_Miner(text)
        assert result == [['hola', 1], ['me', 1], ['llamo', 1], ['alfonso', 1]]

    def test_long_text(self):
        text = "Hola, me llamo Arturo, y Alfonso es más guapo y más listo que yo, pero no es que esto lo esté " \
               "escribiendo Alfonso, para nada. Solo que estoy muy de acuerdo con su superioridad en cualquier " \
               "aspecto de la vida, sobretodo a la hora de hacer tests unitarios, es un crack."
        result = Text_Data_Miner(text)
        assert result == [['que', 3], ['y', 2], ['alfonso', 2], ['más', 2], ['hola', 1], ['me', 1], ['llamo', 1],
                          ['arturo', 1], ['guapo', 1], ['listo', 1], ['no', 1], ['esto', 1], ['esté', 1],
                          ['escribiendo', 1], ['nada', 1], ['acuerdo', 1], ['superioridad', 1], ['cualquier', 1],
                          ['aspecto', 1], ['vida', 1], ['sobretodo', 1], ['hora', 1], ['tests', 1], ['unitarios', 1],
                          ['crack', 1]]


    def test_param_error(self):
        text = 1702.2019
        self.assertRaises(TypeError, Text_Data_Miner, text, "stop_words.txt")

    def test_short_text_stop_words(self):
        text = "vosotras solo solamente saber a agüita de coco"
        result = Text_Data_Miner(text)
        assert result == [['agüita', 1], ['coco', 1]]

    def test_long_text_stop_words(self):
        text = "vosotras solo solamente saber a agüita de melocotón ellas nos nosotros vosotros vosotras si dentro " \
               "solo solamente  un una unas unos uno sobre todo también tras otro algún trabaja trabajamos trabajais " \
               "trabajan podria podrias podriamos podrian podriais yo aquel"
        result = Text_Data_Miner(text)
        assert result == [['agüita', 1], ['melocotón', 1]]

    def test_sort_times_appear(self):
        text_times = ["eselsolquetealumbra ", "tuspiernasquemandan ", "somostresentucama ", "vienedespués ",
                      "tuscontinentes ", "lasmediasfaenas ", "sonlospecadoscometidos ", "sumanconmigo ",
                      "losquetecobro ",
                      "Másdehesentido "]
        text = ""
        for i in range(0, 10):
            for _ in range(i+1):
                text += text_times[i]

        result = Text_Data_Miner(text)
        assert result == [['másdehesentido', 10], ['losquetecobro', 9], ['sumanconmigo', 8],
                          ['sonlospecadoscometidos', 7], ['lasmediasfaenas', 6], ['tuscontinentes', 5],
                          ['vienedespués', 4], ['somostresentucama', 3], ['tuspiernasquemandan', 2],
                          ['eselsolquetealumbra', 1]]

    def test_codification(self):
        text = "妹妹背著洋娃娃 ДеньПобеды 사람은"
        result = Text_Data_Miner(text)
        assert result == [['妹妹背著洋娃娃', 1], ['деньпобеды', 1], ['사람은', 1]]

    def test_long_text_punctuation_marks(self):
        text = "Hola, me llamo Alfonso y Arturo es más guapo y más listo que yo!!! pero no es que esto lo esté´` " \
               "escribiendo Arturo.. para nada. ¡Solo que estoy (muy) de acuerdo con su ''superioridad' en cualquier " \
               "aspecto de la vida!!! sobretodo, a la hora de hacer tests unitarios"
        result = Text_Data_Miner(text)
        assert result == [['que', 3], ['y', 2], ['arturo', 2], ['más', 2], ['hola', 1], ['me', 1], ['llamo', 1],
                          ['alfonso', 1], ['guapo', 1], ['listo', 1], ['no', 1], ['esto', 1], ['esté', 1],
                          ['escribiendo', 1], ['nada', 1], ['acuerdo', 1], ['superioridad', 1], ['cualquier', 1],
                          ['aspecto', 1], ['vida', 1], ['sobretodo', 1], ['hora', 1], ['tests', 1],
                          ['unitarios', 1]]

    def test_short_text_punctuation_marks(self):
        text = "...:-´`+*¨+´+´++++++´+´ que bien es eso `+´+´+...,.,'''?!!!!¿'¡"
        result = Text_Data_Miner(text)
        assert result == [['que', 1], ['eso', 1]]

    def test_caps(self):
        text = "hola Hola hOla hoLa holA HOla HoLa HolA HOLa HOlA HOLA"
        result = Text_Data_Miner(text)
        assert result == [['hola', 11]]

    def test_fail_path_stop_words(self):
        self.assertRaises(FileNotFoundError, Text_Data_Miner,"Hola", "No hay haha")

    def test_fail_type_stop_words(self):
        self.assertRaises(TypeError, Text_Data_Miner, "Hola", 48)


if __name__ == '__main__':
    unittest.main()