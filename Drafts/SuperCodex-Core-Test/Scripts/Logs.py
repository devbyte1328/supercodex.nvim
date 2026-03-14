from Standards import *
import os
import datetime


IMMUTABLE_LIST_DEBUG = load_immutables("LIST_DEBUG")
IMMUTABLE_LIST_OF_ERROR_CRITICAL = load_immutables("LIST_OF_ERROR_CRITICAL")


SAVE_LOGS = False
DEBUG_MODE = True
LOG_TYPE = "ERROR"
LIST_OF_LOG_TYPES = (
    IMMUTABLE_LIST_DEBUG
    + ["INFO", "WARNING"]
    + IMMUTABLE_LIST_OF_ERROR_CRITICAL
    # "IMMUTABLE_LIST_DEBUG" must stay on the left of "LIST_OF_LOG_TYPES"
    # and "IMMUTABLE_LIST_OF_ERROR_CRITICAL" must stay to the right of
    # "LIST_OF_LOG_TYPES" because of sequence dependancy
)
LOG_SCOPES = {
    "MAIN": "Logs/Main.log",
    "LLM": "Logs/LLM.log"
}
TAGS_OF_LOG_SCOPE = Python_tag_list(LOG_SCOPES)


def Logs_spaces_for_readability_of_logs(input_log, log_values):

    loop = 0
    total_amount_of_spaces = 0
    while loop < Python_length(log_values):
        if Python_length(log_values[loop]) > total_amount_of_spaces:
            total_amount_of_spaces = Python_length(log_values[loop])
        loop += 1

    output_text = Python_string(input_log)
    while Python_length(output_text) < total_amount_of_spaces:
        output_text = output_text + " "

    return output_text


def Logs_log(input_of_log_type, input_of_log_scope, input_of_log_text):

    if Python_type(LOG_SCOPES) == Python_type(None):
        text_of_value_error = Python_fstring(f"""
Invalid LOG_SCOPES '{LOG_SCOPES}'. LOG_SCOPES cannot be empty
""")
        raise ValueError(text_of_value_error)

    loop = 0
    while loop < Python_length(TAGS_OF_LOG_SCOPE):
        tag_for_loop = TAGS_OF_LOG_SCOPE[loop]
        value_for_loop = LOG_SCOPES[tag_for_loop]
        if Python_type(value_for_loop) == Python_type(None):
            text_of_value_error = Python_fstring(f"""
Invalid LOG_SCOPES value '{value_for_loop}' for key '{tag_for_loop}'
""")
            raise ValueError(text_of_value_error)
        if "/" in value_for_loop and value_for_loop[:5] != "logs/":
            text_of_value_error = Python_fstring(f"""
Invalid LOG_SCOPES path '{value_for_loop}'. Path must be in working directory 
''''''
or inside 'logs/'
""")
            raise ValueError(text_of_value_error)
        loop += 1

    if input_of_log_type not in LIST_OF_LOG_TYPES:
        text_of_value_error = Python_fstring(f"""
Invalid log type '{input_of_log_type}'. Allowed: {LIST_OF_LOG_TYPES}
""")
        raise ValueError(text_of_value_error)

    loop = 0
    available_log_scopes = []
    while loop < Python_length(TAGS_OF_LOG_SCOPE):
        available_log_scopes += [TAGS_OF_LOG_SCOPE[loop]]
        loop += 1

    if input_of_log_scope not in available_log_scopes:
        text_of_value_error = Python_fstring(f"""
Invalid log scope '{value_error_text}'. Allowed: {available_log_scopes}
""")
        raise ValueError(text_of_value_error)

    if DEBUG_MODE == False and input_of_log_type == "DEBUG":
        return

    loop = 0
    boolean_priority_of_log_type_for_input = None
    boolean_priority_of_log_type_for_loop = None
    while loop < Python_length(LIST_OF_LOG_TYPES):
        if LIST_OF_LOG_TYPES[loop] == input_of_log_type:
            boolean_priority_of_log_type_for_input = loop
        if LIST_OF_LOG_TYPES[loop] == LOG_TYPE:
            boolean_priority_of_log_type_for_loop = loop
        loop += 1

    if boolean_priority_of_log_type_for_input >= boolean_priority_of_log_type_for_loop:
        return

    log_type_output = Logs_spaces_for_readability_of_logs(input_of_log_type, LIST_OF_LOG_TYPES)
    log_scope_output = Logs_spaces_for_readability_of_logs(input_of_log_scope, TAGS_OF_LOG_SCOPE)
    log_output = Python_fstring(f"""
[{str(datetime.datetime.now())}] [{log_type_output}] [{log_scope_output}] 
''''''
{str(input_of_log_text)}
""")
    log_path = LOG_SCOPES[input_of_log_scope]
    Python_write_file(log_path, log_output + "\n")
    Python_print(log_output)
    if input_of_log_type in IMMUTABLE_LIST_OF_ERROR_CRITICAL:
        raise RuntimeError(log_output)

directory_path_of_logs = "logs"
if OS_return_boolean_directory(directory_path_of_logs) == False:
    OS_initalize_directory(directory_path_of_logs)
if SAVE_LOGS == False:
    loop = 0
    LOG_FILES = OS_return_list_of_directory_files("logs")
    while loop < Python_length(LOG_FILES):
        OS_delete_file(f"logs/{LOG_FILES[loop]}")
        loop += 1
elif SAVE_LOGS == True:
    pass
else:
    raise ValueError("SAVE_LOGS must be True or False")


