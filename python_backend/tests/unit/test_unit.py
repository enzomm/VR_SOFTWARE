from unittest.mock import patch, MagicMock


IMAGE = 'image'
DESCRIPTION = 'description'
COST = 10.0
TYPE = 'type'


@patch('app.home.routes.ProductForm')
@patch('app.home.routes.request')
@patch('app.home.routes.db.session')
@patch('app.home.routes.Product')
def test_success_set_product(mock_product, mock_session, mock_request, mock_form, client):

    form = MagicMock()
    form.validate.return_value = True
    form.image.data = IMAGE
    form.description.data = DESCRIPTION
    form.cost.data = COST
    form.type.data = TYPE
    mock_form.return_value = form

    mock_request.get_json = MagicMock(return_value={
        'image': IMAGE,
        'description': DESCRIPTION,
        'cost': COST,
        'type': TYPE
    })

    mock_product_instance = MagicMock()
    mock_product.return_value = mock_product_instance

    response = client.post('/set_product')

    mock_request.get_json.assert_called_once()
    mock_form.assert_called_once_with(data=mock_request.get_json.return_value)
    form.validate.assert_called_once()
    mock_product.assert_called_once_with(
        image=IMAGE,
        description=DESCRIPTION,
        cost=COST,
        type=TYPE
    )
    mock_session.add.assert_called_once_with(mock_product_instance)
    mock_session.commit.assert_called_once()
    
    assert response.json == {'message': 'Produto adicionado com sucesso!'}
    assert response.status_code == 201
