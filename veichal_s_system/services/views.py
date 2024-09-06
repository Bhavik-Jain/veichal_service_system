from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Component, Vehicle, Issue, Transaction
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer, TransactionSerializer
from .config.response import success_response, error_response

class ComponentList(APIView):
    def get(self, request):
        try:
            components = Component.objects.all()
            serializer = ComponentSerializer(components, many=True)
            return success_response(data=serializer.data)
        except Exception as e:
            print("error",e)
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ComponentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Component created successfully.", status=status.HTTP_201_CREATED)
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("error",e)
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ComponentDetail(APIView):
    def get(self, request, pk):
        try:
            component = Component.objects.get(pk=pk)
            serializer = ComponentSerializer(component)
            return success_response(data=serializer.data)
        except Component.DoesNotExist:
            return error_response(message="Component not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("error",e)
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            component = Component.objects.get(pk=pk)
            serializer = ComponentSerializer(component, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Component updated successfully.")
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Component.DoesNotExist:
            return error_response(message="Component not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("error",e)
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            component = Component.objects.get(pk=pk)
            component.delete()
            return success_response(message="Component deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        except Component.DoesNotExist:
            return error_response(message="Component not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("error",e)
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VehicleList(APIView):
    def get(self, request):
        try:
            vehicles = Vehicle.objects.all()
            serializer = VehicleSerializer(vehicles, many=True)
            return success_response(data=serializer.data)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VehicleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Vehicle created successfully.", status=status.HTTP_201_CREATED)
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VehicleDetail(APIView):
    def get(self, request, pk):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
            serializer = VehicleSerializer(vehicle)
            return success_response(data=serializer.data)
        except Vehicle.DoesNotExist:
            return error_response(message="Vehicle not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
            serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Vehicle updated successfully.")
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Vehicle.DoesNotExist:
            return error_response(message="Vehicle not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
            vehicle.delete()
            return success_response(message="Vehicle deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        except Vehicle.DoesNotExist:
            return error_response(message="Vehicle not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class IssueList(APIView):
    def get(self, request):
        try:
            issues = Issue.objects.all()
            serializer = IssueSerializer(issues, many=True)
            return success_response(data=serializer.data)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = IssueSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Issue created successfully.", status=status.HTTP_201_CREATED)
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class IssueDetail(APIView):
    def get(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
            serializer = IssueSerializer(issue)
            return success_response(data=serializer.data)
        except Issue.DoesNotExist:
            return error_response(message="Issue not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
            serializer = IssueSerializer(issue, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Issue updated successfully.")
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Issue.DoesNotExist:
            return error_response(message="Issue not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
            issue.delete()
            return success_response(message="Issue deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        except Issue.DoesNotExist:
            return error_response(message="Issue not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TransactionList(APIView):
    def get(self, request):
        try:
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return success_response(data=serializer.data)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Transaction created successfully.", status=status.HTTP_201_CREATED)
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TransactionDetail(APIView):
    def get(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction)
            return success_response(data=serializer.data)
        except Transaction.DoesNotExist:
            return error_response(message="Transaction not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return success_response(data=serializer.data, message="Transaction updated successfully.")
            return error_response(message="Invalid data.", status=status.HTTP_400_BAD_REQUEST)
        except Transaction.DoesNotExist:
            return error_response(message="Transaction not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
            transaction.delete()
            return success_response(message="Transaction deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        except Transaction.DoesNotExist:
            return error_response(message="Transaction not found.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_response(message=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)