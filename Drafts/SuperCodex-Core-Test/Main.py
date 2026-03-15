from Standards import *
import os

import requests
from sentence_transformers import SentenceTransformer
import numpy
import faiss

from Scripts.Logs import *
from Scripts.System_Prompts import *

ENCRYPTION_API = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjAzNjAzOTBhLTU0NTUtNDM0Ny05NzVlLTE5NTYwODgyYjc2YiIsImV4cCI6MTc3NTk1MTM4NiwianRpIjoiNTEyMDlmOTktZGI3Ni00Y2U1LWE5OWQtMDEyMDRjZmU2NWI3In0.UNqIDy_Kz8tuocHdnuBjkD2Q031GPvcUkxpVEp41uBc"
URL_ENDPOINT = "http://localhost:3000/api/chat/completions"
LLM_NAME = "gemma:latest"
SCRIPT_PATH_FOR_INPUT = "Input/Game.py"
SCRIPT_PATH_FOR_OUTPUT = "Output/Game.py"
PATH_OF_HOME_USER = OS_return_path_of_home_user()
PATH_OF_STE = f"{PATH_OF_HOME_USER}/Models/all-MiniLM-L6-v2"
MAX_NUMBER_OF_CHARACTERS_FOR_DIVIDE = 1250
TOP_K = 2
USER_PROMPT_FOR_INPUT = "Add \"Super Hard\" difficulty"

def Main_return_divide_of_script(script):

    loop = 0
    script_characters = ""
    script_part = []
    while loop < Python_length(script):
        script_characters += script[loop]
        if (
            Python_length(script_characters) == (
                MAX_NUMBER_OF_CHARACTERS_FOR_DIVIDE
            )
            or loop == Python_length(script) - 1
        ):
            script_part += [script_characters]
            script_characters = ""
        loop += 1

    return script_part


def Main_post_prompt(system_prompt_for_IDR):

    response, response_status_code, response_json = Requests_post(
        URL_ENDPOINT,
        headers={
            "Authorization": f"Bearer {ENCRYPTION_API}",
            "Content-Type": "application/json",
        },
        json={
            "model": LLM_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": system_prompt_for_IDR,
                }
            ],
        },
    )
    if response_status_code != 200:
        log_text = Python_fstring(f"""
Unexpected error occurred during requests_post()
URL_ENDPOINT:
{URL_ENDPOINT}

LLM_NAME:
{LLM_NAME}

USER_PROMPT_FOR_INPUT:
{USER_PROMPT_FOR_INPUT}

SYSTEM_PROMPT_FOR_IDR:
{system_prompt_for_IDR}

RESPONSE:
{response}

RESPONSE_STATUS_CODE:
{response_status_code}

RESPONSE_JSON:
{response_json}
""")
        Logs_log("ERROR", "LLM", log_text)

    return response, response_status_code, response_json


Logs_log("INFO", "MAIN", "Making sure \"output/\" directory exists")
path_of_output_directory = "output"
if OS_return_boolean_directory(path_of_output_directory) == False:
    OS_initialize_directory(path_of_output_directory)


Logs_log("INFO", "MAIN", "Loading input Python script...")
SCRIPT_INPUT = Python_read_file(SCRIPT_PATH_FOR_INPUT)


Logs_log("INFO", "MAIN", "Dividing input Python script into parts...")
LIST_OF_SCRIPT_PARTS = Main_return_divide_of_script(SCRIPT_INPUT)


TOTAL_NUMBER_OF_SCRIPT_PARTS = Python_length(LIST_OF_SCRIPT_PARTS)
STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS = (
    Python_string(TOTAL_NUMBER_OF_SCRIPT_PARTS)
)


Main = True

# Disable automatic pinging of HuggingFace servers by the
# "sentence_transformers" library
OS_environment("TRANSFORMERS_OFFLINE", "1")
OS_environment("HF_HUB_DISABLE_TELEMETRY", "1")
OS_environment("HF_HUB_DISABLE_TELEMETRY", "1")

