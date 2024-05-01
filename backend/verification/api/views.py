from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.http import require_http_methods
from django.conf import settings

import json

from api.models import FileData
from api.serializers import FileDataSerializer


@require_http_methods(["POST"])
def upload_file(request):
    uploaded_file = request.FILES['file']
    new_file = FileData(file=uploaded_file)
    data = request.body
    print(data)

    data = json.loads(request.body)
    print(data)
    
    serializer = FileDataSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Upload successful'})
    return JsonResponse({'message': 'Upload failed'})
    # new_file.save()
    # return JsonResponse({'message': 'Upload successful'})
