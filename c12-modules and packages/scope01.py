import mymod0

print("Hello from scope01.py. Let me call a function in mymod0...")
mymod0.mymod0_fun()

print("\nLet me try importing mymod0 a second time....")
import mymod0
print("Modules are only 'run' once when importing, so we see nothing here.")
