from fastapi import APIRouter
from src.domain.address.service.service_get_all_address import service_find_all_address
from src.domain.address.service.service_create_address import service_create_address
from src.domain.address.service.service_delete_address import service_delete_address
from src.domain.address.service.service_get_address_by_email import service_get_address_by_email
from src.domain.schemas.address import AddressSchema
from fastapi import HTTPException, status


routes_address = APIRouter(
    prefix="/api/address",
    tags=["Address"]
)


@routes_address.get("/",
    summary="Search all addresses", 
    description="Route to search all registered addresses",
    status_code=status.HTTP_200_OK)

async def fetch_all_address():
    result = await service_find_all_address()
    if result == False:
        raise Exception(status_code=404, description="There are no registered addresses")
    return result 


@routes_address.get("/find/{email}",
    summary="Search addresses by email", 
    description="Route to look up user address by email address.",
    status_code=status.HTTP_200_OK)

async def get_user_email_address(email):
    result = await service_get_address_by_email(email)
    if result == False:
        raise Exception(status_code=404, description="There is no registered address for this user.")
    return result 


@routes_address.post("/{email}", 
    summary="Creating a new address", 
    description="Route for creating a new address, checking whether or not there are addresses registered for this user.",
    status_code=status.HTTP_201_CREATED)

async def create_address(address: AddressSchema):
    result = await service_create_address(address)
    if result == True:
        return {'mensagem': 'address successfully created'}
    else:
        raise HTTPException(status_code=400, detail="The values entered do not match the required structure.")
    
    
@routes_address.delete("/{address_id}", 
    summary="Delete address by its code", 
    description="Route to delete an address by its code. Only the ObjectId number must be passed",
    status_code=status.HTTP_200_OK)

async def delete_addres_by_code(address_id):
    result = await service_delete_address(address_id)
    if result == True:
        return {'mensagem': 'address successfully deleted'}
    else:
        raise HTTPException(status_code=404, detail="address not found.")