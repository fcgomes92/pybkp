# PyBKP

How to run:

Clone this repository or download the pybkp.py file;

```
chmod +x pybkp.py
./pybkp.py <dir_path>
```

or

```
python3 pybkp.py  <dir_path>
```

After this, a file named dir_path.bkp.zip will be created in the parent directory of dir_path directory.

For some options you can check:

```
python3 pybkp.py -h
```

or

```
./pybkp.py -h
```

TODO:

- Better docs
- Finish backup file part
- Refactor code
- Make a PyPi package
- Auto create an linux alias
