import TexttoSpeech
import wikipedia
from googlesearch import search

def wiki_search(spoken_text):
    try:
        result = wikipedia.summary(spoken_text, sentences=1)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]
        options_text = ", ".join(options)
        result_text = f"There are multiple options. Did you mean {options_text}?"
        return [result_text]
    except wikipedia.exceptions.PageError:
        search_results = search(spoken_text, num_results=10)
        TexttoSpeech.text_to_speech("Here are the top results.")
        results_list = []
        for result in search_results:
            results_list.append(result)
        return results_list


