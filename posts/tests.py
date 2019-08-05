from models import Post
from api.serializers import PostSerializer
p = Post.objects.first()
serializer = PostSerializer(p)
print(serializer.data)
print(serializer.data["slug"])





# from django.test import TestCase
#
# # Create your tests here.
# import json
#
# obj = {"test": False, "test2": False,}
#
# print(json.dumps(obj))
# print(isinstance(obj, dict))
# print(isinstance(json.dumps(obj), str))
#
# class Task:
#     def __init__(self, description, is_completed):
#         self.is_completed = is_completed
#         self.description = description
#
# task_str = '{"desc": "вымыть посуду", "done": false}'
#
# task_dict = json.loads(task_str)
#
# t = Task(task_dict["desc"], task_dict["done"])
# print(t.is_completed, t.description)