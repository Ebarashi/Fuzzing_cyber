import datetime

""""
-----------------------------------------------------
 
  this function detect a fuzzing attack
  by checking the auth.log file for 
  incorrect use of ssh protocol
  
-----------------------------------------------------
"""


def fuzzing_checker():
    print("the detector is running....")
    while True:
        month = datetime.datetime.now().strftime("%b")
        day = str(datetime.datetime.now().day)
        err_counter = 0
        errors = ["Bad protocol version", "Connection closed by" "kex_exchange_identification", "kex_input_kexinit"]
        with open("/var/log/auth.log", "r") as auth_log:
            for line in auth_log:
                line_parts = str(line).split(" ")
                if line_parts[0] == month and line_parts[1] == day:
                    for error in errors:
                        if error in line:
                            err_counter += 1
                            if err_counter > 5:
                                print("**** Fuzzing Attack detected ****")
                                exit(1)


if __name__ == "__main__":
    fuzzing_checker()
