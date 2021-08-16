from aiogram.types import InputFile

TASK_LIST = [
    'Нарисовать сигну с именем Weloxd где угодно, можно на руке, можно на бумаге.',
    'Прорыгать песню Mag.lo - Team',
    'Приготовить Ice-кофе: размешать 2 столовых ложки кипятка с чайной ложкой кофе и 3 чайными ложками сахара до однородной светло-коричнегой массы. Далее налить в кружку молоко, примерно 4/5 стакана, положить туда 2-3 кубика льда и залить всё получившимся раствором кофе. \nПоздравляю, теперь вы выпили отвар из ослиной мочи!!!',
    'Написать телеграмм бота на aiogram, который рассылает котиков',
    'Купить Monster',
    'Пока-кать. Да у этого бота актив как у пятиклассницы, кошмар'
]

KITTY_LIST = [
    'Смотри какой милый комок грязи!',
    'Сбрей всю шерсть',
    'Котяра ещё один',
    'Держи милоту',
    'Кот',
]

FILM_LIST = [
    {'caption': 'Остров проклятых',
     'photo': 'https://nedelya40.ru/wp-content/uploads/2020/06/a043d08784f871e307eb.jpg',
     'link': 'https://cc.lordfilm.energy/695-film-ostrov-prokljatyh-2009.html'
     },
    {'caption': 'Джентльмены',
     'photo': 'https://media.kg-portal.ru/movies/g/gentlemen/posters/gentlemen_15.jpg',
     'link': 'https://aug16.lordfilmaa.net/2082-7274-dzhentlmeny-23138.html'
     },
    {'caption': 'Воровка книг',
     'photo': 'https://cc.lordfilm.energy/uploads/posts/2021-03/1615901800-1784169493-vorovka-knig.jpg',
     'link': 'https://cc.lordfilm.energy/4544-film-vorovka-knig-2013.html'
     },
    {'caption': 'Лиза-лиса',
     'photo': InputFile('src/photos/liza-lisa.jpeg'),
     'link': 'https://hero.lordfilmq.net/16631-liza-lisa.html'
     },
    {'caption': 'Олдбой',
     'photo': 'https://cc.lordfilm.energy/uploads/posts/2020-10/d8721c47851ba6e4bb-oldboy.jpg',
     'link': 'https://cc.lordfilm.energy/2632-film-oldboj-2003.html'
     },
    {'caption': 'Мистический поезд',
     'photo': 'http://www.kinoglobe.ru/cinema/images/88595653f653afeba20a2c8934aeb869.jpg',
     'link': 'http://www.kinoglobe.ru/films/16372-tainstvennyy-poezd'
     },
]

ANIME_LIST = [
    {'caption': 'Atack of Titans',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_shingeki-no-kyojin.jpg',
     'season': {
         '1': [f'https://jut.su/shingeki-kyojin/season-1/episode-{ep}.html' for ep in range(1, 25 + 1)],
         '2': [f'https://jut.su/shingeki-kyojin/season-2/episode-{ep}.html' for ep in range(1, 12 + 1)],
         '3': [f'https://jut.su/shingeki-kyojin/season-3/episode-{ep}.html' for ep in range(1, 23 + 1)],
         '4': [f'https://jut.su/shingeki-kyojin/season-4/episode-{ep}.html' for ep in range(1, 16 + 1)]
     }
     },
    {'caption': 'Summer Wars',
     'photo': 'https://jut-su.net/image210x280/uploads/posts/2020-11/1605085795_poster.jpg',
     'link': 'https://jut-su.net/493-letnie-vojny.html'
     },
    {'caption': 'Банановая рыба',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_banana-fish.jpg',
     'episodes': [f'https://jut.su/banana-fish/episode-{ep}.html' for ep in range(1, 24 + 1)]
     },
    {'caption': 'Нана',
     'photo': 'https://yummyanime.club/img/posters/1589122009.jpg',
     'link': 'https://yummyanime.club/catalog/item/nana'
     },
    {'caption': 'Бродячие Псы',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_bungou-stray-dogs.jpg',
     'season': {
         '1': [f'https://jut.su/bungou-stray-dogs/season-1/episode-{ep}.html' for ep in range(1, 12 + 1)],
         '2': [f'https://jut.su/bungou-stray-dogs/season-2/episode-{ep}.html' for ep in range(1, 12 + 1)],
         '3': [f'https://jut.su/bungou-stray-dogs/season-3/episode-{ep}.html' for ep in range(1, 12 + 1)],
     }
     },
    {'caption': 'Кланнад',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_clannad.jpg',
     'season': {
         '1': [f'https://jut.su/clanad/season-1/episode-{ep}.html' for ep in range(1, 24 + 1)],
         '2': [f'https://jut.su/clanad/season-2/episode-{ep}.html' for ep in range(1, 25 + 1)],
         'Clanad film': 'https://jut.su/clanad/film-1.html',
     }
     },
    {'caption': 'Devil may cry',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_devil-may-cry.jpg',
     'episodes': [f'https://jut.su/devil-may-cry/episode-{ep}.html' for ep in range(1, 12 + 1)]
     },
    {'caption': 'Hellsing',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_hellsing.jpg',
     'episodes': [f'https://jut.su/hellsing/episode-{ep}.html' for ep in range(1, 13 + 1)]
     },
    {'caption': 'Дороро',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_dororo.jpg',
     'episodes': [f'https://jut.su/dororo/episode-{ep}.html' for ep in range(1, 24 + 1)]
     },
    {'caption': 'Дорохедоро',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_dorohedoro.jpg',
     'episodes': [f'https://jut.su/dorohedoro/episode-{ep}.html' for ep in range(1, 12 + 1)]
     },
    {'caption': 'Очень приятно - Бог',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_kamisama.jpg',
     'season': {
         '1': [f'https://jut.su/kamisama/season-1/episode-{ep}.html' for ep in range(1, 14 + 1)],
         '2': [f'https://jut.su/kamisama/season-2/episode-{ep}.html' for ep in range(1, 12 + 1)],
     }
     },
    {'caption': 'Хантер х Хантер',
     'photo': 'https://gen.jut.su/uploads/animethumbs/anime_hunter-x-hunter.jpg',
     'season': {
         '1': [f'https://jut.su/hunter-hunter/episode-{ep}.html' for ep in range(1, 148 + 1)],
         '1 фильм': 'https://jut.su/hunter-hunter/film-1.html',
         '2 фильм': 'https://jut.su/hunter-hunter/film-2.html',
     }
     },
]