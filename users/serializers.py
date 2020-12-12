from rest_framework import serializers
from .models import Profile,User
import django.contrib.auth.password_validation as validators

# from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= ['user','bio','avatar']
        
class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= ['bio','avatar']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username','email','first_name','last_name','password']

 
        
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields= ['username','email','first_name','last_name','password','confirm_password']
        
    def validate_password(self,password):
        
        if not self.initial_data.get('password') or not self.initial_data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if self.initial_data.get('password') != self.initial_data.get('confirm_password'):
            raise serializers.ValidationError("Passwords doesn't match.")
        try:
            validators.validate_password(password)
        except validators.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return password

    def create(self,validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)

        user.set_password( validated_data['password'])
        user.save()
        return user