from django.http import JsonResponse
from django.http import Http404

RECIPE_BASE = {"name" : [],
               "products" : [],}

PRODUCTS = {"meat" : ["kg",],
            "milk" : ["l",],
            "apple" : ["cnt",]}

def get_data(ind):
    return {"name" : RECIPE_BASE["name"][ind],
            "products" : RECIPE_BASE["products"][ind]}

def recipes(request):
    if request.method == "POST":
        new_name = request.POST.get("name", None)
        if new_name:
            recipe_prod = []
            for product in PRODUCTS.keys():
                amount = request.POST.get(product, None)
                if amount:
                    recipe_prod.append({product : amount})
            for ind, name in enumerate(RECIPE_BASE["name"]):
                if name == new_name:
                    RECIPE_BASE["products"][ind] = recipe_prod
                    status_str = "Recipe updated"
                    break
            else:
                RECIPE_BASE["name"].append(new_name)
                RECIPE_BASE["products"].append(recipe_prod)
                status_str = "New recipe Uploaded"
            return JsonResponse({"status" : status_str})
        else:
            return JsonResponse({"status" : "Invalid recipe"})
    elif request.method == "GET":
        name = request.GET.get("name", None)
        for ind, elem in enumerate(RECIPE_BASE["name"]):
            if name == elem:
                return JsonResponse(get_data(ind))
        raise Http404
    else:
        raise JsonResponse({"status" : "Method not allowed"})

def get_table(request):
    if request.method == "GET":
        return JsonResponse({"data" : RECIPE_BASE})
    raise JsonResponse({"status" : "Method not allowed"})
