from src.survey import Survey
from src.load_data import LoadData

loader = LoadData()
survey = Survey(loader)

survey.take_survey()
