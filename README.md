# htt_plot

## Installation

* Go to lyovis10
* Clone this directory
* Put this package in your python path by doing: 

```
source ./init.sh
```

* Copy your small root files in this package, in a directory called `lucas_small` (see [components/lucas_small.py](components/lucas_small.py))

Also install [cpyroot](https://github.com/cbernet/cpyroot)

## Test

```
ipython -i macros/plot_inclusive.py 
```

## TODO

**You should disable parallel mode in the main macro for development and debugging**

* add the proper cross-section and generated number of events for the MC datasets 
* implement the final signal selection cut
* start implementing the various background estimation methods
