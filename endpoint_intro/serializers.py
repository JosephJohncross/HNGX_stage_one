from rest_framework import serializers


class SlackSerializer(serializers.Serializer):
    """Serializes slack formatted output"""

    slack_name = serializers.CharField()
    current_day = serializers.CharField()
    utc_time = serializers.DateTimeField()
    track = serializers.CharField()
    github_file_url = serializers.CharField()
    github_repo_url = serializers.CharField()
    status_code = serializers.IntegerField()
