# Data Classes in Python

**data class module**, is introduced in python 3.7 as utility tool to make structured classes apecially for storing data. , especilamente para almacenar datos;

**dataClasses** in widely used Python3.7,

one can also use it in python 3.6 by installing dataclasses library.



```python
#import dataclasses 
pip install dataclasses
```



The DataClasses are implemented by using decorators with classes. (Las clases de datos se implementan mediante el uso de decoradores con clases.)

```python
#import dataclasses import dataclass
from dataclasses import dataclass #this line of code represent that module it is intalled or contained on version of python.


@dataclass
class GfgArticle():
    """a class for holding(mantener) an article content"""


    #atributtes using type hinsts to declarate

    title: str
    author: str
    languaje: str
    upvotes: int (votos a favor)

#a data class objetc
article=GfgArticle( "The diary of ceguera",
                    "Jose Saramgo",
                    "spanish",0)

print(article)
```

**Output:**

> GfgArticle(title=’DataClasses’, author=’vibhu4agarwal’, language=’Python’, upvotes=0)



**considerations abouth dataclass**

without a [__init__()](https://www.geeksforgeeks.org/constructors-in-python/) constructor, the datas - class accepted values and assigned it  to appropriate variables. 

the output of printing object is a neat representation(ordenada representación) of the data present in it, (presentes en el), without any explicit function coded to do this.

That means it has a modified [__repr__()](https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-2-data-hiding-and-object-printing/) function.



Equality of DataClasses

since the classes store data, checking two objects if they have the same data is a very common task thatś needed with dataclasses.

//dado que las clases almacenan datos, comprobar si dos objetos tienen los mismos datos es una tarea muy común que se necesita.//

This is accomplished by using the == operator.

Below is the code for an equivalent class for storing an article.

```python
class NormalArticle():
    """A class for holding an article content"""
 
    # Equivalent Constructor
    def __init__(self, title, author, language, upvotes):
        self.title = title
        self.author = author
        self.language = language
        self.upvotes = upvotes
 
# Two DataClass objects
dClassArticle1 = GfgArticle("DataClasses",
                            "vibhu4agarwal",
                            "Python", 0)
dClassArticle2 = GfgArticle("DataClasses",
                            "vibhu4agarwal",
                            "Python", 0)
 
# Two objects of a normal class
article1 = NormalArticle("DataClasses",
                         "vibhu4agarwal",
                         "Python", 0)
article2 = NormalArticle("DataClasses",
                         "vibhu4agarwal",
                         "Python", 0)

print("DataClass Equal:", dClassArticle1 == dClassArticle2)
print("Normal Class Equal:", article1 == article2)
```

**output**:

> DataClass Equal: True
> Normal Class Equal: False

Equality between two objects using == operator in python checks for the same memory location. 

*Since two objects take different memory locations on creation => the output for equality is **False** "La salida para igualdad es falsa para los datos en cuestiones de ubicacion"

*Equality between DataClass objects checks for the equality of data present in it. datos contenidos dentro del dataclass se checan , 

this accounts for **True** as output for equality check between two dataClass objects which contain same data.==>the salida es true for queals datas contained are the same values


