from django.contrib.auth.models import User

from web.apps.motorcycle.models import Brand, Model


def brand_model_import(worksheet, user):
    brands = []

    for index, data in enumerate(worksheet.values):
        if index > 0:
            brand_name = data[0]
            brand, brands_created = get_create_brand(
                brands=brands,
                brand_name=brand_name,
                user=user
            )

            if brands_created:
                brands.append(brand)

            model = data[1]
            Model.objects.update_or_create(
                model_name=model,
                brand=brand,
                defaults={
                    'created_user': user,
                    'updated_user': user,
                }
            )

    print(f'Import success!')


def get_create_brand(brands: [Brand], brand_name: str, user: User):
    for brand in brands:
        if brand.name == brand_name:
            return brand, False

    brand, brands_created = Brand.objects.update_or_create(
        name=brand_name,
        defaults={
            'created_user': user,
            'updated_user': user
        }
    )
    return brand, True
