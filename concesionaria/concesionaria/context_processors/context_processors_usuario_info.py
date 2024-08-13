def usuario_info(request):
    if request.user.is_authenticated:
        return {
            'user_full_name': f'{request.user.first_name} {request.user.last_name}',
            'user_email': request.user.email,
            'is_staff': request.user.is_staff,
        }
    return {}
