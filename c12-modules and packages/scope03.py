import mymodules2.mymod_2a
import mymodules2.mymod_2b
import mymodules3.mymod_2a
import mymodules3.mymod_2b

print("Hello from scope02.py.")

print("\n Let me call mymod_2a.mymod_1a_fun() from mymodules2 package...")
mymodules2.mymod_2a.mymod_2a_fun()

print("\n Let me call mymod_2b.mymod_1b_fun() from mymodules2 package...")
mymodules2.mymod_2b.mymod_2b_fun()

print("\n Let me call mymod_2a.mymod_1a_fun() from mymodules3 package... ")
mymodules3.mymod_2a.mymod_2a_fun()

print("\n Let me call mymod_2b.mymod_1b_fun() from mymodules3 package... ")
mymodules3.mymod_2b.mymod_2b_fun()

print("\n Here is the view of dir() in the main module...")
print(dir())
my_str = "Hello"
print("\n ... and after I create a var called my_str...")
print(dir())
