import json


def loads_json() -> list[dict]:
    try:
        with open('posts1.json', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except:
        print("Не удалось открыть или прочитать файл")


def get_search_word(word) -> list[dict]:
    posts = []
    for i in loads_json():
        if word.lower() in i['content'].lower():
            posts.append(i)
    return posts


def save_img(picture):
    filename = picture.filename
    picture.save(f'./uploads/images/{filename}')

    return str(f'/uploads/images/{filename}')


def save_post(post: dict) -> dict:
    posts: list[dict] = loads_json()
    posts.append(post)

    with open('posts1.json', "w", encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post






