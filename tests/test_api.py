from app.api import app

def test_success_price():
    client = app.test_client()
    resp = client.post('/price', json={"price":900,"coupon":"SALES10"})
    assert resp.status_code == 200