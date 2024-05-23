from django.shortcuts import render,redirect
from django.db.models import Avg
from .models import *
from django.http import HttpResponse



import csv
from io import TextIOWrapper

# def home(request):
#     if request.method == 'POST':
#         lat_data = request.POST.get('lat')
#         lon_data = request.POST.get('lon')
#         if lat_data and lon_data:
#             lat_data = float(lat_data)
#             lon_data = float(lon_data)
#             try:
#                 exact_point = GridPoint.objects.get(latitude=lat_data, longitude=lon_data)
#                 return render(request, 'index.html', {'exact_point': exact_point})
#             except GridPoint.DoesNotExist:
#                 nearest_points = GridPoint.objects.filter(latitude__gte=lat_data-0.08333, 
#                                                            latitude__lte=lat_data+0.08333, 
#                                                            longitude__gte=lon_data-0.08333, 
#                                                            longitude__lte=lon_data+0.08333)
#                 if nearest_points.exists():
#                     average_value = round(nearest_points.aggregate(Avg('value'))['value__avg'], 3)
#                     return render(request, 'index.html', {'average_value': average_value})
#                 else:
#                     return render(request, 'index.html', {'error_message': 'No points found near the provided latitude and longitude.'})
#         elif 'csv_file' in request.FILES:
#             csv_file = request.FILES['csv_file']
#             csv_data = TextIOWrapper(csv_file, encoding=request.encoding)
#             reader = csv.DictReader(csv_data)
#             latitudes = []
#             longitudes = []
#             for row in reader:
#                 latitudes.append(float(row['lat']))
#                 longitudes.append(float(row['lon']))
#             # Process latitude and longitude values as needed
#             lat_avg = sum(latitudes) / len(latitudes)
#             lon_avg = sum(longitudes) / len(longitudes)
#             exact_point = GridPoint.objects.get(latitude=lat_avg, longitude=lon_avg)
#             return render(request, 'index.html', {'exact_point': exact_point})
#         else:
#             return render(request, 'index.html', {'error_message': 'Please provide latitude and longitude or upload a CSV file.'})
#     return render(request, 'index.html')



def home(request):
    if request.method == 'POST':
        lat_data = request.POST.get('lat')
        lon_data = request.POST.get('lon')
        if lat_data and lon_data:
            lat_data = float(lat_data)
            lon_data = float(lon_data)
            try:
                exact_point = GridPoint.objects.get(latitude=lat_data, longitude=lon_data)
                return render(request, 'index.html', {'exact_point': exact_point})
            except GridPoint.DoesNotExist:
                nearest_points = GridPoint.objects.filter(latitude__gte=lat_data-0.08333, 
                                                           latitude__lte=lat_data+0.08333, 
                                                           longitude__gte=lon_data-0.08333, 
                                                          longitude__lte=lon_data+0.08333)
                if nearest_points.exists():
                    average_value = round(nearest_points.aggregate(Avg('value'))['value__avg'], 3)
                    return render(request, 'index.html', {'average_value': average_value,'lat_data':lat_data,'lon_data':lon_data})
                    
                else:
                    return render(request, 'index.html', {'error_message': 'No points found near the provided latitude and longitude.'})
        elif 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            csv_data = TextIOWrapper(csv_file, encoding=request.encoding)
            reader = csv.DictReader(csv_data)
            points_data = []
            for row in reader:
                if row['lat'].strip() and row['lon'].strip():  
                    lat_data = float(row['lat'].strip())
                    lon_data = float(row['lon'].strip())
                    try:
                        exact_point = GridPoint.objects.get(latitude=lat_data, longitude=lon_data)
                        exact_point_dict = {
                            'latitude': exact_point.latitude,
                            'longitude': exact_point.longitude,
                            'value': exact_point.value  # Assuming 'value' is an attribute of GridPoint
                        }
                        points_data.append({'latitude': lat_data, 'longitude': lon_data, 'exact_point': exact_point_dict})
                    except GridPoint.DoesNotExist:
                        nearest_points = GridPoint.objects.filter(latitude__gte=lat_data-0.08333, 
                                                                latitude__lte=lat_data+0.08333, 
                                                                longitude__gte=lon_data-0.08333, 
                                                                longitude__lte=lon_data+0.08333)
                        if nearest_points.exists():
                            average_value = round(nearest_points.aggregate(Avg('value'))['value__avg'], 3)
                            points_data.append({'latitude': lat_data, 'longitude': lon_data, 'average_value': average_value})
                        else:
                            points_data.append({'latitude': lat_data, 'longitude': lon_data, 'error_message': 'No points found near the provided latitude and longitude.'})
                else:
                    points_data.append({'latitude': None, 'longitude': None, 'error_message': 'Latitude or longitude is missing or empty in the CSV row.'})
            
            # Save points_data in session
            request.session['points_data'] = points_data
            return render(request, 'index.html', {'points_data': points_data})
        else:
            return render(request, 'index.html', {'error_message': 'Please provide latitude and longitude or upload a CSV file.'})
    return render(request, 'index.html')




def download_processed_csv(request):
    if 'points_data' in request.session:
        points_data = request.session['points_data']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="processed_data.csv"'
        writer = csv.writer(response)
        writer.writerow(['Latitude', 'Longitude', 'Data'])
        for data in points_data:
            writer.writerow([data['latitude'], data['longitude'], data.get('exact_point', {}).get('value') or data.get('average_value') or data.get('error_message')])
        return response
    else:
        return HttpResponse("No processed data available.", status=404)