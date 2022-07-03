"""
Utilitários Python para lhe auxiliar na programação.

Dir -> Apresenta todos os atributos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável
dir(tipo de dado/variável)

Help -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/ métodos disponíveis
para determinado tipo de dado ou variável.
help(tipo de dado/variável.propriedade)

dir("Geek")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

dir("Geek")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
'swapcase', 'title', 'translate', 'upper', 'zfill']
"Geek".lower()
'geek'
help("Geek".lower)

help("Geek".lower)

"Geek".lower
<built-in method lower of str object at 0x10334f4f0>
help("Geek".lower)

"Geek".lower()
'geek'
"Geek".upper()
'GEEK'
help("Geek".upper)

"university".upper()
'UNIVERSITY'
'university'.lower()
'university'
'university'.title()
'University'
help("Geek".title)

'geek university'.title()
'Geek University'
'ANGELINA JOLIE'
'ANGELINA JOLIE'
'ANGELINA JOLIE'.title()
'Angelina Jolie'
'ANGELINA JOLIE'.lower().title()
'Angelina Jolie'


"""

print(dir('geek'))
