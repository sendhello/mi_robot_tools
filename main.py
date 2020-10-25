# Скачать голосовые пакеты в папку voice_packages по ссылке https://yadi.sk/d/osWtpE1PrxCu0Q?w=1
# заполнить параметры ip, token и vois
# token можно узнать из кастомного mi home (https://www.kapiba.ru/2017/11/mi-home.html)

import os
from enum import Enum


class Vois(Enum):
    RU_OFF_2008_LOUDER = 'Ru_off_2008_louder.pkg'  # Официальная русская озвучка для прошивки 2008 с поднятой громкостью
    RU_OFFICIAL = 'ru_official.pkg'  # Официальная русская озвучка
    RU_OUTSIDEPRO_UNIVERSAL = 'ru_outsidepro_universal.pkg'  # Мужской голос (живой)
    RUSSIAN = 'russian.pkg'  # женский голос
    MAXIM = 'maxim.pkg'  # Мужской голос (Максим)
    RU_LEATHER_BASTARDS = 'ru_leather_bastards.pkg'  # Мужской голос (Максим, нецензурная лексика)
    RU_SCARLETT_FOR_1GEN = 'ru_scarlett_for_1gen.pkg'  # Женский голос (Алиса)
    RU_OKSANA = 'ru_Oksana.pkg'  # Женский голос (Оксана)
    RU_ROBOT = 'ru_robot.pkg'  # Робот
    RU_ALISA_GLADOS = 'ru_alisa+glados.pkg'  # Алиса+GLaDOS из Portal
    LEATHER_BASTARDS_MAX = 'leather_bastards_max.pkg'  # Языковый пакет "Кожаные Ублюдки" от @bartwell с увеличенной громкостью
    LESHA_2 = 'Lesha_2.pkg'  # Леша
    BRUT_2 = 'Brut_2.pkg'  # Брутал
    STRAJY_1 = 'Strajy_1.pkg'  # Стражи галактики
    EN_ME_HARBRINGER = 'en_me_harbringer.pkg'  # Озвучка Коллекционеров из Mass Effect 2
    RUBB8_ALICE = 'ruBB8_Alice_2008_12012020.pkg'  # Озвучка дроида BB-8 из Star Wars
    RU_MAX_BASTARD = 'ru_max_bastard.pkg'  # Язык. пакет в стиле "Кожаные ублюдки" (много мата)
    RU_RICK_AND_MORTY = 'ru_rick_and_morty.pkg'  # Языковой пакет "Рик и Морти"
    UA_NORMALIZE_COMPRESSION = 'ua_normalize_compression.pkg'  # Украинский официал
    UKRAINIAN = 'ukrainian.pkg'  # Софiя (укр)
    RUSSIAN_2 = 'russian-2.pkg'  # Бендер из Футурамы


ip = '192.168.2.34'
token = '3648784b594569674c5a6d6744514a6f'
vois = Vois.RU_MAX_BASTARD.value


os.system("mirobo discover --handshake true")
os.system(f"mirobo --ip={ip} --token={token} status")  # Тест на коннект
os.system(f"mirobo --ip={ip} --token={token} install-sound vois_packages/{vois}")
