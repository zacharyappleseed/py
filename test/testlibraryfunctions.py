# for testing purposes

from advfunctions.shell import runshellscript
script = "echo hiya!"
returnvalue = runshellscript(script)
outputstring = returnvalue[0].decode()
print(outputstring)