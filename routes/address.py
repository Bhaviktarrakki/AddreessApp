from fastapi import APIRouter
from config.database import conn
from models.address import address
from schema.address import Address

route = APIRouter()


@route.get("/address")
async def get_addresses(
    lat1: float | None = None,
    long1: float | None = None,
    lat2: float | None = None,
    long2: float | None = None,
):
    if lat1 and long1 and lat2 and long2:
        # return addresses which are betweeng given two distances
        result = conn.execute(
            address.select().where(
                address.c.latitude >= lat1,
                address.c.latitude <= lat2,
                address.c.longitude >= long1,
                address.c.longitude <= long2,
            )
        ).fetchall()
    else:
        result = conn.execute(address.select()).fetchall()

    if not result:
        return {"message": "No addresses found"}
    return result


@route.get("/address/{id}")
async def get_address_by_id(id: int):
    result = conn.execute(address.select().where(address.c.id == id)).fetchall()
    if not result:
        return {"message": "Address does not exist for provided id"}
    return result


@route.post("/address", status_code=201, response_model=Address)
async def add_address(ad: Address):
    query = address.insert().values(
        latitude=ad.latitude,
        longitude=ad.longitude,
        street=ad.street,
        city=ad.city,
        state=ad.state,
        zip_code=ad.zip_code,
    )
    conn.execute(query)
    return {**ad.dict()}


@route.put("/address/{id}", response_model=Address)
async def update_address(id: int, ad: Address):
    query = (
        address.update()
        .where(address.c.id == id)
        .values(
            latitude=ad.latitude,
            longitude=ad.longitude,
            street=ad.street,
            city=ad.city,
            state=ad.state,
            zip_code=ad.zip_code,
        )
    )
    conn.execute(query)
    return {**ad.dict()}


@route.delete("/address/{id}")
async def delete(id: int):
    query = address.delete().where(address.c.id == id)
    return conn.execute(query)
