from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


#For registering user
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)  # Making email required

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def validate_email(self, value):
        # Checking if there is already a user with the same email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value


#This serializer register a user with his company 
class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Company
        fields = ('user', 'name', 'address')

    def create(self, validated_data):
        try:
            user_data = validated_data.pop('user')
            company_name = validated_data['name']

            if not Company.objects.filter(name=company_name).exists():#Checking if there is dublicate company name
                user = User.objects.create_user(**user_data)#regidtring user
                company = Company.objects.create(user=user, **validated_data)#creating company instance correnponsing to user
                Staff.objects.create(user=user, company=company)#this will create the company owner as staff
            else:
                raise serializers.ValidationError("A company with this name already exists.")

        except Exception as e:
            raise serializers.ValidationError({e})
        return company


#just for getting a company custome object
class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)

#This serializer register a user with his corresponding company as staff
class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanyNameSerializer()

    class Meta:
        model = Staff
        fields = ('user', 'company', 'address')

    def create(self, validated_data):
        try:
            user_data = validated_data.pop('user')
            company_data = validated_data.pop('company')
            user = User.objects.create_user(**user_data)
            company = Company.objects.get(name=company_data['name'])
            staff = Staff.objects.create(user=user, company=company, **validated_data)

        except Exception as e:
            raise serializers.ValidationError({e})
        return staff

#Creating employee corresponding company 
class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        exclude = ('id','company')

    def create(self, validated_data):
        user=self.context['request'].user #getting loged in user
        try:
            staff = user.staffs_user.first()
            company = staff.company
            validated_data['company'] = company
            employee = Employee.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({e})
        return employee

#Serializer for asset to corresponding comapny
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        exclude = ('id', 'company')

    def create(self, validated_data):
        user=self.context['request'].user #getting loged in user
        try:
            staff = user.staffs_user.first()
            company = staff.company

            validated_data['company'] = company
            asset = Asset.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({e})
        return asset

#Serializer for asset to corresponding employee
class AssetLogSerializer(serializers.ModelSerializer):
    #getting instance by primary key
    #asset = serializers.PrimaryKeyRelatedField(queryset=Asset.objects.all())
    #employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    
    #getting instance by related_name with field name
    asset = serializers.SlugRelatedField(slug_field='name', queryset=Asset.objects.all())
    employee = serializers.SlugRelatedField(slug_field='name', queryset=Employee.objects.all())
    
    class Meta:
        model = AssetLog
        fields = ('asset', 'employee', 'checkout_quantity', 'checkout_time', 'checkout_condition', 'chekout_note', 'duration', 'is_returned', 'return_time', 'return_quantity', 'return_condition', 'returned_note')

    def create(self, validated_data):
        try:
            user=self.context['request'].user #getting loged in user
            staff = user.staffs_user.first()
            company = staff.company
            validated_data['company'] = company

            assetlog = AssetLog.objects.create(checkout_by_staff=staff,**validated_data)

        except Exception as e:
            raise serializers.ValidationError(str(e))
        return assetlog