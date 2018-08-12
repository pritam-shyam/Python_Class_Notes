fun06.py### Modules, Scoping and namespaces

All Python files are modules. Any non-trivial Python program will start with a call to one module, but will most likely include other modules which in turn may call other modules.

We import a module using the import statement.

```
import somemodule # this "imports" somemodule.py code (located in the current directory) to be used within the current modules namespace.

dir(somemodule) # using the dir() function we can query the lost of names available in the imported modules global namespace.

somemodule.somefunction() # we can call functions found within the module using this format.

```

We can also import as

```
import somemodule as sm # this "imports" somemodule.py code (located in the current directory) to be used within the current modules namespace and renames the module sm.

dir(sm) # using the dir() function we can query the lost of names available in the imported modules global namespace.

sm.somefunction() # we can call functions found within the module using this format.

```

We can also import functions from the module into our current namespace


```
from somemodule import somefunction1, somefunction2

somefunction1()
somefunction2()
# Notice that since we have imported the functions into our current namespace (using the from/import command combination) we don't need to include the module name,

```
__NOTE:__ For more information on modules, please review  https://docs.python.org/3/tutorial/modules.html
