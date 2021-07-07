import yaml


def read_meeting_description():
    with open('./config/agenda.yml', encoding='utf-8') as f:
        templates = yaml.safe_load(f)
    return templates
