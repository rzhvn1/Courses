from rest_framework import serializers
from .models import Course, Contact, Branch, Category


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['type', 'value']

class BranchSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ['latitude', 'longtitude', 'address']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'img_path']



class CourseSerializer(serializers.ModelSerializer):

    contact = ContactSerializer(many=True)
    branch = BranchSerialiazer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'contact', 'branch']

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        branch_data = validated_data.pop('branch')
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        course = Course.objects.create(category=category,**validated_data)
        for contact in contact_data:
            Contact.objects.create(course=course, **contact)
        for branch in branch_data:
            Branch.objects.create(course=course, **branch)
        return course





