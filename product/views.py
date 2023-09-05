from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer, ProductBestSellerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Min, Max


@api_view(['GET'])
def product(request):
    limit = int(request.GET.get('limit', 12))

    paginator = PageNumberPagination()
    paginator.page_size = limit

    products = Product.objects.all()

    categories = Product.objects.values_list('category', flat=True).distinct()

    category_counts = {cat: Product.objects.filter(
        category=cat).count() for cat in categories}

    paginated_products = paginator.paginate_queryset(products, request)
    current_page = paginator.page.number
    total_pages = paginator.page.paginator.num_pages

    serializer = ProductSerializer(paginated_products, many=True)

    min_price = products.aggregate(Min('price'))['price__min']
    max_price = products.aggregate(Max('price'))['price__max']

    response_data = {
        "current_page": current_page,
        "total_pages": total_pages,
        "category_counts": category_counts,
        "current_range": f"Showing {((current_page - 1) * paginator.page_size) + 1} - {min(current_page * paginator.page_size, paginator.page.paginator.count)} of {products.count()}",
        "min_price": min_price,
        "max_price": max_price,
        "products": serializer.data
    }
    return paginator.get_paginated_response(response_data)


@api_view(['GET'])
def product_detail(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def category_product(request, category):
    limit = int(request.GET.get('limit', 12))
    try:
        products = Product.objects.filter(category=category)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    paginator = PageNumberPagination()
    paginator.page_size = limit
    paginated_products = paginator.paginate_queryset(products, request)
    current_page = paginator.page.number
    total_pages = paginator.page.paginator.num_pages
    serializer = ProductSerializer(paginated_products, many=True)

    min_price = products.aggregate(Min('price'))['price__min']
    max_price = products.aggregate(Max('price'))['price__max']

    response_data = {
        "current_page": current_page,
        "total_pages": total_pages,
        "products": serializer.data,
        "current_range": f"Showing {((current_page - 1) * paginator.page_size) + 1} - {min(current_page * paginator.page_size, paginator.page.paginator.count)} of {products.count()}",
        "min_price": min_price,
        "max_price": max_price,
    }
    return paginator.get_paginated_response(response_data)


@api_view(['GET'])
def best_seller(request):
    products = Product.objects.filter(best_seller=True)
    serializer = ProductBestSellerSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def featured(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_products(request):
    query = request.GET.get('query')
    limit = int(request.GET.get('limit', 12))

    if query:
        results = Product.objects.filter(name__icontains=query)

    else:
        results = []

    paginator = PageNumberPagination()
    paginator.page_size = limit
    paginated_products = paginator.paginate_queryset(results, request)
    current_page = paginator.page.number
    total_pages = paginator.page.paginator.num_pages
    serializer = ProductSerializer(paginated_products, many=True)

    min_price = results.aggregate(Min('price'))['price__min']
    max_price = results.aggregate(Max('price'))['price__max']

    response_data = {
        "current_page": current_page,
        "total_pages": total_pages,
        "current_range": f"Showing {((current_page - 1) * paginator.page_size) + 1} - {min(current_page * paginator.page_size, paginator.page.paginator.count)} of {results.count()}",
        "min_price": min_price,
        "max_price": max_price,
        "products": serializer.data,
    }
    return paginator.get_paginated_response(response_data)


@api_view(['GET'])
def filtered_products(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    limit = int(request.GET.get('limit', 12))

    try:
        min_price = float(min_price) if min_price else None
    except ValueError:
        return Response({"error": "Invalid min_price or max_price"})
    products = Product.objects.all()

    if min_price is not None:
        products = products.filter(price__gte=min_price)
    if max_price is not None:
        products = products.filter(price__lte=max_price)

    paginator = PageNumberPagination()
    paginator.page_size = limit
    paginated_products = paginator.paginate_queryset(products, request)

    current_page = paginator.page.number
    total_pages = paginator.page.paginator.num_pages
    serializer = ProductSerializer(paginated_products, many=True)

    min_price = products.aggregate(Min('price'))['price__min']
    max_price = products.aggregate(Max('price'))['price__max']

    response_data = {
        "current_page": current_page,
        "total_pages": total_pages,
        "products": serializer.data,
        "current_range": f"Showing {((current_page - 1) * paginator.page_size) + 1} - {min(current_page * paginator.page_size, paginator.page.paginator.count)} of {products.count()}",
        "min_price": min_price,
        "max_price": max_price,
    }
    return paginator.get_paginated_response(response_data)
