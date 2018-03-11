### Pre-requisites
Python 2.7 with pip

### Installation

#### 1) Clone this repo
```
git clone git@github.com:johnbk/clirpg.git
```
#### 2) Switch to the repo's root directory from terminal
```
cd clirpg
```

#### 3) Install virtualenv if not already installed
https://virtualenv.pypa.io/en/stable/installation/

#### 4) Create virtual environment
```
virtualenv venv
```

#### 5) Activate virutal environment
```
source venv/bin/activate
```

#### 6) Install depenedencies
```
pip install -r requirements.txt
```

### How to Run

#### Available commands

```
list-characters
list-places
play-character
explore-place
fight
reset
```

Example: On the terminal from the root of the repo
```
python zestwar.py list-characters
python zestwar.py list-places
python zestwar.py play-character luke
python zestwar.py epxlore-place naboo
python zestwar.py fight jabba
python zestwar.py reset
```


#### Get help for each command
```
python zestwar.py <command_name> --help
```



