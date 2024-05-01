from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import UploadedFile

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        file_type = request.POST.get('file_type', '')  # Получаем значение file_type из POST запроса
        doc_type = request.POST.get('doc_type', '')  # Получаем значение doc_type из POST запроса
        new_file = UploadedFile(file=uploaded_file, file_type=file_type, doc_type=doc_type)
        new_file.save()
        return JsonResponse({'message': 'Upload successful'})
    return JsonResponse({'message': 'Upload failed'}, status=400)

