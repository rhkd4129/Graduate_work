from PIL import Image

instance_1 =Image.open('C:\Python_1821028\django_project_1-main\duck_img_download\duck1.jpg')
#instance_2 =Image.open('C:\graduate_work\django_project_1-main\duck_img_download\duck1.jpg')


# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Image
# from .forms import ImageForm

# def upload(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             images = request.FILES.getlist('image_field_name')  # image_field_name에는 이미지를 업로드할 필드 이름을 넣어주세요.
#             for image in images:
#                 Image.objects.create(image=image)
#             return HttpResponse('Images uploaded successfully.')
#     else:
#         form = ImageForm()
#     return render(request, 'upload.html', {'form': form})

# Django에서 다중 이미지를 업로드하기 위해서는 MultiValueDict를 사용하여
#  여러 개의 파일을 받아올 수 있습니다. 이를 위해서 request.FILES.getlist() 
#  메서드를 사용하여 파일 리스트를 받아올 수 있습니다.

# 아래는 예시 코드입니다.
# 위 코드에서 Image는 이미지 모델입니다. ImageForm은 이미지 업로드를 위한 폼 클래스입니다. upload.html은 업로드 페이지를 렌더링하는 템플릿 파일입니다.

# 먼저, POST 요청이 들어오면 ImageForm 인스턴스를 생성하고, request.FILES.getlist() 메서드를 사용하여 업로드된 이미지 리스트를 받아옵니다. 그리고 받아온 이미지를 Image.objects.create() 메서드를 사용하여 모델에 저장합니다.

# 만약 폼이 유효하지 않으면 upload.html 템플릿 파일을 렌더링하여 폼을 다시 보여줍니다.

# 위 코드에서 'image_field_name'은 업로드할 필드 이름으로, 해당 필드의 이름으로 바꾸어주어야 합니다. 또한, 해당 뷰 함수에서 사용하는 모델과 폼 클래스는 각각 프로젝트에 맞게 수정하여 사용하시면 됩니다.





# Regenerate response

# from django import forms

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))