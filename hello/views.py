import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def append_to_file(request):
    print("LL")
    if request.method == 'POST':
        if 'stringToAppend' in request.POST:
            string_to_append = request.POST['stringToAppend']
        else:
            try:
                data = json.loads(request.body.decode('utf-8'))
                string_to_append = data['stringToAppend']
            except (KeyError, ValueError):
                return JsonResponse({'error': 'Invalid request. "stringToAppend" is required.'}, status=400)

        desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'android')
        file_path = os.path.join(desktop_dir, 'stats.txt')

        # Create the directory if it doesn't exist
        if not os.path.exists(desktop_dir):
            os.makedirs(desktop_dir)

        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            open(file_path, 'w').close()

        # Append the string to the file
        with open(file_path, 'a') as file:
            file.write(string_to_append + '\n')

        return JsonResponse({'message': 'String appended to the file successfully.'}, status=200)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)