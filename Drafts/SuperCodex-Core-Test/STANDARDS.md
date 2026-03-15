

---

Author: devbyte1328

Document: STANDARDS.md

Version: 0.1.4

Last Updated: 15-03-2026

---

This document is for development purposes. If you are reading this, it is

probably because the document was added to a project, allowing readers to

reference the standards. Regardless of your motive, I hope you find value.

---

# The Truth Will Set You Free

Enough pretending. Software development lives in a fractured world. Languages,

frameworks, conventions, distributions. STOP. Keep naming them and you'll get

stuck in a forever loop. We tried to build a universal tower, and like the

builders of Babel, we now live with the consequences. Endless dialects, endless

disagreement, and endless reinvention. Understanding everything is impossible.

This document makes a simpler choice. It discards the majority of solutions and

bases everything on three core concepts, variables, functions, and

initialzations. It is not negotiable. It is set. The adherent must revert to

first principles. These standards will not appeal to everyone, and they are not

intended to.

---

# Purpose of This Document

This document sets standards for software development. The standards are

intended to allow most of the focus to be directed to the development of the

solution. The practice of these standards will have the adherent revert to

basics while preserving the capabilities of standardized technologies. The

author reserves the option to extend these standards to any technology,

technology stack, and general software development practices in future versions

of this document.

---

# Look into the fray before you jump in

Practicing these standards and onboarding to them is inconvenient and

difficult. This document redefines existing concepts and frequently violates

established nomenclature. This increases the difficulty of writing

documentation and communicating about the code with developers who are unaware

of, or unwilling to practice, these standards. There is a lot of overwritten

and excluded code, concepts, and conventions. Continuous maintenance of the

compatibility layer for these standards is required. And for the last part,

though it is more of a social issue than a practical one, during scrutiny you

are probably going to have to contend with arguments of "technology misuse". I

hope you are already used to the last part.

---

# But look on the bright side

After the onboarding process, the adherent gains the benefit of being able to

devote most of his time and energy to developing the solution rather than

contending with frequently occurring problems during development. The

filesystem and codebase become easier to read. Compatibility layers remove the

need to read documentation and/or learn the nomenclature of the imported

technology. Resolving multiple methodologies is no longer necessary (the

"multiple approaches to the same solution" problem). A coding style is

introduced, providing consistency within the code. And finally, it feels like

the "house is tidy."

---

## Definitions

### 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞

The core function that begins the compilation of functions passed into its

parameters.

### 𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧

The most basic unit of code. It can be written in a terminal or in scripts for

initialization.

### Base-Script

A base script is a Python script that provides reusable variables and functions

that are imported and used by other scripts within a project. It is not

intended to be executed directly as the primary entry point of the program.

### 𝐓𝐚𝐠-𝐋𝐢𝐬𝐭

Formerly known in Python as the data type *"Dictionary"*, a Tag-List is a

mutable, unordered collection of items, where each item consists of a unique

tag and a corresponding value. Tag-Lists allow fast retrieval of values based

on their tags.

### 𝐌𝐮𝐥𝐭𝐢-𝐖𝐨𝐫𝐝 𝐀𝐛𝐛𝐫𝐞𝐯𝐢𝐚𝐭𝐢𝐨𝐧

A shortened form created from multiple words by combining the initial

letters of each word. it refers to identifiers formed

from the first letters of a multi-word name.

### 𝐒𝐢𝐧𝐠𝐥𝐞-𝐖𝐨𝐫𝐝 𝐀𝐛𝐛𝐫𝐞𝐯𝐢𝐚𝐭𝐢𝐨𝐧

A shortened form created from a single word by reducing its length while

attempting to refer to that original word. it refers to

simplified identifiers derived from one word.

### 𝐇𝐲𝐩𝐞𝐫-𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞

A multi-purpose general language that is one level removed from practically

being a programming language. It can be used for both human-to-human and

human-to-LLM communication. On the complete opposite end of the

spectrum there is the "High-Level Language"/"Natural Language".

### 𝐇𝐢𝐠𝐡-𝐋𝐞𝐯𝐞𝐥 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞

A general language that MAY fall under the same definition as a human

language depending on the epistemology used to describe the definition.

On the complete opposite end of the spectrum there is the "Programming