boolean_of_loop_for_IDR = True
string_of_instruction_dependencies_with_line_numbers = ""
list_of_instruction_dependencies_with_line_numbers = []
loop = 0
boolean_of_loop_for_System_Prompts = False
loop_for_System_Prompts = 0
loop_for_IDR = 0
while Main == True:

    if boolean_of_loop_for_System_Prompts == True:
        loop = loop_for_System_Prompts
        instruction_dependencies = (
            System_Prompts_return_instruction_dependencies_for_system_prompt(
                SCRIPT_PATH_FOR_INPUT,
                string_of_instruction_dependencies_with_line_numbers
            )
        )
        boolean_of_loop_for_System_Prompts = False

    string_of_loop_for_IDR = Python_string(loop_for_IDR + 1) # "+ 1" because of
    # Python indexing ...
    while (
        loop < TOTAL_NUMBER_OF_SCRIPT_PARTS
        and boolean_of_loop_for_IDR == True
    ):
        log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}]
''''''
 Checking for missing instruction dependencies...
""")
        Logs_log("INFO", "MAIN", log_text)
        system_prompt_for_IDR, script_part_with_line_numbers = (
            System_Prompts_return_boolean_of_instruction_dependencies(
                list_of_instruction_dependencies_with_line_numbers,
                SCRIPT_PATH_FOR_INPUT,
                SCRIPT_INPUT,
                LIST_OF_SCRIPT_PARTS[loop],
                string_of_loop_for_IDR,
                STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS,
                USER_PROMPT_FOR_INPUT
            )
        )
        response, response_status_code, response_json = Main_post_prompt(system_prompt_for_IDR)
        if "YES" in response:
            log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Found instruction dependencies
""")
            Logs_log("INFO", "MAIN", log_text)
            log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Details about \"Found
''''''
 instruction dependencies\" \"System_Prompts_return_boolean_of_instruction_dependencies()\":
URL_ENDPOINT:
{URL_ENDPOINT}

LLM_NAME:
{LLM_NAME}

USER_PROMPT_FOR_INPUT:
{USER_PROMPT_FOR_INPUT}

SYSTEM_PROMPT_FOR_IDR:
{system_prompt_for_IDR}

RESPONSE:
{response}

RESPONSE_STATUS_CODE:
{response_status_code}

RESPONSE_JSON:
{response_json}
""")
            Logs_log("DEBUG", "LLM", log_text)
            if list_of_instruction_dependencies_with_line_numbers == [""]:
                list_of_instruction_dependencies_with_line_numbers = []
            list_of_instruction_dependencies_with_line_numbers += (
                [script_part_with_line_numbers]
            )
            boolean_of_loop_for_IDR = False
            loop_for_System_Prompts = (
                loop + 1
            )
            loop += 1
        elif "NO" in response:
            log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] No instruction dependencies.
""")
            Logs_log("INFO", "MAIN", log_text)
            log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Details about \"No instruction
''''''
 dependencies\" \"System_Prompts_return_boolean_of_instruction_dependencies()\":
URL_ENDPOINT:
{URL_ENDPOINT}

LLM_NAME:
{LLM_NAME}

USER_PROMPT_FOR_INPUT:
{USER_PROMPT_FOR_INPUT}

SYSTEM_PROMPT_FOR_IDR:
{system_prompt_for_IDR}

RESPONSE:
{response}

RESPONSE_STATUS_CODE:
{response_status_code}

RESPONSE_JSON:
{response_json}
""")
            Logs_log("DEBUG", "LLM", log_text)
            loop_for_System_Prompts = (
                loop + 1
            )
            loop += 1
        else:
            log_text = Python_fstring(f"""
IDR: LLM weight calculation failed during
''''''
 System_Prompts_return_boolean_of_instruction_dependencies():

''''''
URL_ENDPOINT:
{URL_ENDPOINT}

LLM_NAME:
{LLM_NAME}

