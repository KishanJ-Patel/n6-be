from rest_framework import serializers
from userProjectAccessApp.models import UserProjectAccess
from datetime import datetime


class UserProjectAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProjectAccess
        fields = ('id', 'user', 'project', 'access_url', 'otp', 'is_active')

    def create(self, validated_data):
        userProjectAccess = {}
        userProjectAccess['user'] = validated_data.get('user')
        userProjectAccess['project'] = validated_data.get('project')

        url = f"/user_id={userProjectAccess['user'].id}/project_id={userProjectAccess['project'].id}"
        userProjectAccess['access_url'] = url
        userProjectAccess['otp'] = 0000

        if (userProjectAccess['user'] is None):
            raise serializers.ValidationError(
                {'error': 'User Project Access must have a user id', 'status': 400})
        if (userProjectAccess['project'] is None):
            raise serializers.ValidationError(
                {'error': 'User Project Access must have a project id', 'status': 400})

        data = UserProjectAccess(**userProjectAccess)
        data.save()

        return data

    def update(self, instance, validated_data):

        instance.user = validated_data.get(
            'user', instance.user)
        instance.project = validated_data.get(
            'project', instance.project)

        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        if (validated_data.get('otp')):
            instance.otp = validated_data.get(
                'otp', instance.otp)
            instance.otp_updated_at = datetime.now()

        instance.save()
        return instance