Language", and one level before it is the "Hyper-Technical Language".

---

## Imported Standards

This document takes precedence over any imported standards.



### Semantic Versioning 2.0.0

Versioning scheme, full practice without any exception.

```
https://semver.org
```

### RFC 2119

Any protocol documentation.

```
https://rfc-editor.org/rfc/rfc2119
```

### Python PEP 8

Coding styles and/or conventions, except for parts that are overwritten or forbidden.

```
https://peps.python.org/pep-0008
```

---

## Naming Framework Standard

> [!NOTE]
> In the following standard, four terms are used to categorize different types of
> words and groups of words. These terms are made up and exist only as references
> for the categories, so don’t read too much into them. They slightly hint at how
> each category is used, but they are not meant to carry deeper meaning beyond
> that. Sorry if this is confusing, I didn’t have better terms to use for this
> part of the document. The terms are: "Functionist", "Dataist",
> "Categorizationist", and "Researchist".

### Description

The naming framework consists of three rules: Word Groups, Dataist Word Types,

and Connectors. A Word Group contains one or two words. Each word belongs to

one of two Dataist Word Types. Between each Word Group, one of three

Connectors is used.

#### Word Groups

- *`any base-script`***`(Functionist)`** The name of the base-script itself

    and "return" to disclose functions that return data.

- *`any words`***`(Dataist)`** - Contains any Categorizationist and/or

    Researchist word types.

#### Dataist Word Types

- *`any word`***`(Categorizationist)`** - A hyper-technical or high-level term

    that describes the stored value, function, or solution definition.
    
- *`any word`***`(Researchist)`** - a Mathematics or Technologies based term or

    data type that describes the stored value, function, or solution
    
    definition.

#### Connectors

- `of` - Bases the variable, function, solution definition, or data type to the

    word group on the right.
    
- `with` - Combines the left group with the right group.

- `for` - Describes what variable, function, or solution definition is to use

    the stored value.

### MUST ❗

- Put an underscore between each word.

- Uppercase every letter in any name that contains a multi-word abbreviation.

- Treat multi-word abbreviation names as a single Dataist-Categorizationist

    word type.

- Use only Categorizationist and Researchist word types for variables.

- Use Functionist and Dataist word groups for functions.

- For base-scripts with one or two words, uppercase the first letter of each

    word.

- Prefix the base-script name to all of its function names.

- Use return as the second word in a Functionist word group to indicate that

    the function returns data.

### MUST NOT ❗

- Use single-word abbreviations.

- Use the `for` connector with the name of the base-script in which it is

    defined.

- Use `of` to base a Functionist word group.

- Have the name surpess 79 characters.

### MAY ❗

- Use any number of words necessary to sufficiently describe a variable or

function (under 79 characters).

### Examples

Correct ✅

```
From Standards import *
import os

from Scripts.Logs import *
from Scripts.System_Prompts import *


PATH_OF_HOME_USER = OS_return_path_of_home_user()
PATH_OF_STE = f"{PATH_OF_HOME_USER}/Models/all-MiniLM-L6-v2"


def Logs_log(input_of_log_type, input_of_log_scope, input_of_log_text):
    pass


PATH_OF_HOME_USER = OS_return_path_of_home_user()
OS_initialize_directory("output")


instruction = ""
IDR = []
instruction_dependancies = ["abc", "def", "ghi"]

one_word = "script"
two_words = "script_path"
three_words = "path_of_script"
four_words = "path_of_python_script_for_LLM"
six_words = "path_of_python_script_with_line_numbers_for_LLM"
seven_words = "directory_path_of_python_scripts_with_line_numbers_for_LLM"
eight_words = "directory_path_of_python_scripts_with_prefix_of_line_numbers_for_LLM"
```

Wrong ❌

```
import os

from utils.logs import *
from utils.system_prompts import *

PATH_OF_SENTENCE_TRANSFORMER_ENCODER = os.path.expanduser("~\Models\all-MiniLM-L6-v2")

def log_for_Logs(input_log_type, input_log_scope, input_log_text):
    pass

os.makedirs("output", exist_ok=True)

Instruction = ""
instruction_dependancy_resolutions = []
ID = ["abc", "def", "ghi"]

one_word = "Script"
two_words = "Script_Path"
three_words = "LLM_Script_Path"
four_words = "LLM_python_script_path"
six_words = "LLM_python_scripts_prefixed_with_line_numbers"
```

