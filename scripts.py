#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from datacenter.models import (Chastisement, Commendation,
                               Lesson, Mark, Schoolkid)
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def check_student(Name):

    try:
        child = Schoolkid.objects.get(full_name__contains=Name)
        return child
    except MultipleObjectsReturned:
        raise Exception("Найдено два или более учеников")
    except ObjectDoesNotExist:
        raise Exception("Данный ученик не найден")


def fix_marks(Name):

    child = check_student(Name)
    Ivan_bad_marks = Mark.objects.filter(schoolkid_id=child.id, points__lt=4)

    for Ivan_bad_mark in Ivan_bad_marks:

        Ivan_bad_mark.points = 5
        Ivan_bad_mark.save()


def remove_chastisements(Name):

    child = check_student(Name)

    Ivan_Chastisements = Chastisement.objects.filter(schoolkid_id=child.id)
    Ivan_Chastisements.delete()


def create_commendation(Name, lesson_title):

    child = check_student(Name)
    letter = child.group_letter

    try:
        Lessons = Lesson.objects.get(year_of_study=6, group_letter=letter,
                                     subject__title__contains=lesson_title)
    except ObjectDoesNotExist:
        raise Exception("Введенный предмет не найден")

    list_praise = ["Молодец!", "Отлично!", "Хорошо!",
                   "Гораздо лучше, чем я ожидал!", "Приятно удивил!",
                   "Великолепно!", "Прекрасно!",
                   "Ты меня очень обрадовал!", "Очень хороший ответ!",
                   "Талантливо!", "Уже существенно лучше!", "Потрясающе!"]

    praise = random.choice(list_praise)

    Lessons_ordered = Lessons.order_by("-date")
    Lesson_date = Lessons_ordered[0].date
    Lesson_name = Lessons_ordered[0].subject
    Lesson_teacher = Lessons_ordered[0].teacher

    Commendation.objects.create(text=praise, created=Lesson_date,
                                schoolkid=child, subject=Lesson_name,
                                teacher=Lesson_teacher)


def update_all(Name="Фролов Иван", Lesson_title="Математика"):

    fix_marks(Name)
    remove_chastisements(Name)
    create_commendation(Name, Lesson_title)
