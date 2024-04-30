from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import UploadedFile

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        new_file = UploadedFile(file=uploaded_file)
        new_file.save()
        return JsonResponse({'message': 'Upload successful'})
    return JsonResponse({'message': 'Upload failed'}, status=400)
