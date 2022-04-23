import json


def load_candidates(path):
    """ Загружаем данные из .json файла"""
    with open(path, 'r', encoding='utf-8') as candidates_file:
        return json.load(candidates_file)


candidates_list = load_candidates('candidates.json')


def sort_by_name(candidate_name):
    """ Возвращает данные кандидата по имени"""
    result_name = []
    for candidate in candidates_list:
        if candidate_name.lower() in candidate['name'].lower():
            result_name.append(candidate)

    return result_name


def sort_by_id(candidate_id):
    """ Возвращает данные кандидата по id"""
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not_found': 'Кандидата с таким id нет'}


def sort_by_skill(skill):
    """ Возвращает кандидатов по навыку"""
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if skill in candidate_skills:
            result.append(candidate)

    return result
