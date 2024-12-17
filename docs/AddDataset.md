# Add a dataset

We are very keen to incorporate other published datasets on worm neuronal connectivity into this package and add them to this website. You can either A) add it yourself to the code, or B) tell us about it and we can add it for you. 

## A) Add it yourself

1) [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the [main repository](https://github.com/openworm/ConnectomeToolbox).

2) Add the source file of your dataset (usually the adjacency matrices of connection weights in, for example csv, Excel or Matlab format) into the [data folder](https://github.com/openworm/ConnectomeToolbox/tree/main/cect/data).

3) Create a Reader for the dataset, which converts it to our internal format. See examples for loading structured datasets in [CSV format](https://github.com/pgleeson/ConnectomeToolbox/blob/main/cect/Cook2020DataReader.py), [XLSX format](https://github.com/openworm/ConnectomeToolbox/blob/main/cect/Cook2019DataReader.py) or [XLS format](https://github.com/openworm/ConnectomeToolbox/blob/6847151db6a5dc9bc3fea1c5a40d01d1a6b024fa/cect/SpreadsheetDataReader.py). 

4) Add the new data reader to the list of readers in [Comparison.py](https://github.com/openworm/ConnectomeToolbox/blob/6847151db6a5dc9bc3fea1c5a40d01d1a6b024fa/cect/Comparison.py) (at 2 locations - see how Cook2020 is handled there).

5) Run [./test.sh](https://github.com/openworm/ConnectomeToolbox/blob/main/test.sh) in your local directory (or `./test.sh -q` for a quicker test) to install the latest version of the code and attempt to regenerate the website locally with your changes. 

6) Commit the code and [open a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to [https://github.com/openworm/ConnectomeToolbox](https://github.com/openworm/ConnectomeToolbox) with your changes. Note, enabling [GitHub Actions](https://github.com/features/actions) on the repository containing your fork will cause a number of [tests](https://github.com/openworm/ConnectomeToolbox/tree/main/.github/workflows) to be run automatically when you commit, which should pass before you open the pull request. 

## B) Tell us about the dataset

Please contact *p.gleeson AT ucl.ac.uk* with details of the missing resource (or just a link to the relevant publication) and we can discuss adding this to our codebase.

