from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .merge import get_concat_v, get_concat_v_resize, get_concat_v_cut_center, customer
from PIL import Image
# Create your views here.
import os
from django.core.files.storage import default_storage
class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        if(request.data['title']=='head'):
            request.data['image'].name='head.png'
        else:
            request.data['image'].name='body.png'
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            
            if(request.data['title']=='body'):
                default_storage.delete('media/post_images/body.png')
                os.unlink('media/post_images/body.png')
                posts_serializer.save()
                # delete human.png
                default_storage.delete('media/merge/human.png')
                os.unlink('media/merge/human.png')
                im1 = Image.open('media/post_images/head.png')
                im2 = Image.open('media/post_images/body.png')
                
                im = Image.open('media/post_images/body.png')
                im.size  # (364, 471)
                # im2 = im.crop((0,im.getbbox()[1], im.width, im.height))
                im2 =im.crop(im.getbbox())
                im2.size  # (214, 178)
                im2.save('media/post_images/body.png')

                im = Image.open('media/post_images/head.png')
                im.size  # (364, 471)
                # im2 = im.crop((0,im.getbbox()[1], im.width, im.height))
                im1 =im.crop(im.getbbox())
                im1.size  # (214, 178)
                im1.save('media/post_images/head.png')
                # get_concat_v(im1, im2).save('media/merge/human.png')
                # get_concat_v_resize(im1, im2, resize_big_image=False).save('media/merge/human.png')
                customer(im1, im2).save('media/merge/human.png')
                # delete head, body
#                 im.size  # (364, 471)
# im.getbbox()  # (64, 89, 278, 267)
# im2 = im.crop(im.getbbox())
# im2.size  # (214, 178)
# im2.save("test2.bmp")
            else:
                default_storage.delete('media/post_images/head.png')
                os.unlink('media/post_images/head.png')
                posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# file = ContentFile("Hello world!")
# path = default_storage.save("path_to_file.txt", file)
# default_storage.delete(path)
# print default_storage.exists(path)