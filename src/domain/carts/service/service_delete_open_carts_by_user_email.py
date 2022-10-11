from src.domain.carts.models.delete_cart import delete_cart


async def service_delete_open_carts_by_user_email(user_email):
        result = await delete_cart(user_email)
        if result == False:
            return False
        return result