Correct ✅
```
.
...
├── Documentations
│   ├── STANDARDS.md
│   └── USEFUL_RESOURCES.md
├── .git
├── .gitignore
├── .Immutables.py
...
├── Logs
│   ├── LLM.log
│   └── Main.log
├── Main.py
...
├── README.md
├── Scripts.pip
├── Standards.py
├── Scripts
│   ├── Logs.py
│   └── System_Prompts.py
...
```

Wrong ❌
```
.
...
├── doc
│   ├── standards.md
│   └── ur.md
├── .git
├── .gitignore
├── .immutables.py
...
├── logs
│   ├── llm.log
│   └── main.log
├── init.py
...
├── readme.md
├── requirements.txt
├── standards.py
├── utils
│   ├── logs.py
│   └── system_prompts.py
...
```

---

## Working Directory Standards

### Description

Filsystems and Codebases.

#### Standards.py

`Standards.py` acts as the compatibility layer for the standards, a crude and

brutish way of applying them to Python. When writing code or importing scripts,

first update the compatibility layer to include any necessary corrections. To

access the standardized definitions in a target script, include the following

at the top of the file: `from Standards import *`

**Template**

<details><summary>🔽 CLICK TO EXPAND SCRIPT... 🔽</summary>

```


# Python

Python_data_type_integer = int
Python_data_type_float = float
Python_data_type_string = str
Python_data_type_boolean = bool
Python_data_type_list = list
Python_data_type_tag_list = dict

import importlib.util
def Python_load_immutables(immutable_data):
    spec = importlib.util.spec_from_file_location(
        "immutables",
        os.path.join(os.path.dirname(__file__), ".immutables.py")
    )
    immutables = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(immutables)
    immutable_data = getattr(immutables, immutable_data)
    return immutable_data

def Python_print(any_value):
    print(any_value)

def Python_integer(any_value):
    return int(any_value)
    
def Python_float(any_value):
    return float(any_value)
    
def Python_string(any_value):
    return str(any_value)
    
def Python_boolean(any_value):
    return bool(any_value)
    
def Python_list(any_value):
    return list(any_value)

def Python_tag_list(any_value):
    return dict(any_value)

def Python_return_tags_of_list(any_value):
    return list(dict(any_value).keys())

def Python_fstring(string_value):
    loop = 0
    temporary_hold_of_single_quotes = ""
    was_single_quotes_found = False
    was_f_string_divider_found = False
    text_for_output = ""
    while loop < len(string_value):
        if temporary_hold_of_single_quotes == "''''''":
            was_f_string_divider_found = True
        if was_f_string_divider_found == False:
            if was_single_quotes_found == False:
                if string_value[loop:loop + 1] != "'":
                    text_for_output += string_value[loop:loop + 1]
                elif string_value[loop:loop + 1] == "'":
                    was_single_quotes_found = True
                    temporary_hold_of_single_quotes += (
                        string_value[loop:loop + 1]
                    )
            elif was_single_quotes_found == True:
                if string_value[loop:loop + 1] != "'":
                    text_for_output += temporary_hold_of_single_quotes
                    text_for_output += string_value[loop:loop + 1]
                    temporary_hold_of_single_quotes = ""
                    was_single_quotes_found = False
                elif string_value[loop:loop + 1] == "'":
                    temporary_hold_of_single_quotes += (
                        string_value[loop:loop + 1]
                    )
        elif was_f_string_divider_found == True:
            text_for_output = text_for_output[:-1]
            was_double_quotes_found = False
            was_f_string_divider_found = False
            temporary_hold_of_single_quotes = ""
        loop += 1
    return text_for_output[1:-1]

def Python_read_file(FILE_PATH):
    open_file = open(FILE_PATH, "r").read()
    open(FILE_PATH).close()
    return open_file

def Python_read_binary_of_file(FILE_PATH):
    open_file = open(FILE_PATH, "rb").read()
    open(FILE_PATH).close()
    return open_file
    
def Python_write_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "a").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_write_binary_of_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "ab").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_overwrite_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "w").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_overwrite_binary_of_file(FILE_PATH, STRING_VALUE):
    open(FILE_PATH, "wb").write(STRING_VALUE)
    open(FILE_PATH).close()

def Python_type(ANY_VALUE):
    return type(ANY_VALUE)

def Python_length(ANY_VALUE):
    return len(ANY_VALUE)


import os

def OS_exit_Main():
    os.sys.exit()

def OS_environment(ANY_TAG, ANY_VALUE):
    os.environ[ANY_TAG] = ANY_VALUE

def OS_initialize_directory(directory_path):
    os.makedirs(directory_path)

def OS_return_boolean_filesystem(filesystem_path):
    return os.path.exists(filesystem_path)

def OS_return_boolean_file(file_path):
    return os.path.isfile(file_path) 

def OS_return_boolean_directory(directory_path):
    return os.path.isdir(directory_path)

def OS_return_list_of_directory_files(directory_path):
    return os.listdir(directory_path)

def OS_delete_file(file_path):
    os.remove(file_path)

def OS_return_path_of_home_user():
    return os.path.expanduser("~")

def OS_return_absolute_path(relative_path_of_filesystem):
    return os.path.abspath(relative_path_of_filesystem)

def OS_return_resolution_path_of_symbolic_link(relative_path_of_symbolic_link):
    return os.path.realpath(relative_path_of_symbolic_link)

def OS_return_function_parameters():
    return os.sys.argv


import subprocess

def SubProcess_Initialize(functions):
    subprocess.run(functions, shell=True)

def SubProcess_Parallel_Initialize(functions):
    subprocess.Popen(functions, shell=True)


import signal

def Signal_signal(signal_type, function):
    signal.signal(signal_type, function)

def Signal_return_signal_for_interruption():
    return signal.SIGINT

def Signal_return_signal_for_termination():
    return signal.SIGTERM


```

