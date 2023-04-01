import joblib


purchases_collection = joblib.load('./src/pkls/purchase_collection.pkl')
data_collection = joblib.load('./src/pkls/data_collection.pkl')
companies_collection = joblib.load('./src/pkls/companies_collection.pkl')


async def get_data_database():
    return data_collection


async def get_purchases_database():
    return purchases_collection


async def get_companies_database():
    return companies_collection


async def get_exact_id_data(exact_id: str):
    result = data_collection[data_collection['id']==exact_id]
    return result


async def get_exact_id_purchases(exact_id: str):
    result = purchases_collection[purchases_collection['id']==exact_id]
    return result
