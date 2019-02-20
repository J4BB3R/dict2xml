# pydict2xml
Python lib who convert python dictionnary into xml string output

#### This Python Dictionnary :

```
DATA_SEP="><"

dict : {
    "opt" : "nope"
    "opt-alter" : "nope"
    "data" : {
        "foo" : "none"
        DATA_SEP : "Random Data"
    }
    "data-alter" : {
        "foo" : "none"
        DATA_SEP : "Random Data"
    }
}
```
DATA_SET in the lib is '><'

#### Give in Xml :

```
<dict opt=nope opt-alter=nope>
    <data foo=none>Random Data</data>
    <data-alter foo=none>Random Data</data-alter>
</dict>
```
