import requests
import datetime as dt


def logerrors(errors):
    error_log = open("log_creation_error.txt", "a")
    for error in errors:
        error_log.write(error[0] + "-" + error[1] +
                        ":"+str(dt.datetime.now())+"\n")
    error_log.close()


def logsuccesses(successes):
    success_log = open("log_creation_successes.txt", 'w')
    for success in successes:
        success_log.write(success +"-"+str(dt.datetime.now())+'\n')
    success_log.close()
