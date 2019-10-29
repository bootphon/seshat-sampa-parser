# seshat-parser-template

This is a template for any external class that would be needed at any step of the
pyannote pipeline. The classes that are defined in your extension can be then 
used through the `config.yml` file.

The name of submodule you use in the `pyannote/` folder should reflect what your
extension is about (`models`, `features`, `callbacks`, ...).
 

## Installation

Pyannote extensions usually require the
 [pyannote-audio](https://github.com/pyannote/pyannote-audio) environment to be installed
 and activated. Be sure to follow the installation instructions on the aforementioned's repo.
 
Once this is done (and the environment activated), you can install it through pip:

``` 
pip install git+git://github.com/pyannote/pyannote-myextension.git
``` 