USER_PROMPT_FOR_INPUT:
{USER_PROMPT_FOR_INPUT}

RESPONSE:
{response}

RESPONSE_STATUS_CODE:
{response_status_code}

RESPONSE_JSON:
{response_json}
""")
            Logs_log("ERROR", "LLM", log_text)

    if boolean_of_loop_for_IDR == False:
        log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Getting the instruction
''''''
 dependencies with line numbers...
""")
        Logs_log("INFO", "MAIN", log_text)
        system_prompt_for_IDR = (
            System_Prompts_return_list_of_instruction_dependencies_with_line_numbers(
                list_of_instruction_dependencies_with_line_numbers,
                SCRIPT_PATH_FOR_INPUT,
                list_of_instruction_dependencies_with_line_numbers[loop_for_IDR],
                string_of_loop_for_IDR,
                STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS,
                USER_PROMPT_FOR_INPUT
            )
        )
        response, response_status_code, response_json = Main_post_prompt(system_prompt_for_IDR)
        log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Got the raw instruction
''''''
 dependencies with line numbers. Details
''''''
 \"prompts_return_list_of_instruction_dependencies_with_line_numbers()\":
URL_ENDPOINT:
{URL_ENDPOINT}

LLM_NAME:
{LLM_NAME}

USER_PROMPT_FOR_INPUT:
{USER_PROMPT_FOR_INPUT}

SYSTEM_PROMPT_FOR_IDR:
{system_prompt_for_IDR}

RESPONSE:
{response}

RESPONSE_STATUS_CODE:
{response_status_code}

RESPONSE_JSON:
{response_json}
""")
        Logs_log("DEBUG", "LLM", log_text)
        log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Processing raw instruction
''''''
 dependencies with line numbers for next system prompt...
""")
        Logs_log("INFO", "MAIN", log_text)
        boolean_of_loop_for_IDR = True

        loop = 0
        boolean_of_first_character_of_line_number = False
        string_of_instruction_dependencies_with_line_numbers = ""
        while loop < Python_length(response):
            single_character_of_response = response[loop]
            if (
                single_character_of_response >= "0"
                and single_character_of_response <= "9"
            ):
                string_of_instruction_dependencies_with_line_numbers += (
                    response[loop]
                )
                boolean_of_first_character_of_line_number = True
            elif (
                single_character_of_response == ","
                and boolean_of_first_character_of_line_number == True
            ):
                string_of_instruction_dependencies_with_line_numbers += (
                    response[loop]
                )
            loop += 1
            
        loop = 0
        line_number_of_instruction_dependency = ""
        list_of_instruction_dependencies_with_line_numbers = []
        while loop < Python_length(string_of_instruction_dependencies_with_line_numbers):
            single_character_of_instruction_dependencies_with_line_numbers = (
                string_of_instruction_dependencies_with_line_numbers[loop:loop + 1]
            ) # "+ 1" because of Python indexing...
            if single_character_of_instruction_dependencies_with_line_numbers != ",":
                line_number_of_instruction_dependency += single_character_of_instruction_dependencies_with_line_numbers
            elif (
                single_character_of_instruction_dependencies_with_line_numbers == ","
                and line_number_of_instruction_dependency != ""
            ):
                list_of_instruction_dependencies_with_line_numbers += [Python_integer(line_number_of_instruction_dependency)]
                line_number_of_instruction_dependency = ""
            loop += 1

        loop = 0
        boolean_of_instruction_dependencies_with_line_numbers = True
        while loop < Python_length(list_of_instruction_dependencies_with_line_numbers):
            if Python_type(list_of_instruction_dependencies_with_line_numbers[loop]) != Python_data_type_integer:
                boolean_of_instruction_dependencies_with_line_numbers = False
                break
            elif (
                loop > 0
                and (
                    list_of_instruction_dependencies_with_line_numbers[loop]
                    <= list_of_instruction_dependencies_with_line_numbers[loop - 1]
                )
            ):
                boolean_of_instruction_dependencies_with_line_numbers = False
                break
            loop += 1

        if boolean_of_instruction_dependencies_with_line_numbers == True:
            log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Done processing instruction
