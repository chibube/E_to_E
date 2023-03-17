import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #how our log file will be created
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE) #declaring a file path for the log file
os.makedirs(logs_path, exist_ok=True) #making the logfile directories and if there is already a file keep appending the new ones

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#creating the log
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", level=logging.INFO,

)