</details>

#### .Immutables.py

`Tuples` and `Frozen Dataclasses` are not recognized as immutable data types

under these standards, and their use is forbidden. At the time of writing,

Python does not provide true immutable data types. However, the concept of

immutability can improve code readability by expressing intent more clearly.

For this reason, developers are encouraged to experiment with fake immutables.

To use fake immutables, create `.Immutables.py` in the working directory. This

script stores the fake immutable values that will be exposed. In the target

script, use `from Standards import *` all the way at the top. Pass the fake

immutable reference to `Python_load_immutables()` and assign the returned value

to the constant.

#### While Function

Before using a `while` function, initialize a `loop` counter variable. Use this

counter in the while function condition. Place variables used exclusively by

the while function between the counter initialization and the `while`

statement. This visually groups them with the while function and indicates they

are only relevant to that while function. Increment the `loop` counter at the

end of the while function body using exactly one level of indentation.

### MUST ❗

- Have `Standards.py` contain two empty lines above and below the script, each

    script import section must contain two empty lines above and below, each

    function must contain one empty line above and below, no empty lines inside the

    functions, each function has to begin with the name of the base script being

    standardized.

- Have `Main.py` serve as the entry point script.

- Have `Main.py` be the location where the public API is declared.

- Have `Main.py` and `README.md` declare the version.

- Have the working directory contain the files, "STANDARDS.md", "Standards.py",

    "README.md", "Main.py", ".git", ".gitignore"

- Apply compatibility workarounds to imported technologies so they comply with

    these standards (In Python, this is implemented through `Standards.py`.)

- Maintain a maximum line length of 79 characters.

    If a variable name causes a line to exceed this limit, shorten the
    
    variable name by removing unnecessary words.
    
- For functions that resolve conditions:

    `if` for the primary intended data manipulation.

    `elif` for following cases.

    `else` only when absolutely necessary.

    `raise` only with Python's standard exception hierarchy:

    `https://docs.python.org/3/library/exceptions.html#exception-hierarchy`

- Add a comment after the index explaining any `+1` or `-1` correction made due

    to Python's zero-based indexing.

- Only code with Python data types: "Integers", "Floats", "Strings",

    "Booleans", "Lists", and "Tag-Lists".

- Only code with Python Functions: "Imports", "Built-in", "Base-script",

    "Whiles", "Ifs", "Elifs", "Elses", "Ins", "Not Ins", "Trys",
    
    "Excepts", "Finallys", and "Raises".

