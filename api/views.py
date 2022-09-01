from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal , Rating
from .serializers import MealSerializer,RatingSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import request,status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    @action(detail=True,methods =['post'])
    def rate_meal(self , request , pk=None):
        if 'stars' in request.data :
            
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print(user)
            try:
                rating = Rating.objects.get(user=user,meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating,many=False)
                json ={
                    'message':'Meal rate updated',
                    'result': serializer.data
                }
                return Response (
                    json , 
                    status = status.HTTP_200_OK
                )
            except:
                rating = Rating.objects.create(meal=meal,user=user,stars=stars)
                serializer = RatingSerializer(rating,many=False )
                json ={
                    'message':'rate created',
                    'result':serializer.data
                }
                return Response(
                    json ,
                    status = status.HTTP_200_OK
                )
            
        else:
            json ={
                'message':'stars not provided'
            }
            return Response(
                json,
                status = status.HTTP_400_BAD_REQUEST
            )
                
        
        
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def create(self,request,*args,**kwargs):
        response ={
            'message' : 'Invalid way to create or update rate'
        }
        return Response(request,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,*args,**kwargs):
        response ={
            'message' : 'Invalid way to create or update rate'
        }
        return Response(request,status=status.HTTP_400_BAD_REQUEST)
