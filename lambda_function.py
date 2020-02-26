import json
import subprocess
import os
import shutil

# directory of the lambda function
LAMBDA_ROOT = os.environ.get('LAMBDA_TASK_ROOT', os.path.dirname(os.path.abspath(__file__)))

# directory where the executables originally is stored
ORIG_BIN_DIR = os.path.join(LAMBDA_ROOT, 'bin')

# directory where execution of binaries is allowed
EXEC_BIN_DIR = '/tmp/bin'

# name of the executable file
EXECUTABLE = 'gobin'

def _init_bin(executable_name):
    '''Copy the exectutable file to directory (BIN_DIR) where
    it is allowed to execute binaries. 
    '''
    
    # create the EXEC_BIN_DIR if not exists
    if not os.path.exists(EXEC_BIN_DIR):
        os.makedirs(EXEC_BIN_DIR)
        
    # copy the executable
    src_file = os.path.join(ORIG_BIN_DIR, executable_name)
    dest_file  = os.path.join(EXEC_BIN_DIR, executable_name)
    shutil.copy2(src_file, dest_file)

    # set executable mode for the binary
    os.chmod(dest_file, 0o0775)

    
def lambda_handler(event, context):
    
    # prepare the workspace
    _init_bin(EXECUTABLE)
    
    # call the executable
    cmdline = [os.path.join(EXEC_BIN_DIR, EXECUTABLE)]
    process = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    # process response
    json_string = process.communicate()[0]
    data = json.loads(json_string)
    return data


