from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_lessons_of_course = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_lessons_of_course(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('name', 'course_description', 'count_lessons_of_course', 'lessons')
