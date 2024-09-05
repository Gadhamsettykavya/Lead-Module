from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def get_products(request):

    emp = {
        'product_id' : 2458,
        'product_name' : 'Washing Maching',
        'product_brand' : 'Samsung',

        'specifications' : {
            'capacity' : '7kg',
            'type' : 'Front Load',
            'color' : 'White',
            'energy_rating' : '5 Star',
        },

        'pricing' : {
            'currency' : 'INR',
            'amount' : 35000,

            'discount' : {
                'amount' : 500,
                'expiry_date' : '2024-8-30'
            }
        },
        'availability' : {
            'instock' : True,
            'stockcount' : 25,
            'estimated_delivery' : '2024-6-10'
        }
    }

    return JsonResponse(emp)