from rest_framework import serializers

from .models import Admin

class AdminRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    
    class Meta:
        model = Admin
        fields = ['email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def save(self):
        new_admin = Admin(email=self.validated_data['email'])
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        if password != password_confirm:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        new_admin.set_password(password)
        new_admin.is_admin = True
        new_admin.is_staff = True
        new_admin.is_superuser = True
        new_admin.save()
        return new_admin
