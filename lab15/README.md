## Львівський Національний Університет Природокористування
## Кафедра Інформаційних Систем та Технологій



### Звіт про виконання лабораторної роботи №15
# "Рефакторинг програмного забезпечення"



| **Виконав: студент групи ІТ-31 Юрій Геврик** |
|----------------------------------------------|
| **Перевірив: Татомир А. В.**                 |




**Мета: познайомитися з основними принципами та найбільш
поширеними техніками рефакторингу програмного забезпечення..**


Завдання:

1. Дати загальний опис принципів рефакторингу.
2. Ознайомитися із основними техніками рефакторингу.
3. Познайомитися із поняттям “запахів коду”.

**Опис принципів рефакторингу**

Рефакторинг є важливою практикою в розробці програмного забезпечення, спрямованою на покращення внутрішньої структури коду без зміни його зовнішньої поведінки.
Метою рефакторингу є підвищення якості та чистоти коду, спрощення структури програмного забезпечення, полегшення підтримки та розширення коду, зменшення технічного боргу та спрощення подальшої модифікації системи.
Ключовими принципами рефакторингу є послідовність та систематичність.Process повинен виконуватися поступово, невеликими кроками, причому кожна зміна має бути мінімальною та перевіреною. Важливою умовою є підтримка працездатності коду на кожному етапі перетворень.
Критеріями успішного рефакторингу є перетворення коду на більш читабельний, легкий для розуміння, простий у модифікації, ефективний та менш схильний до появи помилок.
Важливо дотримуватися застережень: не змінювати код без вагомих причин, не додавати нову функціональність, бути обережним з впливом на продуктивність системи та погоджувати значні зміни з командою розробників.

## Основні техніки рефакторингу.

Винесення методу: розділення великого методу на менші, більш спеціалізовані методи для підвищення читабельності та модульності коду.

Переміщення методу:переміщення методу до класу, де він логічно повинен знаходитися, для покращення організації коду та зменшення зчеплення.

Видалення подвійного коду: усунення повторюваних блоків коду шляхом створення спільних методів або використання спадкування.

Спрощення умовних конструкцій: розбиття складних умовних операторів на простіші, більш зрозумілі частини, використання поліморфізму замість численних перевірок.

Інкапсуляція поля: приховання прямого доступу до полів класу через приватні змінні та створення getter/setter методів.

## Запахи коду.

Запахи коду - це характеристики вихідного коду, які вказують на потенційні проблеми в його структурі, потребують рефакторингу та можуть ускладнювати підтримку та розвиток програмного забезпечення.
Характеристики запахів коду:

Природа виникнення: Не є безпосередніми помилками, Сигналізують про приховані недоліки архітектури,
Потребують уваги розробників, Можуть призводити до складнощів у подальшому супроводженні коду

Основні категорії запахів коду: Структурні запахи:Надмірна складність методів, Великі класи,
Глибока вкладеність успадкування, Забагато параметрів у методах, Надлишкові коментарі
Об'єктно-орієнтовані запахі:Божественний об'єкт (клас, що виконує забагато функцій),
Глибока ієрархія успадкування, Жорстке зчеплення класів, Порушення принципів SOLID

Архітектурні запахі: Заплутані залежності між модулями, Відсутність чіткої межі відповідальності,
Складність розуміння логіки системи

**[Код до рефакторингу](./15_before.py)**
**[Код після рефакторингу](./15_after.py)**

## Опис коду
Техніки рефакторингу:
Інкапсуляція (Encapsulation):
Створення класів User та UserManager
Приховання внутрішньої реалізації
Контрольований доступ до даних

Виділення методу (Extract Method):
Розділення логіки на окремі методи
Метод _generate_next_id() для генерації ID
Метод find_users_by_criteria() для гнучкого пошуку

Використання лямбда-функцій:
Заміна жорстко заданих умов на динамічні критерії
Підвищення гнучкості пошуку користувачів

Принцип єдиної відповідальності (Single Responsibility):
Клас User відповідає за представлення користувача
Клас UserManager відповідає за управління колекцією користувачів

Поліморфізм:
Реалізація методу __str__ для зручного виведення
Використання генератора списків для фільтрації

## Висновок:
На даній лабораторній роботі я опанував навички роботи з принципами покращення внутрішньої структури коду без зміни його зовнішньої поведінки
Дізнався про техніки рефакторингу, оволодів методами виділення та переміщення методів
Набув навички боротьби з дублюванням коду, вивчив принципи спрощення умовних конструкцій та інкапсуляції

