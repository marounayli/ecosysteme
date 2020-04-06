import requests
import datetime as dt


def logerrors(errors):
    error_log = open("log_creation_error.txt", "a")
    for error in errors:
        error_log.write(str(error[0]) + "##" +
                        str(error[1]) + ":"+str(dt.datetime.now())+"\n")
    error_log.close()


def logsuccesses(successes):
    success_log = open("log_creation_successes.txt", 'w')
    for success in successes:
        success_log.write(success[0] + "##" + success[2] +
                          "##" + success[1] + "##" + str(dt.datetime.now())+'\n')
    success_log.close()


def logActiveProbes(probes):
    active_probes = open("log_active_probes.txt", 'w')
    for probe in probes:
        active_probes.write(str(probe[0])+"-"+str(probe[1])+'\n')
    active_probes.close()
