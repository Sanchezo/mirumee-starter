import json



def test_product_by_id(db, client_query, product):

    response = client_query(
        """
        query myproduct($id: ID!) {
            product(id: $id){
                price
                id
                name
                description
                quantity
            }
        }
        """,
        variables={'id':1}
    )
    content = json.loads(response.content)

    product_response = content['data']['product']

    assert product_response['id'] == str(product.id)
    assert product_response['description'] == product.description
    assert product_response['quantity'] == product.quantity
    assert product_response['price'] == str(product.price)