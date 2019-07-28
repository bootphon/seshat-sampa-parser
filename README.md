# pyannote-extension-template

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

## Pyannote Configuration

To use the model contained in this library, this is the kind of configuration you
should add your `config.yml` file:

```yaml
pipeline_step_name:
  name: pyannote.submodule.MyClass
  params:
    param_1 : 1
    param_2 : some other string value
    param_3 : 4577
    
```

Be sure to add one or more sample configurations in the `sample_config` folder.
