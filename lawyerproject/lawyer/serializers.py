from rest_framework import serializers
from lawyer.models import Lawyer


class LawyerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lawyer
        fields = ('id', 'url', 'first_name', 'last_name', 'speciality', 'mobile_number', 'email_address', 'lawyer_pic')