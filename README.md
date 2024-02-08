# Python JSON Parser

This project takes a JSON file OR a JSON string and creates an Excel file of the structure.

## Requirements
* Make sure you have the correct packages installed.
    - I've used a ```Conda``` env, here is the ```environment.yml``` if you want the same setup.
    - Open your terminal
    - Navigate to this folder
    - ```conda env create -f environment.yml```
    - Wait untill the env has been created
    - ```conda activate py-json-parser```

<br />

* Make sure you use valid JSON
    - Use double quotes to wrap your keys and text values
    - Use ```false``` and ```true``` (NOT capitalised)
    - Use ```null```instead of ```None```
    - Here is a [great validator](https://jsonlint.com/)
    - And a [minifier](https://codebeautify.org/jsonminifier)
        - You need to minify your JSON if you want to copy-paste a JSON string in the terminal


## How to use
You can use 2 options in this tool: insert a JSON file or a JSON string. In both cases you'll need **valid** JSON! Once the script has run, you will find a ```json-parser.xlsx``` in the root of this folder.

### Option 1: Use a JSON file
```python script.py -f /path/to/file.json```

### Option 2: Use a JSON string
```python script.py -s '{"key": "value"}'```

## Screenshot
![Code Result](/screenshot-code-result.png?raw=true "Code Result")