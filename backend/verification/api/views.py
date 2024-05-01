from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings

import json

from api.models import FileData
from api.serializers import FileDataSerializer
from api.verification import verify_document


@require_http_methods(["POST"])
@csrf_exempt
def upload_file(request):
    uploaded_file = request.FILES['file']
    
    file_type = request.POST.get('file_type', '')  # Получаем значение file_type из POST запроса
    doc_type = request.POST.get('doc_type', '')  # Получаем значение doc_type из POST запроса
    new_file = FileData(file=uploaded_file, file_type=file_type, doc_type=doc_type)

    if (upload_file is None) or (not upload_file):
        return JsonResponse({
            'is_uploaded': False,
            "is_valid": False,
            "message": [] 
            }, status=400)   
         
    new_file.save()
    print(new_file.file.name)

    is_valid, message = verify_document(file_type, new_file.file.name, doc_type)

    return JsonResponse({
        'is_uploaded': True,
        'is_valid': is_valid,
        'message': message
        }, status=201)
