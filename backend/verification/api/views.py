from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings

import json

from api.models import FileData
from api.serializers import FileDataSerializer


@require_http_methods(["POST"])
@csrf_exempt
def upload_file(request):
    uploaded_file = request.FILES['file']
    data = request.body
    print(data)

    data = json.loads(request.body)
    print(data)
    
    file_type = request.POST.get('file_type', '')  # Получаем значение file_type из POST запроса
    doc_type = request.POST.get('doc_type', '')  # Получаем значение doc_type из POST запроса
    new_file = FileData(file=uploaded_file, file_type=file_type, doc_type=doc_type)

    new_file.save()

    serializer = FileDataSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Upload successful'})
    return JsonResponse({'message': 'Upload failed'}, status=400)        

