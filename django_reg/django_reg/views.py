from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home(request):
    return render(request, 'home.html')

def result(request):

    cls = joblib.load('laptop_reg.sav')

    lis = []


# Add each parameter to `lis` with default values if missing
    lis.append(request.GET.get('Company', 'Other'))          # Default to 'Unknown' if Company is missing
    lis.append(request.GET.get('TypeName', 'Notebook'))         # Default to 'Unknown' if TypeName is missing
    lis.append(float(request.GET.get('Inches', 13)))            # Default to 0 inches if missing
    lis.append(int(request.GET.get('Ram', 8)))                 # Default to 0 GB RAM if missing
    lis.append(request.GET.get('OS', 'Windows'))               # Default to 'Unknown' if OS is missing
    lis.append((request.GET.get('Screen', 'Standard')))              # Default to 0 if Screen is missing
    lis.append(int(request.GET.get('Touchscreen', 0)))         # Default to 0 if Touchscreen is missing
    lis.append(int(request.GET.get('IPSpanel', 0)))            # Default to 0 if IPSpanel is missing
    lis.append(int(request.GET.get('RetinaDisplay', 0)))       # Default to 0 if RetinaDisplay is missing
    lis.append(float(request.GET.get('CPU_freq', 2.3)))        # Default to 0.0 GHz if CPU_freq is missing
    lis.append(request.GET.get('CPU_model', 'i3'))        # Default to 'Unknown' if CPU_model is missing
    lis.append(int(request.GET.get('PrimaryStorage', 128)))      # Default to 0 GB if PrimaryStorage is missing
    lis.append(int(request.GET.get('SecondaryStorage', 0)))    # Default to 0 GB if SecondaryStorage is missing
    lis.append(request.GET.get('PrimaryStorageType', 'SSD'))  # Default to 'Unknown' if PrimaryStorageType is missing
    lis.append(request.GET.get('SecondaryStorageType', 'No')) # Default to 'Unknown' if SecondaryStorageType is missing
    lis.append(request.GET.get('GPU_company', 'Intel'))      # Default to 'Unknown' if GPU_company is missing
    print(lis)

    ans = cls.predict([lis])


    return render(request, 'result.html',{'ans':ans})