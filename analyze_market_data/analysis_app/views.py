#from . import ai  # import the whole ai module
#print("AI module contents:", dir(ai))  #to print all list,functions and classes available in ai module


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from .ai import generate_analysis_with_gemini
from .news import fetch_sector_news
from .security import validate_sector

class AnalyzeSectorView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(ratelimit(key='user', rate='5/m', block=True)) #this is used to how a user can access endpoint.
    def get(self, request, sector):
        try:
            #if we are giving any sector other than pharmaceuticals, agriculture and technology, will print error
            if not validate_sector(sector):
                return Response({"error": "Invalid sector"}, status=400)

            # to get news
            news_data = fetch_sector_news(sector)

            # to get analysis from  Google Gemini
            markdown = generate_analysis_with_gemini(sector, news_data)

            # return markdown in response
            return Response({
                "sector": sector,
                "markdown_report": markdown
            })

        except Exception as e:
            return Response({"error": str(e)}, status=500)
        

# to check AnalyzeSectorView class is working
'''from django.http import JsonResponse
from django.views import View

class AnalyzeSectorView(View):
    def get(self, request, sector):
        return JsonResponse({"message": f"Analysis for {sector}"})'''
