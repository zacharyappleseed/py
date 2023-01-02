# for testing purposes

from returnshellresult import runshellscript

script = "echo hiya!"
returnvalue = runshellscript(script)
outputstring = returnvalue[0].decode()
print(outputstring)