from eliza import Eliza
from UserInput import get_user_input
import subprocess
#import speech_recognition as sr


"""
Modeled on the original chatbot as well as the work of George Dunlop.

<p>
// This javascript version of ELIZA was originally written by
//   <a href="http://www.sabren.net/">Michal Wallace</a> and was significantly enhanced by
//   <a href="http://www.peccavi.com/">George Dunlop</a>.
// Eliza is a Classic Model of chat Bots.. but this implementation is mine :)
// May be used/modified if credit line is retained (c) 1997 All rights reserved

// converted to python
Robert Vanderwall
2020
"""


def show_response(resp):
    print(f"* {resp}")
    subprocess.call(['say', resp])


def get_response(context, e, in_text):
    if in_text == "bye":
        return True, "Bye"

    resp = e.listen(in_text)
    return False, resp


def loop():
    e = Eliza()
    done = False
    context = None
    show_response("Welcome, what is on your mind?")
    while not done:
        in_text = get_user_input("")
        done, resp = get_response(context, e, in_text)
        show_response(resp)


def main():
    loop()


if __name__ == "__main__":
    main()

