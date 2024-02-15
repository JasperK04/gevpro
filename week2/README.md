# usage of programs

## cdb.py

the python program cdb.py returns all adjectives in a lexicon
This lexicon can be specified on the command line.
**Important is that this file is in xml format**
By default this lexicon is cdb-sample.xml

to run the program use:
```
python3 cdb.py [<lexicon>]
```

### options
use -h or --help to print the help
```
python3 cdb.py -h
python3 cdb.py --help
```

use -d or --debug to print extra information
```
python3 cdb.py -d [<lexicon>]
python3 cdb.py --debug [<lexicon>]
```


## anagrams.py

the python program anagrams.py returns all anagrams of a word that are found in a file.
The word has to be specified on the command line.
Optionally the filename can be specified on the command line.
**Important is that this file is in json format**
by default this file is words.json

Additionally you can specify a query file on the command line.
**Important is that this file is in txt format**
by default this file is query.txt

to run the program use:
```
python3 anagrams.py <word> [<file.json>] [<query.txt>]
```

### options
use -o or --one to print only the result of running the function find
this function takes a single word and returns its anagrams as a set
```
python3 cdb.py -o <word> [<file.json>] [<query.txt>]
python3 cdb.py --one <word> [<file.json>] [<query.txt>]
```

use -m or --many to print only the result of running the function find_many
this function takes the query and returns all anagrams as a dictionary
unfortunately a word still has to be specified even though it is not used
```
python3 cdb.py -m <word> [<file.json>] [<query.txt>]
python3 cdb.py --many <word> [<file.json>] [<query.txt>]
```

**if neither of these flags are set both functions will run**

use -t or --time to print the timed results
```
python3 cdb.py -t
python3 cdb.py --time
```

use -d or --debug to print extra information
**No other output than the debug information will be printed**
```
python3 cdb.py -d <word> [<file.json>] [<query.txt>]
python3 cdb.py --debug <word> [<file.json>] [<query.txt>]
```

use -h or --help to print the help
```
python3 cdb.py -h
python3 cdb.py --help
```