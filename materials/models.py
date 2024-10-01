from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    preview_image = models.ImageField(upload_to="course/image", verbose_name='Превью (картинка)', **NULLABLE)
    course_description = models.TextField(verbose_name='Описание курса', **NULLABLE)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    preview_image = models.ImageField(upload_to="lesson/image", verbose_name='Превью (картинка)', **NULLABLE)
    video_link = models.URLField()

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
