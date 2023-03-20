### db_hack

Данный проект создан для редактирования сайта электронного дневника. Репозиторий электронного дневника находится [здесь](https://github.com/devmanorg/e-diary/tree/master). Архив базы данных к нему можно найти по [следующей ссылке](https://dvmn.org/filer/canonical/1562234129/166/)
Данные скрипты выполняют следующие функции: 

* Редактирование оценок ниже "хорошо" на "Отлично";
* Удаление замечаний;
* Добавление одобрений;

Для корректной работы скриптов вам необходимо запустить интерактивную среду ```Django Shell``` и импортировать скрипты

Ниже описаны функции и пример запуска каждого скрипта. 


## check_student

Данный скрипт создан для проверки уникальности и существования ученика. 

В качетсве входного аргумента скрипт принимает ФИО ученика. В случае успешного выполнения скрипт вернет экземпляр модели ```Schoolkid```

В случае, если будет найдено больше одного ученика, то программа сообщит об этом. Также программа сообщит, если ученика с введенными данными не существует

Для запуска кода необходимо выполнить команду: 

```
scripts.check_student("Фролов Иван")
```
Пример запуска кода представлен ниже:

![image](https://user-images.githubusercontent.com/42433463/226237329-1299892a-0073-44fd-83c3-38e8b54215e7.png)


## fix_marks

Данный скрипт создан для редактирования оценок ниже "хорошо" на "отлично". 

В качетсве входного аргумента скрипт принимает ФИО ученика.

В случае, если будет найдено больше одного ученика, то программа сообщит об этом. Также программа сообщит, если ученика с введенными данными не существует

После выполнения скрипта оценки "неудовлетворительно" и "удовлетворительно" изменятся на "отлично" 

Для запуска кода необходимо выполнить команду: 

```
scripts.fix_marks("Фролов Иван")
```
Пример запуска кода представлен ниже:

![image](https://user-images.githubusercontent.com/42433463/226237914-aeaf69fc-352f-4287-8690-07a727cdccbd.png)


## remove_chastisements

Данный скрипт создан для удаления замечаний

В качетсве входного аргумента скрипт принимает ФИО ученика.

В случае, если будет найдено больше одного ученика, то программа сообщит об этом. Также программа сообщит, если ученика с введенными данными не существует

После выполнения скрипта все замечания будут удалены

Для запуска кода необходимо выполнить команду: 

```
scripts.remove_chastisements("Фролов Иван")
```
Пример запуска кода представлен ниже:

![image](https://user-images.githubusercontent.com/42433463/226238337-e0bd69ed-7aa9-4862-8387-ead9d556c346.png)


## create_commendation

Данный скрипт предназначен для добавления поощрений. 

В качетсве входного аргумента скрипт принимает ФИО ученика и название предмета.

В случае, если будет найдено больше одного ученика, то программа сообщит об этом. Также программа сообщит, если ученика с введенными данными не существует.
Если не будет найден введенный предмет, то программа также предупредит об этом.

После выполнения скрипта программа добавит поощрение по введеному уроку из уже готового списка поощрений

Для запуска кода необходимо выполнить команду: 

```
scripts.create_commendation("Фролов Иван", "Математика")
```
Пример запуска кода представлен ниже:

![image](https://user-images.githubusercontent.com/42433463/226239453-8d4fbef8-6ab8-4fce-9822-c80a50a485c0.png)


## update_all

Данный скрипт предназначен для выполнения всех описанных выше функций сразу. 

В качетсве входного аргумента скрипт принимает ФИО ученика и название предмета. По умолчанию ченика зовут "Фролов Иван", а прдемет для поощрений - "Математика"

В случае, если будет найдено больше одного ученика, то программа сообщит об этом. Также программа сообщит, если ученика с введенными данными не существует.
Если не будет найден введенный предмет, то программа также предупредит об этом.

После выполнит все 3 основные функции:

* Редактирование оценок ниже "хорошо" на "Отлично";
* Удаление замечаний;
* Добавление одобрений;

Для запуска кода необходимо выполнить команду: 

```
scripts.update_all("Фролов Иван","Математика")
```
Пример запуска кода представлен ниже:

![image](https://user-images.githubusercontent.com/42433463/226239749-6a37b673-9fae-4ab4-b492-54e8c51a38cc.png)



### Как установить

Для корректной работы программы вам необходимо выполнить все действия описанные в ссылке - документации электронного дневника. [Ссылка на документацию](https://github.com/devmanorg/e-diary/tree/master)

После этого потребуется скачать по [данной ссылке](https://dvmn.org/filer/canonical/1562234129/166/) базу данных и подключить ее. 

Затем вам будет необходимо запустить интерактивную среду ```Django Shell``` с помощью команды ```python manage.py shell``` и импортировать файл со скриптами с помощью команды import ```scripts```. 

Python3 должен быть уже установлен. 


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
