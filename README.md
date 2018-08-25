# Github Python import hook

Did you know you can define how Python imports the code? Import hooks allow to overwrite its behaviour and let you define your own sources for loading the Python code.

This repository is an example of a Python import hook that allows loading python files directly from Github. No more clonning, no installing of the packages.

That may not work in some cases. It was tested with simple cases just to prove the concept. 

## Use manual

### Simple example

This one uses one of my repos with simple iteration.

1. Clone
1. Run: `python test_tqlol.py`
1. Read the code for your viewing pleasure

### Even more hilarious example

This example imports another repository modified by [@Overfl0](https://github.com/overfl0/), which is able to import python code directly from Stack Overflow (importception ;) ). In this case it imports a quick sort function found on StackOverflow and runs on a simple example. This may stop working if the StackOverflow answer is modified or voted down.

1. Clone (if you didn't before)
1. Run `python test_sort_over_stack_overflow_over_github.py`
1. Enjoy the StackOverflow importer sources at [@overfl0's Github](https://github.com/overfl0/stack_overflow_import)
