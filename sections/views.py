from django.shortcuts import render, redirect

from .models import Pharmacy
from .models import Medicine
from .models import Distribution

from .forms import PharmacyForm
from .forms import MedicineForm
from .forms import DistributionForm


def hello_world(request):
    return render(request, "sections/home.html")


# Pharmacies
def pharmacies_detail(request, pk):
    pharmacy = Pharmacy.objects.get(pk=pk)
    return render(request, "sections/pharm.html", {
        "pharmacy": pharmacy,
    })



def pharmacies_view(request):
    search = request.GET.get("search")

    if search is None:
        pharmacies = Pharmacy.objects.all()
    else:
        pharmacies = Pharmacy.objects.filter(name__contains=search)

    return render(request, "sections/pharmacy.html", {
        "pharmacies": pharmacies, "search": search,
    })




def pharmacy_create(request):
    if request.method == "GET":
        form = PharmacyForm()
    else:
        form = PharmacyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pharmacy = Pharmacy.objects.create(
                name=data['name'],
                location=data['location'],
                phone_number=data['phone_number'],
                # is_working=data['is_working'],
            )
            return redirect("pharmacies-list")
    return render(request, "sections/pharmacy_create.html", {
        "form": form,
    })




# Medicines
def medicines_detail(request, pk):
    medicine = Medicine.objects.get(pk=pk)
    return render(request, "sections/med_dori.html", {
        "medicine": medicine,
    })



def medicines_view(request):
    search = request.GET.get("search")

    if search is None:
        medicines = Medicine.objects.all()
    else:
        medicines = Medicine.objects.filter(name__contains=search)

    return render(request, "sections/medicine.html", {
        "medicines": medicines, "search": search,
    })



def medicine_create(request):
    if request.method == "GET":
        form = MedicineForm()
    else:
        form = MedicineForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            return redirect("medicines-list")
    return render(request, "sections/medicine_create.html", {
        "form": form,
    })




# Distribution
def distribution_detail(request, pk):
    distribution = Distribution.objects.get(pk=pk)
    return render(request, "sections/distribute.html", {
        "distribution": distribution,
    })



def distribution_view(request):
    search = request.GET.get("search")

    if search is None:
        distribution = Distribution.objects.all()
    else:
        distribution = Distribution.objects.filter(name__contains=search)

    return render(request, "sections/distribution.html", {
        "distribution": distribution, "search": search,
    })




def distribution_create(request):
    if request.method == "GET":
        form = DistributionForm()
    else:
        form = DistributionForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            form.save()
            return redirect("distribution-list")
    return render(request, "sections/distribution_create.html", {
        "form": form,
    })
