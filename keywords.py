

class KwResponse:
    def __init__(self, keywords, responses):
        if isinstance(keywords, str):
            self.keys = [keywords,]
        if isinstance(keywords, list):
            self.keys = keywords      # Phrase to match
        self.next = 0     # Next response to use
        self.responses = responses

    def get_next_response(self):
        if self.next > len(self.responses):
            self.next = 0
        resp = self.responses[self.next]
        self.next += 1
        return resp


def find_response_for_keyword(in_text: str) -> (str, KwResponse):
    # Find a keyword match to the users input text
    upper_text = in_text.upper()
    for kwr in __keywords:
        for kw in kwr.keys:
            if kw in upper_text:
                return kw, kwr
    return NO_KEY_FOUND, _no_keyword_found_resp


def find_response_for_repeated_phrase() -> (str, KwResponse):
    return REPEATED_INPUT, _repeated_input_resp


NO_KEY_FOUND="NO KEY FOUND"
REPEATED_INPUT="REPEATED INPUT"

__keywords = [
    KwResponse("CAN YOU", ["Don't you believe that I can<*",
                        "Perhaps you would like to be able to<*",
                        "You want me to be able to<*"
    ]),
    KwResponse("CAN I",   ["Perhaps you don't want to<*",
                        "Do you want to be able to<*"
    ]),
    KwResponse(["YOU ARE", "YOU'RE"], ["What makes you think I am<*",
                        "Does it please you to believe I am<*",
                        "Perhaps you would like to be<*",
                        "Do you sometimes wish you were<*"
    ]),
    KwResponse("I DON'T", ["Don't you really<*",
                        "Why don't you<*",
                        "Do you wish to be able to<*",
                        "Does that trouble you?"
    ]),
    KwResponse("I FEEL", ["Tell me more about such feelings.",
                        "Do you often feel<*",
                        "Do you enjoy feeling<*"
    ]),
    KwResponse("WHY DON'T YOU", ["Do you really believe I don't<*",
                        "Perhaps in good time I will<@"
                        "Do you want me to<*"
    ]),
    KwResponse("WHY CAN'T I", ["Do you think you should be able to<*",
                        "Why can't you<*"
    ]),
    KwResponse("ARE YOU", ["Why are you interested in whether or not I am<*",
                        "Would you prefer if I were not<*",
                        "Perhaps in your fantasies I am<*"
    ]),
    KwResponse("I CAN'T", ["How do you know you can't<*",
                        "Have you tried?",
                        "Perhaps you can now<*"
    ]),
    KwResponse(["I AM", "I'M"], ["Did you come to me because you are<*",
                        "How long have you been<*",
                        "Do you believe it is normal to be<*",
                        "Do you enjoy being<*"
                        ]),
    KwResponse("YOU",     ["We were discussing you, not me.",
                        "Oh... <*",
                        "You're not really talking about me, are you?"
                        ]),
    KwResponse("I WANT",  ["What would it mean to you if you got<*",
                        "Why do you want<*",
                        "Suppose you got<*",
                        "What if you never got<*",
                        "I sometimes also want<@"
                    ]),
    KwResponse(["WHAT", "HOW", "WHO", "WHERE", "WHEN", "WHY"],
                       ["Why do you ask?",
                        "Does that question interest you?",
                        "What answer would please you the most?",
                        "What do you think?",
                        "Are such questions on your mind often?",
                        "What is it that you really want to know?",
                        "Have you asked anyone else?",
                        "Have you asked such questions before?",
                        "What else comes to mind when you ask that?",
                       ]),
    KwResponse("NAME", ["Names don't interest me.",
                        "I don't care about names, please go on."
                        ]),
    KwResponse("CAUSE", ["Is that the real reason?",
                        "Don't any other reasons come to mind?",
                        "Does that reason explain anything else?",
                        "What other reasons might there be?"
                    ]),
    KwResponse("SORRY", ["Please don't apologise!",
                        "Apologies are not necessary.",
                         "What feelings do you have when you apologise?",
                         "Don't be so defensive!"
                    ]),
    KwResponse("DREAM", ["What does that dream suggest to you?",
                        "Do you dream often?",
                      "What persons appear in your dreams?",
                       "Are you disturbed by your dreams?"
                    ]),
    KwResponse(["HELLO","HI"], ["How are you today.. What would you like to discuss?",
                    ]),
    KwResponse("MAYBE", ["You don't seem quite certain.",
                        "Why the uncertain tone?",
                        "Can't you be more positive?",
                        "You aren't sure?",
                       "Don't you know?"
                    ]),
    KwResponse("NO", ["Are you saying no just to be negative?",
                        "You are being a bit negative.",
                        "Why not?",
                        "Are you sure?",
                        "Why no?",
                    ]),

    KwResponse("YOUR", ["Why are you concerned about my<*",
                    "What about your own<*"
                   ]),
    KwResponse("ALWAYS", ["Can you think of a specific example?",
                        "When?",
                        "What are you thinking of?",
                        "Really, always?",
                     ]),
    KwResponse("THINK", ["Do you really think so?",
                       "But you are not sure you think<*",
                       "Do you doubt that<*",
                       ]),
    KwResponse("ALIKE", ["In what way?",
                      "What resemblence do you see?",
                      "What does the similarity suggest to you?",
                      "What other connections do you see?",
                      "Could there really be some connection?",
                      "How?",
                      "You seem quite positive.",
                      ]),
    KwResponse("YES", ["Are you Sure?",
                      "I see.",
                      "I understand.",
                      ]),
    KwResponse("FRIEND", ["Why do you bring up the topic of friends?",
                      "Do your friends worry you?",
                      "Do your friends pick on you?",
                      "Are you sure you have any friends?",
                      "Do you impose on your friends?",
                      "Perhaps your love for friends worries you.",
                      ]),
    KwResponse("COMPUTER", ["Do computers worry you?",
                    "Are you talking about me in particular?",
                    "Are you frightened by machines?",
                    "Why do you mention computers?",
                    "What do you think machines have to do with your problems?",
                    "Don't you think computers can help people?",
                    "What is it about machines that worries you?",
                    ]),
]

_no_keyword_found_resp = KwResponse(NO_KEY_FOUND, ["Say, do you have any psychological problems?",
                         "What does that suggest to you?",
                         "I see.",
                         "I'm not sure I understand you fully.",
                         "Come, come, elucidate your thoughts.",
                         "Can you elaborate on that?",
                         "That is quite interesting.",
                         ]),

_repeated_input_resp = KwResponse(REPEATED_INPUT, ["Why did you repeat yourself?",
                             "Do you expect a different answer by repeating yourself?",
                             "Come, come, elucidate your thoughts.",
                             ]),
