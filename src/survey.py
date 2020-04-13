import json
import requests
from sklearn.utils import shuffle

class Survey():
    def __init__(self, data):
        self.questions = data.questions
        self.answers = data.answers
        pass

    def transform_results(self, responses):
        survey_responses_corrected = {}
        for k, v in responses.items():
            if self.questions.loc[k, 'flip_scale'] == 1:
                if v == 0:
                    v = 4
                elif v == 1:
                    v = 3
                elif v == 3:
                    v = 1
                elif v == 4:
                    v = 0
                survey_responses_corrected[k] = v
            else:
                survey_responses_corrected[k] = v

        return survey_responses_corrected

    def take_survey(self):
        questions = shuffle(self.questions)
        survey_responses = {}

        # Print Questions and Answer choices, then prompt user for input
        for index, row in questions.iterrows():
            for index_a, row_a in self.answers.iterrows():
                print(index_a, "-", row_a['answer'])
                q = row['Question'] + ": "
            x = input(q)

            # Check to make sure the value from the user is an integer between 0 and 4
            while True:
                try:
                    n = int(x)
                except ValueError:
                    print('Value must be an integer between 0 and 4')
                    x = input(q)
                else:
                        if 0 <= int(n) <= 4:
                            survey_responses[index] = n
                            break
                        else:
                            print('Value must be an integer between 0 and 4')
                            x = input(q)

        # Pass the results back to Docker to get the results
        r = requests.post('http://35.237.214.19', json=self.transform_results(survey_responses))
        divorce_results = r.json()['divorce']

        return f'Your likelihood of divorce is {divorce_results * 100:.2f}%.'