''''''
 dependencies with line numbers for next system prompt
""")
            Logs_log("INFO", "MAIN", log_text)
            log_text = Python_fstring(f"""
IDR: [{string_of_loop_for_IDR}/
''''''
{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS}] Details about \"Done processing
''''''
 instruction dependencies with line numbers for next system prompt.\"
''''''
 \"prompts_return_list_of_instruction_dependencies_with_line_numbers()\":
URL_ENDPOINT:
{URL_ENDPOINT}

LLM_NAME:
{LLM_NAME}

USER_PROMPT_FOR_INPUT:
{USER_PROMPT_FOR_INPUT}

SYSTEM_PROMPT_FOR_IDR:
{system_prompt_for_IDR}

RESPONSE:
{response}

RESPONSE_STATUS_CODE:
{response_status_code}

RESPONSE_JSON:
{response_json}

STRING_OF_INSTRUCTION_DEPENDENCIES_WITH_LINE_NUMBERS:
{string_of_instruction_dependencies_with_line_numbers}
""")
            Logs_log("DEBUG", "LLM", log_text)
            list_of_instruction_dependencies_with_line_numbers += (
                [string_of_instruction_dependencies_with_line_numbers]
            )
            boolean_of_loop_for_Prompts = True
        elif boolean_of_instruction_dependencies_with_line_numbers == False:
            log_text = Python_fstring(f"""
IDR: LLM weight calculation failed during
''''''
 prompts_return_list_of_instruction_dependencies_with_line_numbers():

''''''
URL_ENDPOINT:
{URL_ENDPOINT}

LLM_NAME:
{LLM_NAME}

USER_PROMPT_FOR_INPUT:
{USER_PROMPT_FOR_INPUT}

SYSTEM_PROMPT_FOR_IDR:
{system_prompt_for_IDR}

RESPONSE:
{response}

RESPONSE_STATUS_CODE:
{response_status_code}

RESPONSE_JSON:
{response_json}

STRING_OF_INSTRUCTION_DEPENDENCIES_WITH_LINE_NUMBERS:
{string_of_instruction_dependencies_with_line_numbers}
""")
            Logs_log("ERROR", "LLM", log_text)

    loop_for_IDR += 1
    if (loop_for_IDR + 1) == TOTAL_NUMBER_OF_SCRIPT_PARTS:
        Main = False









































input("Reached the end of Main...")
print("Saving and loading Golang code output...")
open(PATH_FOR_SCRIPT_OUTPUT, "w").write(output); open(PATH_FOR_SCRIPT_OUTPUT).close()
golang_script = open(PATH_FOR_SCRIPT_OUTPUT, "r").read(output)
open(PATH_FOR_SCRIPT_OUTPUT).close()


print("Splitting Golang script into chunks...")
golang_script_chunks = return_divide_of_script(golang_script)


print("Loading embedding model...")
embedder = SentenceTransformer(PATH_OF_STE)


print("Embedding Python script chunks...")
python_script_chunk_embeddings = embedder.encode([python_script_chunks])
python_script_chunk_embeddings = numpy.array(
    python_script_chunk_embeddings
).astype("float32")

print("Preparing FAISS index...")
dimension = python_script_chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(python_script_chunk_embeddings)


print("Embedding Golang script chunk...")
golang_script_chunk_embeddings = embedder.encode([golang_script_chunks[0]])
golang_script_chunk_embeddings = numpy.array(
    golang_script_chunk_embeddings
).astype("float32")

print("Searching top chunks...")
distances, indices = index.search(golang_script_chunk_embeddings, TOP_K)
top_indices = indices[0]
similar_chunks = []
loop = 0
while loop < len(top_indices):
    chunk_index = top_indices[loop]
    chunk_text = python_script_chunks[chunk_index]
    similar_chunks.append(chunk_text)
    loop += 1










