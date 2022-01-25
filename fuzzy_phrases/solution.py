import json
import re

pattern_segment = r'\s*\w*\s+'

def phrasel_search(P, Queries):
    # Write your solution here
    ans = [[]]
    for ij, sent in enumerate(Queries):
        result = []
        for phrase in P:
            temp_str = ""
            # retriece each wordf
            phrase_count = phrase.split(" ")
            for ix, word in enumerate(phrase.split(" ")):
                if ix < len(phrase_count)-1:
                    temp_str += word + pattern_segment
                else:
                    temp_str += word
            match = re.findall(temp_str, sent)
            if match:
                if len(ans) == 0:
                    ans[0] = match
                else:
                    try:
                        ans[ij] += match
                    except IndexError:
                        ans.append(match)
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
