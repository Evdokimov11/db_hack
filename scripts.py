#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from datacenter.models import (Chastisement, Commendation,
                               Lesson, Mark, Schoolkid)


PRAISES = ["Молодец!", "Отлично!", "Хорошо!",
           "Гораздо лучше, чем я ожидал!",
           "Приятно удивил!", "Великолепно!",
           "Прекрасно!", "Ты меня очень обрадовал!",
           "Очень хороший ответ!", "Талантливо!",
           "Уже существенно лучше!", "Потрясающе!"]


def check_student(name):

    try:
        child = Schoolkid.objects.get(full_name__contains=name)
        return child
    except Schoolkid.MultipleObjectsReturned:
        raise Exception("Найдено два или более учеников")
    except Schoolkid.DoesNotExist:
        raise Exception("Данный ученик не найден")


def fix_marks(name):

    child = check_student(name)
    Mark.objects.filter(schoolkid_id=child.id, points__lt=4).update(points=5)


def remove_chastisements(name):

    child = check_student(name)

    chastisements = Chastisement.objects.filter(schoolkid_id=child.id)
    chastisements.delete()


def create_commendation(name, lesson_title):

    child = check_student(name)
    letter = child.group_letter
    year_of_study = child.year_of_study

    lessons = Lesson.objects.filter(year_of_study=year_of_study,
                                    group_letter=letter,
                                    subject__title__contains=lesson_title).order_by("-date")
    if not lessons:

        raise Exception("Введенный предмет у данного ученика не найден")

    praise = random.choice(PRAISES)

    lesson = lessons.first()
    lesson_date = lesson.date
    lesson_name = lesson.subject
    lesson_teacher = lesson.teacher

    Commendation.objects.create(text=praise, created=lesson_date,
                                schoolkid=child, subject=lesson_name,
                                teacher=lesson_teacher)


def update_all(name="Фролов Иван", lesson_title="Математика"):

    fix_marks(name)
    remove_chastisements(name)
    create_commendation(name, lesson_title)
