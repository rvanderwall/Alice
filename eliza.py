from Strings import pad_string, unpad_string, remove_end_punctuation, get_text_after_keyword
from conjegations import conjugate
from keywords import find_response_for_keyword, KwResponse, NO_KEY_FOUND, find_response_for_repeated_phrase


class Eliza:
    def __init__(self):
        self.__greet = True

        self.__prev_working_text = None
        self.__sTopic = None
        self.__working_topic = None


    def listen(self, in_text):
        in_text = remove_end_punctuation(in_text.strip())
        working_text = pad_string(in_text.upper())
        if in_text == "":
            return "I can't help you if you won't talk to me"
        elif working_text == self.__prev_working_text:
            kword, kwr = find_response_for_repeated_phrase()
        else:
            kword, kwr = find_response_for_keyword(working_text)

        if kword == NO_KEY_FOUND:
            if self.__greet:
                self.__greet = False
                return "Don't you ever say Hello?"
            else:
                # save inputs for topics and repeats
                self.__prev_working_text = working_text
                if len(in_text) < 10 and self.__working_topic != "" and self.__working_topic != self.__prev_working_text:
                    l_topic = conjugate(self.__sTopic)
                    self.__sTopic = ""
                    self.__working_topic = ""
                    return 'OK... "' + l_topic + '". Tell me more.'
                else:
                    if len(in_text) < 15:
                        return "Tell me more"
                    else:
                        return self.form_response_text(in_text, kword, kwr)
        else:
            self.__greet = False
            if len(in_text) > 12:
                self.__working_topic = working_text
                self.__sTopic = in_text
            self.__prev_working_text = working_text
            return self.form_response_text(in_text, kword, kwr)

    def form_response_text(self, in_text, kwrd: str, kwr: KwResponse):
        response_text = kwr.get_next_response()
        last_char = response_text[-1]
        if last_char in ['*', '@']:
            in_text = pad_string(in_text)
            text_after_keyword = get_text_after_keyword(in_text, kwrd)
            conjugated_text = conjugate(text_after_keyword)
            conjugated_text = remove_end_punctuation(unpad_string(conjugated_text).strip())
            if last_char == '*':
                response_text = response_text.replace("<*", f" {conjugated_text}?")
            else:
                response_text = response_text.replace("<@", f" {conjugated_text}.")
            return response_text
        else:
            return response_text
