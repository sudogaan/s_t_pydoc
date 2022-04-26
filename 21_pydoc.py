python -m pydoc

# to get the documentation of the math module, it describes each function it contains
python -m pydoc math

#the advantage of pydoc is you don't have to import a module to look a help text
#we can also use pydoc to search all modules for a certain keyword 

python -m pydoc -k ftp 
python -m pydoc ftplib #it gives examples

python -m pydoc -k sql

#you can use pydoc to start an HTTP server on the given port on the local machine
python -m pydoc -p 314 # this will start a server on port 314 and will give us a PO dock server on port p
#after running that code, python gives us the URL for browsing all the documentation, we can open a browser and type in the URL ourselves, or we can write b to the directory and python take us to the url


