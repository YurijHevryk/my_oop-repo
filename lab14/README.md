## Львівський Національний Університет Природокористування
## Кафедра Інформаційних Систем та Технологій



### Звіт про виконання лабораторної роботи №14
# "Принципи проєктування програмного забезпечення"



| **Виконав: студент групи ІТ-31 Юрій Геврик** |
|----------------------------------------------|
| **Перевірив: Татомир А. В.**                 |




**Мета: познайомитися з найбільш поширеними сучасними
принципами проєктування програмного забезпечення.**


Завдання:

1. Дати загальний опис принципів проєктування.
2. Дати детальний опис одного із принципів SOLID з наведення прикладу
коду.

**Опис принципів проектування**

S — Принцип єдиного обов'язку (Single Responsibility Principle, SRP)
«Модуль повинен мати одну і лише одну причину для змін». Іншими словами, модуль має відповідати лише за один аспект функціональності.
Метою принципу SRP є зменшення впливу змін в одній частині системи на функціонування інших частин. Порушення цього принципу призводить до ускладнення підтримки коду та ризику виникнення помилок та побічних ефектів.

O — Принцип відкритості для розширення, закритості для змін (Open/Closed Principle, OCP)
Принцип відкритості для розширення, закритості для змін (Open/Closed Principle, OCP). Проєктування програмних сутностей повинно дозволяти розширювати їх поведінку без необхідності змінювати вже існуючий код. Для досягнення цього часто застосовують принципи SRP і DIP.
Порушення цього принципу може призвести до необхідності змінювати код, який раніше стабільно працював, при кожному додаванні нової функціональності.

L — Принцип підставлення Лісков (Liskov Substitution Principle, LSP)
«Якщо тип S є підтипом T, то будь-які властивості, які задовольняють всі об'єкти типу T, повинні задовольняти всі об'єкти типу S».
Принцип LSP посилює вимоги до нащадка. Відомо, що заперечення наслідків призводить до заперечення передумов, тому цей принцип можна переформулювати так: «Якщо можна знайти властивість, яка задовольняє всі об'єкти типа Т і не задовольняє хоча б один об'єкт типу S, то не слід тип S наслідувати від типу Т».
Порушення принципу LSP може привести до порушення поліморфізму, коли об'єкт нащадка не зможе замінити об'єкт предка в певному контексті (програмі). Як приклад, порушенням принципу LSP можна назвати таке: є два класи «Квадрат» та «Прямокутник», якщо ми наслідуємо перший від другого (квадрат є окремим випадком прямокутника), то порушимо LSP тоді, якщо у прямокутника є функціональність зміни ширини без зміни висоти.

I — Принцип розділення інтерфейсу (Interface Segregation Principle, ISP)
«Клієнти не повинні залежати від методів, які вони не використовують». При проєктуванні інтерфейсів перевагу варто надавати створенню невеликих спеціалізованих інтерфейсів.
Якщо порушити цей принцип, код залежатиме від функціональності, яку він не використовує, і це ускладнюватиме супровід коду і слугуватиме потенційним джерелом помилок.

D — Принцип інверсії залежностей (Dependency Inversion Principle, DIP)
«Залежності в вихідному коді повинні бути спрямовані на абстракції, а не на конкретні реалізації». Це принцип, який дозволяє зменшити залежність між компонентами.

**Опис Open/Closed Principle**
Принцип відкритості/закритості стверджує, що програмні сутності (класи, модулі, функції тощо) мають бути відкритими для розширення, але закритими для модифікацій. Це означає, що ми повинні мати можливість розширювати функціональність класу без необхідності його безпосередньої зміни.
Основні характеристики

Розширюваність: Клас може отримувати нову функціональність через додавання нового коду, а не через зміну існуючого.
Стабільність: Базовий код залишається незмінним, що мінімізує ризик введення нових помилок у вже протестовану функціональність.

Механізми реалізації
Для впровадження цього принципу найчастіше використовуються такі підходи:
Абстракції та поліморфізм

Використання абстрактних класів та інтерфейсів
Створення розширень через успадкування або імплементацію інтерфейсів
Делегування спеціалізованої поведінки похідним класам


**Опис [коду](./14.py)**

Поліморфізм забезпечує гнучкість:
Функція calculate_employee_bonus викликає метод calculate_bonus, який визначений у кожному підкласі. Це дозволяє працювати з новими класами без змін у функції.

Існуючий код залишається стабільним:
Базовий клас Employee і вже створені підкласи (Senior, Middle, Junior) не потребують змін, якщо ми додаємо новий тип співробітника.

Функція calculate_employee_bonus не змінюється:
Вона використовує узагальнений підхід, працюючи з будь-яким об'єктом, що наслідує Employee.

Абстрактний базовий клас (Employee):
Декларує загальні методи та властивості, які повинні реалізувати всі підкласи.
Забезпечує контракт для майбутніх розширень, що запобігає необхідності змін у наявному коді.

Реалізація в підкласах:
Логіка обчислення бонусів для кожного типу співробітника ізольована в підкласах (Senior, Middle, Junior).

## Висновок:
На даній лабораторній роботі я ознайомився з основними принципами проєктування програмного забезпечення, SOLID. Детально розглянув Open/Closed Principle, який забезпечує відкритість коду для розширення функціональності та закритість для модифікації, що сприяє створенню стабільного, гнучкого та легко масштабованого програмного забезпечення.