- Have `README.md` at the very least include initialization instructions

     written in a hyper-technical language for private solutions.

- Have `README.md` include initialization instructions in `README.md` written

    in a high-level language for public solutions.

- Ignore the non-standardized names of automatically generated filesystems.

- Use `/` when defining filesystem path values.

- For filesystem names, Uppercase the first letter of each major word, use

    lowercase for minor words, Separate all words with underscores.

- Uppercase all letters for Markdown filenames.

- Use `Virtual_Environment` to name the Python virtual environment.

- Use the file `Scripts.pip` for storing Python scripts imported with `pip`.

- Version control Python scripts imported with `pip` in `Scripts.pip`.

- Uppercase the entire `.Immutables.py`.

- Have `.Immutables.py` contain two empty lines above and two empty lines below

    the script.  

- Prefix every constant in `.Immutables.py` with `IMMUTABLE`.

### MUST NOT ❗

- Use the file `requirements.txt` for storing pip-managed Python scripts. 

- Use `venv` to name the Python virtual environment.

- Use `\` when defining filesystem path values.

- Leave Python scripts imported with `pip` in rolling release.

- Use the file `requirements.txt` for storing Python scripts imported with `pip`.

- Use the Imports: "pathlib", "sys", and "shutil".

- Use the legacy Python functions: "Classes", "Frozen Dataclasses", "Tuples",

    "Object Methods", "Lambdas", "For Loops", "Is".

- Nest While functions that isn't Main.

- Pass functions into functions.

- Have functions returns functions.

- Use Dunders.

- Using `not` before `in`.

- Modify the base of the imported technology to enforce these standards.

- Include empty lines between code lines in `.Immutables.py`.

### MAY ❗

- `Standards.py` ca be placed either in the working directory or inside the
    `Documentations/` directory.

- Have working directory include "Dockerfile" to address compatibilities.

### Examples

Correct ✅

> Using `Standards.py` to standardize Python functions.


Wrong ❌

> Using `CPython` to fix Python for compliance with these standards.

Correct ✅

`.Immutables.py`

```


LIST_DEBUG = ["DEBUG"]
LIST_OF_ERROR_CRITICAL = ["ERROR", "CRITICAL"]


```

`Scripts/Log.py` ("Main.py" initializes "Log.py")

```
from Standards import *


IMMUTABLE_LIST_DEBUG = Python_load_immutables("LIST_DEBUG")
IMMUTABLE_LIST_OF_ERROR_CRITICAL = Python_load_immutables("LIST_OF_ERROR_CRITICAL")


LIST_OF_LOG_TYPES = (
    IMMUTABLE_LIST_DEBUG
    + ["INFO", "WARNING"]
    + IMMUTABLE_LIST_OF_ERROR_CRITICAL
)
```

Wrong ❌

`Scripts/Log.py`

```
IMMUTABLE_LIST_DEBUG = ["DEBUG"]
IMMUTABLE_LIST_OF_ERROR_CRITICAL = ["ERROR", "CRITICAL"]

LIST_OF_LOG_TYPES = (
    IMMUTABLE_LIST_DEBUG
    + ["INFO", "WARNING"]
    + IMMUTABLE_LIST_OF_ERROR_CRITICAL
)
```

Correct ✅

```
string_of_loop_for_IDR = Python_string(loop_for_IDR + 1)
# "+ 1" because of Python indexing...
```

Wrong ❌

```
string_of_loop_for_IDR = Python_string(loop_for_IDR + 1)
```

Correct ✅

```
loop = 0
loop_for_line_number = 0
last_of_line_number = 10
script = "import os; print("hello world")..."
line_number = loop_for_line_number
while loop < last_of_line_number:
    if script[loop] == "\n":
        line_number += 1
    loop += 1
    
```

Wrong ❌

```
line_number = loop_for_line_number
for loop in range(last_of_line_number):
    if script[loop] == "\n":
        line_number += 1
```

Correct ✅
```
.
...
├── .git
├── .gitignore
...
├── LICENSE
...
├── __pycache__
...
└── Virtual_Environment
```

Wrong ❌
```
.
...
├── License
...
└── venv
```

---


